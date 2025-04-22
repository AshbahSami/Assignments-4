import streamlit as st
import pandas as pd

st.title("💪 BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is **{bmi:.2f}**")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

st.success(f"Category: **{category}**")

st.subheader("📊 BMI Categories")
st.markdown("""
| BMI Range | Category       |
|-----------|----------------|
| < 18.5    | Underweight    |
| 18.5–24.9 | Normal weight  |
| 25–29.9   | Overweight     |
| 30+       | Obese          |
""")
