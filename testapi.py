import streamlit as st
import os
import random

# ---------------- CONFIG ----------------
st.title("🧪 Visual Test - Local Images")

# ---------------- FUNCTION ----------------
def get_visual(interest):
    folder = f"assets/visuals/{interest.lower()}"

    st.write("📂 Looking in folder:", folder)

    if os.path.exists(folder):
        images = os.listdir(folder)

        # filter only image files
        images = [img for img in images if img.endswith((".jpg", ".png", ".jpeg"))]

        st.write("🖼️ Found images:", images)

        if images:
            return os.path.join(folder, random.choice(images))

    return None

# ---------------- INPUT ----------------
user_text = st.text_area("Enter text:")

if st.button("Test Visual"):

    # for now hardcode interest
    interest = "technology"

    st.write("🎯 Interest:", interest)

    img_path = get_visual(interest)

    if img_path:
        st.success("✅ Image Loaded Successfully")
        st.image(img_path, use_column_width=True)
    else:
        st.error("❌ No image found in folder")