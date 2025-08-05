import streamlit as st
import joblib

# Load model and vectorizer with new filenames
model = joblib.load("model3.pkl")
vectorizer = joblib.load("vectorizer3.pkl")

st.title("📧 Spam Email Classifier")
st.write("Enter an email message and this app will predict whether it's **Spam** or **Ham (Not Spam)**.")

user_input = st.text_area("✉️ Enter the email text below:")

if st.button("Predict"):
    input_data = [user_input]
    transformed_input = vectorizer.transform(input_data)
    prediction = model.predict(transformed_input)

    if prediction[0] == 1:
        st.success("✅ This is a **Ham** email.")
    else:
        st.error("🚫 This is a **Spam** email.")
