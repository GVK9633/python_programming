import streamlit as st
import numpy as np

# Set page config
st.set_page_config(
    page_title="Modern Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 20px;
        border-radius: 10px;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: right;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🧮 Modern Calculator")

# Initialize session state for calculator
if 'current_value' not in st.session_state:
    st.session_state.current_value = '0'
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'first_number' not in st.session_state:
    st.session_state.first_number = None

# Display result
st.markdown(f'<div class="result-box">{st.session_state.current_value}</div>', unsafe_allow_html=True)

# Function to handle number input
def number_click(number):
    if st.session_state.current_value == '0':
        st.session_state.current_value = str(number)
    else:
        st.session_state.current_value += str(number)

# Function to handle operation
def operation_click(op):
    if st.session_state.first_number is None:
        st.session_state.first_number = float(st.session_state.current_value)
        st.session_state.operation = op
        st.session_state.current_value = '0'

# Function to calculate result
def calculate():
    if st.session_state.first_number is not None and st.session_state.operation is not None:
        second_number = float(st.session_state.current_value)
        if st.session_state.operation == '+':
            result = st.session_state.first_number + second_number
        elif st.session_state.operation == '-':
            result = st.session_state.first_number - second_number
        elif st.session_state.operation == '×':
            result = st.session_state.first_number * second_number
        elif st.session_state.operation == '÷':
            if second_number == 0:
                st.error("Cannot divide by zero!")
                return
            result = st.session_state.first_number / second_number
        
        st.session_state.current_value = str(result)
        st.session_state.first_number = None
        st.session_state.operation = None

# Function to clear calculator
def clear():
    st.session_state.current_value = '0'
    st.session_state.first_number = None
    st.session_state.operation = None

# Create calculator layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=number_click, args=(7,))
    st.button("4", on_click=number_click, args=(4,))
    st.button("1", on_click=number_click, args=(1,))
    st.button("C", on_click=clear)

with col2:
    st.button("8", on_click=number_click, args=(8,))
    st.button("5", on_click=number_click, args=(5,))
    st.button("2", on_click=number_click, args=(2,))
    st.button("0", on_click=number_click, args=(0,))

with col3:
    st.button("9", on_click=number_click, args=(9,))
    st.button("6", on_click=number_click, args=(6,))
    st.button("3", on_click=number_click, args=(3,))
    st.button(".", on_click=number_click, args=('.',))

with col4:
    st.button("÷", on_click=operation_click, args=('÷',))
    st.button("×", on_click=operation_click, args=('×',))
    st.button("-", on_click=operation_click, args=('-',))
    st.button("+", on_click=operation_click, args=('+',))

# Equal button
st.button("=", on_click=calculate) 