import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    model = joblib.load('models/job_category_nlp_model.pkl')
    vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_model()

st.set_page_config(page_title="Job Category Predictor", layout="centered")
st.title("Job Category Predictor")

st.write( "This app classifies job postings into categories using " "Natural Language Processing (TF-IDF + Logistic Regression).")

job_title = st.text_input("Enter the job title:",placeholder="e.g. Senior Python Developer") 
job_description = st.text_area("Enter the job description (optional):",placeholder="e.g. We are looking for a Senior Python Developer with experience in Django and REST APIs...")

if st.button("Predict Job Category"):
    if job_title.strip() == "":
        st.warning("Please enter a job title to get a prediction.")
    else:
        input_text = job_title + " " + job_description
        input_vec = vectorizer.transform([input_text])
        prediction = model.predict(input_vec)[0]
        st.success(f"The predicted job category is: **{prediction}**")

        probs = model.predict_proba(input_vec)[0]
        confidence = max(probs)
        st.write(f"Prediction confidence: {confidence:.2%}")

st.markdown("---")
st.caption("Built by Senitha Gunathilaka • NLP Project • Deployed with Streamlit")