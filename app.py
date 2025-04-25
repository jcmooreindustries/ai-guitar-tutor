# File: app.py

import streamlit as st
from modules import pose_tracking, feedback
import json

st.set_page_config(page_title="AI Guitar Tutor", layout="wide")
st.title("🎸 AI Guitar Tutor (Prototype)")

# Step 1: Load chord library
try:
    with open("data/chord_library.json", "r") as f:
        chord_library = json.load(f)
except FileNotFoundError:
    st.error("Chord library not found.")
    st.stop()

# Step 2: Chord selection
chord_name = st.selectbox("Choose a chord to practice:", list(chord_library.keys()))
target_shape = chord_library[chord_name]

# Step 3: Webcam feed and hand tracking
frame = pose_tracking.get_hand_pose()

# Step 4: Show webcam + pose results
if frame is not None:
    st.image(frame, channels="RGB", caption="Live Feed with Hand Pose")
    result = feedback.compare_pose(frame, target_shape)
    st.markdown(f"**Feedback:** {result}")
else:
    st.warning("Waiting for webcam input...")
