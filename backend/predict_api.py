"""
ArogyaAI - Disease Prediction API
===================================
Run this Flask server to expose the trained model as a REST API.
Your React frontend calls this to get disease predictions.

Install:  pip install flask flask-cors joblib scikit-learn
Run:      python predict_api.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import json
import numpy as np

app = Flask(__name__)
CORS(app)  # allows your React frontend to call this API

# ── Load model artifacts ──────────────────────────────────────────
model    = joblib.load("arogya_model/disease_model.pkl")
le       = joblib.load("arogya_model/label_encoder.pkl")

with open("arogya_model/symptoms_list.json") as f:
    all_symptoms = json.load(f)

with open("arogya_model/diseases_list.json") as f:
    diseases_list = json.load(f)

print("✅ Model loaded. API ready.")

# ── Routes ────────────────────────────────────────────────────────

@app.route("/symptoms", methods=["GET"])
def get_symptoms():
    """Returns the full list of symptoms the model understands."""
    return jsonify({"symptoms": all_symptoms})


@app.route("/predict", methods=["POST"])
def predict():
    """
    Accepts a list of symptoms and returns top disease predictions.

    Request body (JSON):
    {
        "symptoms": ["fever", "cough", "headache"]
    }

    Response:
    {
        "predictions": [
            {"disease": "Influenza", "confidence": 0.87},
            {"disease": "COVID-19",  "confidence": 0.08},
            ...
        ]
    }
    """
    data = request.get_json()

    if not data or "symptoms" not in data:
        return jsonify({"error": "Please send symptoms in request body"}), 400

    input_symptoms = [s.strip().lower() for s in data["symptoms"]]

    # Encode into binary feature vector
    feature_vector = [1 if s in input_symptoms else 0 for s in all_symptoms]
    feature_array  = np.array(feature_vector).reshape(1, -1)

    # Get probabilities for all diseases
    probabilities  = model.predict_proba(feature_array)[0]

    # Build top-5 predictions sorted by confidence
    results = sorted(
        [
            {"disease": le.classes_[i], "confidence": round(float(p), 4)}
            for i, p in enumerate(probabilities)
        ],
        key=lambda x: x["confidence"],
        reverse=True
    )[:5]

    return jsonify({
        "input_symptoms": input_symptoms,
        "predictions": results
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model": "RandomForest", "diseases": len(diseases_list)})


# ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)