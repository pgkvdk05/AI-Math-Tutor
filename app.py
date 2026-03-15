import streamlit as st
import cv2
import numpy as np
from PIL import Image
import re

from vision.ocr import extract_equation_from_image
from services.gemini_service import solve_equation_with_gemini


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="AI Math Tutor",
    page_icon="🧠",
    layout="wide"
)

st.title("AI Math Tutor")
st.write("Upload an algebra equation image or type the equation manually.")

# -----------------------------
# Helper Function
# -----------------------------

def normalize_equation(eq):
    """
    Convert OCR text to valid math expression
    """
    eq = eq.replace("^", "**")

    # convert 3x -> 3*x
    eq = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', eq)

    return eq


# -----------------------------
# Tabs UI
# -----------------------------

tab1, tab2 = st.tabs(["Upload Image", "Type Equation"])

# ======================================================
# TAB 1 — IMAGE OCR
# ======================================================

with tab1:

    uploaded_file = st.file_uploader(
        "Upload Equation Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        col1, col2 = st.columns(2)

        image = Image.open(uploaded_file)

        with col1:
            st.subheader("Uploaded Image")
            st.image(image, width=300)

        # Convert image for OCR
        img = np.array(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        with col2:
            st.subheader("Processed Image")
            st.image(gray, width=300)

        # OCR extraction
        equation = extract_equation_from_image(gray)

        equation = equation.replace(" ", "")

        st.markdown("### Recognized Equation")

        st.code(equation)

        st.latex(equation)

        # Solve Button
        if st.button("Solve Equation", key="solve_image"):

            equation = normalize_equation(equation)

            with st.spinner("Gemini AI solving..."):

                solution = solve_equation_with_gemini(equation)

                st.markdown("### Step-by-Step Solution")

                st.write(solution)


# ======================================================
# TAB 2 — MANUAL INPUT
# ======================================================

with tab2:

    st.markdown("### Enter Equation Manually")

    user_equation = st.text_input(
        "Type algebra equation",
        placeholder="Example: 3x + 5 = 14"
    )

    if user_equation:

        equation = user_equation.replace(" ", "")

        st.markdown("### Recognized Equation")

        st.code(equation)

        st.latex(equation)

        if st.button("Solve Equation", key="solve_manual"):

            equation = normalize_equation(equation)

            with st.spinner("Gemini AI solving..."):

                solution = solve_equation_with_gemini(equation)

                st.markdown("### Step-by-Step Solution")

                st.write(solution)


# -----------------------------
# Footer
# -----------------------------

st.markdown("---")
st.caption("Powered by Gemini AI + Streamlit")