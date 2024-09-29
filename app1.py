import streamlit as st

# Title and description
st.title("AI-Powered Medical Chatbot")
st.write(
    "Get preliminary assessments, personalized health recommendations, and schedule appointments with healthcare providers.")

# Sidebar - Input parameters
st.sidebar.header("Patient Information")
age = st.sidebar.slider("Age", 0, 100, 25)
gender = st.sidebar.selectbox("Gender", ("Male", "Female", "Other"))
st.sidebar.text("Existing Conditions (Optional)")
hypertension = st.sidebar.checkbox("Hypertension")
diabetes = st.sidebar.checkbox("Diabetes")
obesity = st.sidebar.checkbox("Obesity")
asthma = st.sidebar.checkbox("Asthma")
other_conditions = st.sidebar.text_input("Other conditions", "")

# Symptom Input
st.header("Symptom Checker")
st.write("Please input your symptoms below to get a preliminary assessment.")
symptoms = st.text_area("Enter your symptoms (e.g., headache, fever, cough):")

# Recommendations
if st.button("Get Preliminary Assessment"):
    if symptoms:
        # Simple logic to determine assessment and recommendation
        # In real-world applications, this will be connected to an AI/ML model or API
        st.subheader("Preliminary Assessment")
        if "fever" in symptoms.lower() and "cough" in symptoms.lower():
            st.write("Possible Condition: Flu or COVID-19")
            st.write("Recommendation: Please schedule a COVID-19 test and consult a healthcare provider.")

        elif "headache" in symptoms.lower() and age > 50 and hypertension:
            st.write("Possible Condition: Hypertension-related headache")
            st.write("Recommendation: Monitor your blood pressure and consult a healthcare provider.")

        else:
            st.write(
                "We cannot identify a specific condition based on the symptoms provided. Please consult a healthcare professional.")

        # Personalized Recommendations based on health profile
        st.subheader("Personalized Recommendations")
        if age > 50:
            st.write("Since you're over 50, we recommend regular cardiovascular check-ups.")
        if diabetes:
            st.write("You have diabetes. Ensure regular blood sugar monitoring and stick to a low-sugar diet.")
        if obesity:
            st.write("We recommend a diet and exercise plan to manage obesity. Consider consulting a nutritionist.")
        if asthma:
            st.write("Keep an inhaler with you and avoid exposure to allergens to manage asthma.")
    else:
        st.write("Please input symptoms to get an assessment.")

# Appointment Scheduling
st.header("Schedule an Appointment")
appointment_type = st.selectbox("Select Appointment Type",
                                ("General Consultation", "Cardiologist", "Endocrinologist", "Pulmonologist", "Other"))
preferred_date = st.date_input("Preferred Appointment Date")
preferred_time = st.time_input("Preferred Appointment Time")

if st.button("Schedule Appointment"):
    st.write(f"Appointment Scheduled with a {appointment_type} on {preferred_date} at {preferred_time}.")
    st.write("You will receive a confirmation email shortly.")

# End
st.write("Thank you for using our medical chatbot. Stay healthy!")
