import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Capital Letter Detector (Demo)", layout="centered")
st.title("🧠 Capital Letter Detector (Demo Only)")

st.write("Upload a handwritten image. This demo version **simulates OCR output** without using Tesseract (not supported on Streamlit Cloud).")

uploaded_file = st.file_uploader("Choose a handwritten image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and convert image
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)

    # Simulate detection by drawing a few fake boxes
    height, width = img_np.shape[:2]
    box_coords = [
        (50, 40, 80, 90),
        (200, 50, 230, 100),
        (350, 70, 380, 120)
    ]

    for (x1, y1, x2, y2) in box_coords:
        cv2.rectangle(img_np, (x1, y1), (x2, y2), (0, 255, 0), 2)

    st.image(img_np, caption="(Simulated) Capital Letters Highlighted", use_column_width=True)

    st.subheader("📋 Extracted Capital Letters")
    st.code("HELLO
WORLD
TEST")
else:
    st.info("Upload an image to simulate capital letter detection.")
