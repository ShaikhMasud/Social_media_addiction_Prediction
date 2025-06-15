# 📱 Social Media Addiction Prediction System

A smart, secure, and scalable web-based system that predicts the risk of social media addiction using psychological and behavioral traits. Powered by **XGBoost** and wrapped in a user-friendly **Django** interface, this project combines machine learning with practical usability to raise awareness and promote healthier digital habits.

---


## 🚀 Features

* ✅ **93% Accuracy** using XGBoost classifier (outperforms Random Forest)
* 🧠 Behavioral & psychological data-driven insights
* 🔐 Secure preprocessing for handling sensitive information
* 📊 Detailed EDA to understand correlations and user behavior patterns
* 🌐 Real-time prediction via a Django-powered web interface
* 📋 Personalized recommendations to reduce risk of addiction using gemini integretion

---

## 🧠 About the Model

The core of this system is an XGBoost model, trained on a dataset containing key behavioral and psychological indicators. After comparing multiple models, **XGBoost** was chosen due to its superior performance and accuracy.

* ✅ **Model Used**: XGBoost Classifier
* 📁 Trained model stored as a `.pkl` file for seamless integration
* 📉 Compared against Random Forest and other baseline classifiers

---

Google collab file: https://colab.research.google.com/drive/1fVxxhVHNHtYCqje-S8NCe1n_rQxO7b2c?usp=sharing

---

## 🛠️ Tech Stack

* **Frontend**: HTML/CSS (via Django templates)
* **Backend**: Python, Django
* **Machine Learning**: XGBoost, Pandas, Scikit-learn
* **Deployment**: Localhost / Cloud-ready

---

## 🧪 EDA & Preprocessing Highlights

* Correlation heatmaps and feature importance visualizations
* Normalization and encoding of user inputs
* Secure handling of personal data with anonymization techniques

---

## 🌐 How It Works

1. 📝 User fills in a simple form with behavioral and psychological inputs.
2. 🧠 The Django server loads the `.pkl` model and predicts addiction risk.
3. 📊 The result is displayed with a prediction score and tailored advice.


---

## 📦 Installation

```bash
git clone https://github.com/your-username/social-media-addiction-predictor.git
cd social-media-addiction-predictor
pip install -r requirements.txt
python manage.py runserver
```

> Visit `http://localhost:8000/` to get started!

---

## 📚 References

* [XGBoost Documentation](https://xgboost.readthedocs.io/)
* [Django Framework](https://www.djangoproject.com/)
* Transfer learning approaches for psychological data interpretation

---
