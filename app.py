import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model and encoder
model = joblib.load('final_xgb_classifier.joblib')
label_encoder = joblib.load('final_label_encoder.joblib')

# Define the symptom categories and their corresponding symptoms
symptom_categories = {
    "Skin Conditions": [
        "itching", "skin_rash", "nodal_skin_eruptions", "ulcers_on_tongue", "redness_of_eyes",
        "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
        "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze",
        "dischromic_patches", "watering_from_eyes", "pus_filled_pimples", "brittle_nails"
    ],
    "Digestive System": [
        "stomach_pain", "acidity", "vomiting", "diarrhoea", "constipation", "abdominal_pain",
        "nausea", "loss_of_appetite", "stomach_bleeding", "distention_of_abdomen", "belly_pain",
        "passage_of_gases", "internal_itching", "indigestion", "bloody_stool"
    ],
    "Immune System": [
        "shivering", "chills", "swelled_lymph_nodes", "malaise", "high_fever", "sweating",
        "dehydration", "red_spots_over_body", "continuous_sneezing", "acute_liver_failure",
        "mild_fever"
    ],
    "Respiratory System": [
        "cough", "breathlessness", "phlegm", "throat_irritation", "sinus_pressure", "runny_nose",
        "congestion", "mucoid_sputum", "rusty_sputum", "blood_in_sputum", "chest_pain",
        "sunken_eyes", "yellowing_of_eyes"
    ],
    "Cardiovascular System": [
        "fast_heart_rate", "palpitations", "painful_walking", "prominent_veins_on_calf",
        "swelling_of_stomach", "swollen_blood_vessels"
    ],
    "Nervous System": [
        "headache", "dizziness", "cramps", "slurred_speech", "knee_pain", "hip_joint_pain",
        "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness", "spinning_movements",
        "loss_of_balance", "unsteadiness", "weakness_of_one_body_side", "altered_sensorium",
        "lack_of_concentration", "visual_disturbances", "coma", "blurred_and_distorted_vision",
        "drying_and_tingling_lips", "pain_behind_the_eyes"
    ],
    "Endocrine System": [
        "fatigue", "weight_gain", "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss",
        "restlessness", "lethargy", "irregular_sugar_level", "increased_appetite", "polyuria",
        "excessive_hunger", "enlarged_thyroid", "swollen_extremeties", "obesity",
        "puffy_face_and_eyes"
    ],
    "Urinary System": [
        "burning_micturition", "spotting_urination", "yellow_urine", "foul_smell_of_urine",
        "bladder_discomfort", "continuous_feel_of_urine", "dark_urine"
    ],
    "Musculoskeletal System": [
        "joint_pain", "muscle_wasting", "back_pain", "fluid_overload", "weakness_in_limbs",
        "pain_during_bowel_movements", "pain_in_anal_region", "neck_pain", "muscle_pain",
        "bruising", "swollen_legs"
    ],
    "Other/Infectious": [
        "history_of_alcohol_consumption", "receiving_blood_transfusion", "receiving_unsterile_injections",
        "family_history", "extra_marital_contacts", "patches_in_throat", "abnormal_menstruation",
        "irritability", "toxic_look_(typhos)", "depression", "yellowish_skin", "loss_of_smell", "irritation_in_anus"
    ]
}

st.title("Intelligent Disease Diagnosing System")
st.write("Please check the boxes if you are genuinely experiencing these symptoms.")
# Collect user input, organized by categories
user_symptoms = {}
symptoms_list = []  # Initialize an empty list for symptom names
selected_symptoms = []  # List to store the names of selected symptoms

for category, symptoms in symptom_categories.items():
    with st.expander(category):
        for symptom in symptoms:
            unique_key = f"{category}_{symptom}" 
            user_symptoms[symptom] = st.checkbox(symptom, value=False, key=unique_key)
            symptoms_list.append(symptom)  # Add symptom names to the list
            if user_symptoms[symptom]:
                selected_symptoms.append(symptom)  # Add selected symptom to the list

# Create a DataFrame for prediction, ensuring the correct order of symptoms
input_data = pd.DataFrame([user_symptoms])
input_data = input_data[symptoms_list]  # Reorder columns to match training data

# Make prediction on button click
if st.button("Predict"):
    if len(selected_symptoms) < 2:
        st.warning("Please select at least two symptoms.")
    else:
        input_data = input_data.astype(int)  # Convert input_data, not input
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        
        predicted_disease = label_encoder.inverse_transform(prediction)[0]
        predicted_probabilities = prediction_proba[0]  # Extract probabilities for the predicted class

        # Create a DataFrame for diseases and their probabilities
        proba_df = pd.DataFrame({
            'Disease': label_encoder.classes_,
            'Probability': predicted_probabilities
        })
        
        # Sort the DataFrame by probabilities in descending order
        proba_df = proba_df.sort_values(by='Probability', ascending=False)

        st.subheader("Prediction Results:")
        st.write("Name : Venkata Ramana")
        st.write("Age : 54")
        st.write("Gender : Male")
        st.write("Selected Symptoms:")
        st.write(", ".join(selected_symptoms))
        st.write(f"Predicted Disease: {predicted_disease}")
        st.write(f"Based on the symptoms you have given, the predicted disease with higher probability is {predicted_disease}")
        st.write(f"As you are  a Chemical worker and also exposed to agrochemicals since 20 years,this {predicted_disease} may  be caused due to the exposure to agrochemicals ")
        st.button("Learn More")
        
        st.subheader("Prediction Probabilities:")
        for i, row in proba_df.iterrows():
            st.write(f"{row['Disease']}: {row['Probability']:.4f}")
