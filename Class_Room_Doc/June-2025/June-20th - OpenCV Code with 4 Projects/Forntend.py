import streamlit as st
import cv2
import numpy as np
import tempfile
import os

# ----------------- Page Configuration -----------------
st.set_page_config(page_title="🧊 Pedestrian Detection AI", layout="wide")

# ----------------- Custom Glassmorphism CSS -----------------
st.markdown("""
    <style>
    /* Global Background */
    body {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
    }

    .main {
        background-color: transparent;
    }

    /* Glass Panel Style */
    .glass {
        background: rgba(255, 255, 255, 0.35);
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 30px;
        margin: 20px 0;
    }

    h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif;
        color: #0d47a1;
        text-align: center;
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(255, 255, 255, 0.3);
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
        border-top: 1px solid #ccc;
    }

    .stSidebar {
        background-color: #e1f5fe;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.markdown("<h1>🧊 Pedestrian Detection AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#4f4f4f;'>Elegant, Accurate, and Client-Ready AI Video Analysis Tool</h4><hr>", unsafe_allow_html=True)

# ----------------- Sidebar Controls -----------------
st.sidebar.markdown("### 📂 Upload & Settings")
video_file = st.sidebar.file_uploader("📼 Upload your video", type=["mp4", "avi", "mov"])
show_boxes = st.sidebar.checkbox("🖼️ Show Detection Boxes", value=True)
scale_factor = st.sidebar.slider("🔍 Detection Scale", 1.05, 1.5, 1.2, step=0.05)
min_neighbors = st.sidebar.slider("👁️‍🗨️ Min Neighbors", 1, 10, 3)

# ----------------- Load Haar Classifier -----------------
haar_path = r'./Haarcascades/haarcascade_fullbody.xml'

if not os.path.exists(haar_path):
    st.error("🚫 Haar XML not found.")
    st.stop()

classifier = cv2.CascadeClassifier(haar_path)
if classifier.empty():
    st.error("❌ Error loading classifier.")
    st.stop()

# ----------------- Main Content -----------------

if video_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()
    detected = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = classifier.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=(50, 50))

        if len(bodies) > 0:
            detected = True
            status = "🟢 Pedestrians Found"
        else:
            status = "🔍 Scanning..."

        if show_boxes:
            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 153, 0), 2)

        frame = cv2.resize(frame, (720, 400))
        stframe.image(frame, channels="BGR", caption=status)

    cap.release()

    if detected:
        st.success("✅ Detection complete. Pedestrians detected.")
        st.balloons()
    else:
        st.warning("⚠️ No pedestrians were found in this video.")

st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Footer -----------------
st.markdown('<div class="footer">💎 Created by Mahesh Babu | 🌐 AI with Elegance | Powered by OpenCV & Streamlit</div>', unsafe_allow_html=True)
