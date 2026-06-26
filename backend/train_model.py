"""
ArogyaAI - Disease Prediction Model Trainer
============================================
Uses symptom data to train a Random Forest classifier.
Saves the model + encoder for direct use in your backend.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json
import os

# ─────────────────────────────────────────────
# STEP 1: Load Dataset
# ─────────────────────────────────────────────
# Replace 'dataset.csv' with your actual CSV file path
df = pd.read_csv("dataset.csv")

print("[OK] Dataset loaded:", df.shape)
print(df.head())

# ─────────────────────────────────────────────
# STEP 2: Extract All Unique Symptoms
# ─────────────────────────────────────────────
all_symptoms = set()
for entry in df["Symptoms"].dropna():
    for symptom in entry.split(","):
        all_symptoms.add(symptom.strip().lower())

all_symptoms = sorted(list(all_symptoms))
print(f"\n[OK] Total unique symptoms found: {len(all_symptoms)}")
print("Symptoms:", all_symptoms)

# ─────────────────────────────────────────────
# STEP 3: Convert Symptoms to Binary Feature Vectors
# ─────────────────────────────────────────────
def encode_symptoms(symptom_str, all_symptoms):
    present = [s.strip().lower() for s in str(symptom_str).split(",")]
    return [1 if s in present else 0 for s in all_symptoms]

X = df["Symptoms"].apply(lambda x: encode_symptoms(x, all_symptoms))
X = pd.DataFrame(X.tolist(), columns=all_symptoms)

# ─────────────────────────────────────────────
# STEP 4: Encode Target Labels (Disease names)
# ─────────────────────────────────────────────
le = LabelEncoder()
y = le.fit_transform(df["Disease"])

print(f"\n[OK] Classes (diseases): {list(le.classes_)}")

# ─────────────────────────────────────────────
# STEP 5: Train/Test Split
# ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n[OK] Train size: {len(X_train)} | Test size: {len(X_test)}")

# ─────────────────────────────────────────────
# STEP 6: Train Random Forest Model
# ─────────────────────────────────────────────
model = RandomForestClassifier(
    n_estimators=200,       # 200 trees for better accuracy
    max_depth=10,
    min_samples_split=2,
    random_state=42,
    n_jobs=-1               # use all CPU cores
)

model.fit(X_train, y_train)
print("\n[OK] Model training complete!")

# ─────────────────────────────────────────────
# STEP 7: Evaluate
# ─────────────────────────────────────────────
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n[Stats] Test Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, labels=np.unique(y_test), target_names=le.classes_[np.unique(y_test)]))

# ─────────────────────────────────────────────
# STEP 8: Save Model + Encoder + Symptom List
# ─────────────────────────────────────────────
os.makedirs("arogya_model", exist_ok=True)

joblib.dump(model, "arogya_model/disease_model.pkl")
joblib.dump(le, "arogya_model/label_encoder.pkl")

# Save symptoms list as JSON (needed for frontend/API)
with open("arogya_model/symptoms_list.json", "w") as f:
    json.dump(all_symptoms, f, indent=2)

# Save disease list as JSON
with open("arogya_model/diseases_list.json", "w") as f:
    json.dump(list(le.classes_), f, indent=2)

print("\n[OK] Saved to arogya_model/")
print("   |-- disease_model.pkl   -> main model")
print("   |-- label_encoder.pkl   -> disease name encoder")
print("   |-- symptoms_list.json  -> all symptom features")
print("   +-- diseases_list.json  -> all disease labels")