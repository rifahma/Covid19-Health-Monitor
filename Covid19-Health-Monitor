!pip install streamlit pandas openpyxl

%%writefile app.py
import streamlit as st
import pandas as pd

def calculate_health_score(symptoms):
    weights = {
        'fever': 1.0,
        'fatigue': 0.8,
        'dry_cough': 0.7,
        'shortness_of_breath': 1.2,
        'sore_throat': 0.5,
        'headache': 0.6,
        'muscle_pain': 0.6,
        'loss_of_taste_smell': 0.9,
        'runny_nose': 0.4,
        'diarrhea': 0.3
    }
    score = sum(weights[symptom] * severity for symptom, severity in symptoms.items())
    return score

@st.cache
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

st.title('COVID-19 Health Monitoring and Symptom Tracker')

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("Data loaded successfully!")
    st.write(df.head())

    st.sidebar.title("Symptoms Severity Input")
    symptoms = {}
    symptoms['fever'] = st.sidebar.slider('Fever', 0, 10, 0)
    symptoms['fatigue'] = st.sidebar.slider('Fatigue', 0, 10, 0)
    symptoms['dry_cough'] = st.sidebar.slider('Dry Cough', 0, 10, 0)
    symptoms['shortness_of_breath'] = st.sidebar.slider('Shortness of Breath', 0, 10, 0)
    symptoms['sore_throat'] = st.sidebar.slider('Sore Throat', 0, 10, 0)
    symptoms['headache'] = st.sidebar.slider('Headache', 0, 10, 0)
    symptoms['muscle_pain'] = st.sidebar.slider('Muscle Pain', 0, 10, 0)
    symptoms['loss_of_taste_smell'] = st.sidebar.slider('Loss of Taste/Smell', 0, 10, 0)
    symptoms['runny_nose'] = st.sidebar.slider('Runny Nose', 0, 10, 0)
    symptoms['diarrhea'] = st.sidebar.slider('Diarrhea', 0, 10, 0)

    if st.sidebar.button('Calculate Health Score'):
        health_score = calculate_health_score(symptoms)
        st.write(f'Health Score: {health_score}')

    if st.sidebar.button('Personalized Guidance'):
        health_score = calculate_health_score(symptoms)
        st.write(f'Health Score: {health_score}')
        if health_score > 15:
            st.write("High risk. Consult a healthcare provider immediately.")
        elif 10 < health_score <= 15:
            st.write("Moderate risk. Monitor symptoms and consider seeking medical advice.")
        else:
            st.write("Low risk. Maintain regular precautions.")

%%writefile requirements.txt
streamlit
pandas
openpyxl
