import os
import json
import joblib
import numpy as np
import pandas as pd

from django.shortcuts import render
from django.db.models import Q
from .models import DiseasePrediction
from hospitals.models import Doctor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "backend",
    "arogya_model",
    "disease_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "backend",
    "arogya_model",
    "label_encoder.pkl"
)

SYMPTOMS_PATH = os.path.join(
    BASE_DIR,
    "backend",
    "arogya_model",
    "symptoms_list.json"
)

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

with open(SYMPTOMS_PATH) as f:
    all_symptoms = json.load(f)

DISEASE_SPECIALIZATION_MAP = {
    'Allergy': ['ENT', 'General Medicine'],
    'Anemia': ['General Medicine'],
    'Anxiety': ['General Medicine', 'Neurology'],
    'Arthritis': ['Orthopedics'],
    'Asthma': ['General Medicine'],
    'Bronchitis': ['General Medicine'],
    'COVID-19': ['General Medicine', 'ENT'],
    'Chronic Kidney Disease': ['General Medicine'],
    'Common Cold': ['General Medicine', 'ENT'],
    'Dementia': ['Neurology'],
    'Depression': ['General Medicine', 'Neurology'],
    'Dermatitis': ['Dermatology'],
    'Diabetes': ['General Medicine'],
    'Epilepsy': ['Neurology'],
    'Food Poisoning': ['General Medicine', 'General Surgery'],
    'Gastritis': ['General Medicine'],
    'Heart Disease': ['Cardiology'],
    'Hypertension': ['Cardiology', 'General Medicine'],
    'IBS': ['General Medicine'],
    'Influenza': ['General Medicine'],
    'Liver Disease': ['General Medicine'],
    'Migraine': ['Neurology', 'General Medicine'],
    'Obesity': ['General Medicine', 'Orthopedics'],
    "Parkinson's": ['Neurology'],
    'Pneumonia': ['General Medicine'],
    'Sinusitis': ['ENT'],
    'Stroke': ['Neurology'],
    'Thyroid Disorder': ['General Medicine'],
    'Tuberculosis': ['General Medicine'],
    'Ulcer': ['General Medicine', 'General Surgery']
}


def disease_predict(request):
    prediction = None
    recommended_doctors = None

    if request.method == "POST":
        selected_symptoms = request.POST.getlist("symptoms")

        feature_vector = [
            1 if symptom in selected_symptoms else 0
            for symptom in all_symptoms
        ]

        feature_df = pd.DataFrame([feature_vector], columns=all_symptoms)
        prediction_encoded = model.predict(feature_df)

        prediction = encoder.inverse_transform(
            prediction_encoded
        )[0]

        # Get recommended doctors based on predicted disease
        specs = DISEASE_SPECIALIZATION_MAP.get(prediction, ['General Medicine'])
        query = Q()
        for spec in specs:
            query |= Q(specialization__icontains=spec)

        recommended_doctors = Doctor.objects.filter(query).select_related('hospital')[:3]
        if not recommended_doctors.exists():
            recommended_doctors = Doctor.objects.filter(
                Q(specialization__icontains='General Medicine') | Q(specialization__icontains='General Surgery')
            ).select_related('hospital')[:3]
        if not recommended_doctors.exists():
            recommended_doctors = Doctor.objects.all().select_related('hospital')[:3]

        # SAVE TO DATABASE
        if request.user.is_authenticated:
            DiseasePrediction.objects.create(
                user=request.user,
                symptoms=", ".join([s.replace("_", " ").title() for s in selected_symptoms]),
                predicted_disease=prediction
            )

    symptoms_formatted = [
        {"value": sym, "label": sym.replace("_", " ").title()}
        for sym in all_symptoms
    ]

    return render(
        request,
        "disease_tracker/predict.html",
        {
            "symptoms": symptoms_formatted,
            "prediction": prediction,
            "recommended_doctors": recommended_doctors
        }
    )