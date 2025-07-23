import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from train_model import  categorical_features,numeric_features# Assuming the model is trained and saved in train_model.py

# Load model and data
model = joblib.load('costco_fulfillment_model.pkl')
warehouses = pd.read_csv('costco_warehouses.csv')

# App title
st.title("Costco Order Fulfillment Time Predictor")
st.markdown("""
This tool predicts order fulfillment times and identifies bottlenecks in Costco's supply chain.
""")

# Sidebar for input parameters
st.sidebar.header("Order Details")

# Input form
with st.form("order_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        warehouse_id = st.selectbox(
            "Warehouse ID",
            options=warehouses['warehouse_id'].unique()
        )
        membership_type = st.selectbox(
            "Membership Type",
            options=['Gold Star', 'Executive', 'Business']
        )
        num_items = st.number_input(
            "Number of Items",
            min_value=1,
            max_value=50,
            value=5
        )
        
    with col2:
        total_weight = st.number_input(
            "Total Weight (lbs)",
            min_value=1.0,
            max_value=500.0,
            value=25.0
        )
        order_date = st.date_input(
            "Order Date",
            value=datetime.now()
        )
        order_time = st.time_input(
            "Order Time",
            value=datetime.now().time()
        )
    
    submit_button = st.form_submit_button("Predict Fulfillment Time")

# Process input and make prediction
if submit_button:
    # Prepare input data
    order_datetime = datetime.combine(order_date, order_time)
    is_weekend = 1 if order_datetime.weekday() >= 5 else 0
    is_holiday = 1 if order_datetime.month == 12 and order_datetime.day in range(15, 26) else 0
    
    warehouse_data = warehouses[warehouses['warehouse_id'] == warehouse_id].iloc[0]
    
    input_data = pd.DataFrame([{
        'warehouse_id': warehouse_id,
        'membership_type': membership_type,
        'num_items': num_items,
        'total_weight': total_weight,
        'is_weekend': is_weekend,
        'is_holiday': is_holiday,
        'order_month': order_datetime.month,
        'order_dayofweek': order_datetime.weekday(),
        'order_hour': order_datetime.hour,
        'region': warehouse_data['region'],
        'staff_level': warehouse_data['staff_level']
    }])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display results
    st.subheader("Prediction Results")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Predicted Fulfillment Time", f"{prediction:.1f} hours")
        
        if prediction <= 48:
            st.success("This order is predicted to meet the 48-hour SLA")
        else:
            st.error("This order is at risk of missing the 48-hour SLA")
    
    with col2:
        # Get feature importances
        feature_importances = model.named_steps['regressor'].feature_importances_
        feature_names = (model.named_steps['preprocessor']
                        .named_transformers_['cat']
                        .named_steps['onehot']
                        .get_feature_names_out(categorical_features))
        
        all_feature_names = numeric_features + list(feature_names)
        importance_df = pd.DataFrame({
            'Feature': all_feature_names,
            'Importance': feature_importances
        }).sort_values('Importance', ascending=False).head(10)
        
        fig, ax = plt.subplots()
        ax.barh(importance_df['Feature'], importance_df['Importance'])
        ax.set_xlabel('Importance')
        ax.set_title('Top Factors Affecting Fulfillment Time')
        st.pyplot(fig)
    
    # Bottleneck analysis
    st.subheader("Bottleneck Analysis")
    
    # Simulate stage times (in a real app, these would come from model components)
    stages = {
        'Processing': prediction * 0.3,
        'Picking': prediction * 0.4,
        'Packing': prediction * 0.1,
        'Shipping': prediction * 0.2
    }
    
    bottleneck = max(stages, key=stages.get)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Time by Stage:")
        for stage, time in stages.items():
            st.write(f"- {stage}: {time:.1f} hours")
    
    with col2:
        st.warning(f"Potential Bottleneck: {bottleneck} stage")
        
        if bottleneck == 'Picking':
            st.write("Recommendations:")
            st.write("- Optimize warehouse layout")
            st.write("- Increase picker staff during peak hours")
            st.write("- Implement batch picking for multi-item orders")
        elif bottleneck == 'Shipping':
            st.write("Recommendations:")
            st.write("- Negotiate better carrier contracts")
            st.write("- Implement regional fulfillment centers")
            st.write("- Offer tiered shipping options")

# Add historical data visualization
st.subheader("Historical Performance")
show_historical = st.checkbox("Show historical fulfillment times")

if show_historical:
    orders = pd.read_csv('costco_orders.csv')
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    time_period = st.selectbox(
        "Time Period",
        options=['Last 7 days', 'Last 30 days', 'Last 90 days', 'Last year']
    )
    
    if time_period == 'Last 7 days':
        cutoff = datetime.now() - timedelta(days=7)
    elif time_period == 'Last 30 days':
        cutoff = datetime.now() - timedelta(days=30)
    elif time_period == 'Last 90 days':
        cutoff = datetime.now() - timedelta(days=90)
    else:
        cutoff = datetime.now() - timedelta(days=365)
    
    filtered = orders[orders['order_date'] >= cutoff]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered['order_date'], filtered['total_fulfillment_time_hrs'], alpha=0.5)
    ax.axhline(y=48, color='r', linestyle='--', label='48-hour SLA')
    ax.set_xlabel('Order Date')
    ax.set_ylabel('Fulfillment Time (hours)')
    ax.set_title('Actual Fulfillment Times')
    ax.legend()
    st.pyplot(fig)