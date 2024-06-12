
import streamlit as st

def calculate_health_score(symptoms):
    return sum(symptoms.values()) / len(symptoms)

def provide_guidance(score):
    if score < 3:
        return "Your symptoms are mild. Stay hydrated and rest."
    elif score < 7:
        return "Your symptoms are moderate. Monitor closely and consider contacting a healthcare provider."
    else:
        return "Your symptoms are severe. Seek medical attention immediately."

st.title('COVID-19 Health Monitoring and Symptom Tracker')

symptoms = {
    'Fever': st.slider('Fever (0-10)', 0, 10, 0),
    'Fatigue': st.slider('Fatigue (0-10)', 0, 10, 0),
    'Cough': st.slider('Cough (0-10)', 0, 10, 0),
    'Shortness of Breath': st.slider('Shortness of Breath (0-10)', 0, 10, 0),
    'Loss of Taste/Smell': st.slider('Loss of Taste/Smell (0-10)', 0, 10, 0),
}

if st.button('Calculate Health Score'):
    health_score = calculate_health_score(symptoms)
    st.write(f'Your health score is {health_score:.2f}')
    st.write(provide_guidance(health_score))
    