import joblib
import numpy as np
from django.shortcuts import render
from .forms import StressForm  # Ensure you have a form class for validation

# Load the trained model and scaler once at startup
model = joblib.load(r"C:\Users\shaik\Downloads\Social_Media_Addiction_Predictor\Social_Media_Addiction_Predictor_app\stress_model.pkl")
scaler = joblib.load(r"C:\Users\shaik\Downloads\Social_Media_Addiction_Predictor\Social_Media_Addiction_Predictor_app\scaler.pkl")

def home(request):
    return render(request,"Homepage.html");

def predict_stress(request):
    print("hello")
    if request.method == "POST":
        form = StressForm(request.POST)
        if form.is_valid():
            # Extract cleaned input data from the form
            user_input = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['gender'],
                form.cleaned_data['social_media_usage'],
                form.cleaned_data['dominant_platform'],
                form.cleaned_data['check_freq'],
                form.cleaned_data['pre_sleep_usage'],
                form.cleaned_data['content_type'],
                form.cleaned_data['sleep_latency'],
                form.cleaned_data['total_sleep'],
                form.cleaned_data['sleep_efficiency'],
                form.cleaned_data['sleep_quality'],
                form.cleaned_data['waso'],
                form.cleaned_data['num_awakenings'],
                form.cleaned_data['melatonin'],
                form.cleaned_data['cortisol'],
                form.cleaned_data['blue_light_exposure'],
                form.cleaned_data['stress_level'],
                form.cleaned_data['anxiety_depression'],
                form.cleaned_data['restlessness'],
                form.cleaned_data['interest_fluctuation'],
                form.cleaned_data['relationship_status'],
                form.cleaned_data['loneliness'],
            ]])

            # Normalize input before prediction
            user_input_scaled = scaler.transform(user_input)

            # Predict stress level
            prediction = model.predict(user_input_scaled)[0] + 1  # Convert back to 1-5 scale

            return render(request, "HomePage.html", {"prediction": prediction})

    else:
        form = StressForm()

    return render(request, "HomePage.html", {"form": form})
