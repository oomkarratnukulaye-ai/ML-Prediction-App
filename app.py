import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("model.pkl")

# UI
st.set_page_config(page_title="Prediction App", page_icon="💡")

st.title("💡 ML Prediction App")
st.write("Enter details below to get prediction")

# inputs
age = st.number_input("Enter Age", min_value=1, max_value=100, value=25)
salary = st.number_input("Enter Salary", min_value=0, value=50000)

# predict button
if st.button("Predict"):
    prediction = model.predict(np.array([[age, salary]]))

    # result logic
    if prediction[0] == 1:
        st.success("✅ Result: Customer WILL BUY")
    else:
        st.error("❌ Result: Customer will NOT BUY")

    st.info(f"Raw Output: {prediction[0]}")