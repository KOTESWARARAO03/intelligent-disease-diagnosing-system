# 🩺 Intelligent Disease Diagnosing System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://intelligent-diagnosis-agrochemicals.streamlit.app/)

## 📋 Description

This Intelligent Disease Diagnosing System is a web application built with Streamlit that predicts potential diseases based on user-input symptoms. It's particularly focused on diseases that may be caused or exacerbated by exposure to agrochemicals.

## 🚀 Features

- Interactive symptom selection organized by body systems
- Disease prediction using a trained XGBoost classifier
- Probability distribution for various diseases
- Tailored results for chemical workers exposed to agrochemicals

## 🛠️ Installation

1. Clone this repository:
git clone https://github.com/your-username/intelligent-disease-diagnosis.git
Copy
2. Navigate to the project directory:
cd intelligent-disease-diagnosis
Copy
3. Install the required packages:
pip install -r requirements.txt
Copy
## 🏃‍♂️ How to Run

Run the Streamlit app locally:
streamlit run app.py
Copy
Or visit the deployed app at: [https://intelligent-diagnosis-agrochemicals.streamlit.app/](https://intelligent-diagnosis-agrochemicals.streamlit.app/)

## 📊 How It Works

1. Select your symptoms from the categorized checkboxes.
2. Click the "Predict" button to get results.
3. View the predicted disease, its probability, and other possible conditions.
4. Get additional context related to agrochemical exposure.

## 🧠 Model Information

- The system uses an XGBoost classifier trained on a dataset of symptoms and diseases.
- The model and label encoder are loaded from joblib files.

## 📁 File Structure

- `app.py`: Main Streamlit application
- `final_xgb_classifier.joblib`: Trained XGBoost model
- `final_label_encoder.joblib`: Label encoder for disease names
- `requirements.txt`: Required Python packages

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## 📄 License

This project is licensed under the terms of the LICENSE file included in the repository.

## 👥 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/intelligent-disease-diagnosis/issues).


---

Made with ❤️ by [Your Name]
