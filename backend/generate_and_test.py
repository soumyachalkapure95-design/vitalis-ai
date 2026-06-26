import random
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

diseases = ['Allergy', 'Anemia', 'Anxiety', 'Arthritis', 'Asthma', 'Bronchitis', 'COVID-19', 
            'Chronic Kidney Disease', 'Common Cold', 'Dementia', 'Depression', 'Dermatitis', 
            'Diabetes', 'Epilepsy', 'Food Poisoning', 'Gastritis', 'Heart Disease', 'Hypertension', 
            'IBS', 'Influenza', 'Liver Disease', 'Migraine', 'Obesity', "Parkinson's", 'Pneumonia', 
            'Sinusitis', 'Stroke', 'Thyroid Disorder', 'Tuberculosis', 'Ulcer']

symptoms = ['abdominal pain', 'anxiety', 'appetite loss', 'back pain', 'blurred vision', 
            'chest pain', 'cough', 'depression', 'diarrhea', 'dizziness', 'fatigue', 'fever', 
            'headache', 'insomnia', 'joint pain', 'muscle pain', 'nausea', 'rash', 'runny nose', 
            'shortness of breath', 'sneezing', 'sore throat', 'sweating', 'swelling', 'tremors', 
            'vomiting', 'weight gain', 'weight loss']

disease_symptoms = {
    'Allergy': ['runny nose', 'sneezing', 'sore throat', 'rash', 'cough'],
    'Anemia': ['fatigue', 'dizziness', 'shortness of breath', 'appetite loss', 'headache'],
    'Anxiety': ['anxiety', 'tremors', 'sweating', 'insomnia', 'dizziness'],
    'Arthritis': ['joint pain', 'muscle pain', 'swelling', 'fatigue', 'back pain'],
    'Asthma': ['shortness of breath', 'chest pain', 'cough', 'anxiety', 'fatigue'],
    'Bronchitis': ['cough', 'sore throat', 'fever', 'shortness of breath', 'chest pain'],
    'COVID-19': ['fever', 'cough', 'fatigue', 'shortness of breath', 'sore throat'],
    'Chronic Kidney Disease': ['swelling', 'fatigue', 'nausea', 'vomiting', 'appetite loss'],
    'Common Cold': ['runny nose', 'sneezing', 'sore throat', 'cough', 'headache'],
    'Dementia': ['depression', 'anxiety', 'insomnia', 'dizziness', 'tremors'],
    'Depression': ['depression', 'fatigue', 'insomnia', 'appetite loss', 'weight loss'],
    'Dermatitis': ['rash', 'swelling', 'sweating', 'abdominal pain', 'nausea'],
    'Diabetes': ['weight loss', 'fatigue', 'blurred vision', 'dizziness', 'appetite loss'],
    'Epilepsy': ['tremors', 'dizziness', 'anxiety', 'headache', 'sweating'],
    'Food Poisoning': ['vomiting', 'diarrhea', 'abdominal pain', 'nausea', 'fever'],
    'Gastritis': ['abdominal pain', 'nausea', 'vomiting', 'appetite loss', 'fatigue'],
    'Heart Disease': ['chest pain', 'shortness of breath', 'dizziness', 'sweating', 'fatigue'],
    'Hypertension': ['headache', 'dizziness', 'blurred vision', 'anxiety', 'chest pain'],
    'IBS': ['abdominal pain', 'diarrhea', 'nausea', 'appetite loss', 'weight loss'],
    'Influenza': ['fever', 'cough', 'muscle pain', 'sore throat', 'fatigue'],
    'Liver Disease': ['abdominal pain', 'nausea', 'vomiting', 'appetite loss', 'fatigue'],
    'Migraine': ['headache', 'nausea', 'vomiting', 'blurred vision', 'dizziness'],
    'Obesity': ['weight gain', 'fatigue', 'shortness of breath', 'joint pain', 'back pain'],
    'Parkinson\'s': ['tremors', 'muscle pain', 'dizziness', 'fatigue', 'anxiety'],
    'Pneumonia': ['cough', 'fever', 'shortness of breath', 'chest pain', 'sweating'],
    'Sinusitis': ['headache', 'runny nose', 'sore throat', 'cough', 'fever'],
    'Stroke': ['blurred vision', 'dizziness', 'headache', 'anxiety', 'tremors'],
    'Thyroid Disorder': ['weight gain', 'fatigue', 'insomnia', 'sweating', 'tremors'],
    'Tuberculosis': ['cough', 'sweating', 'weight loss', 'fever', 'chest pain'],
    'Ulcer': ['abdominal pain', 'nausea', 'vomiting', 'appetite loss', 'chest pain']
}

random.seed(42)
np.random.seed(42)

records = []
for i in range(25000):
    disease = random.choice(diseases)
    primary_syms = disease_symptoms[disease]
    # Pick a random subset of primary symptoms (at least 3)
    k = random.randint(3, len(primary_syms))
    selected_syms = list(random.sample(primary_syms, k))
    # Add 0-2 random filler symptoms
    num_filler = random.randint(0, 2)
    other_symptoms = [s for s in symptoms if s not in primary_syms]
    filler = list(random.sample(other_symptoms, num_filler))
    
    all_selected = selected_syms + filler
    random.shuffle(all_selected)
    
    age = random.randint(1, 90)
    gender = random.choice(['Male', 'Female', 'Other'])
    symptom_str = ", ".join(all_selected)
    symptom_count = len(all_selected)
    
    records.append({
        'Patient_ID': i + 1,
        'Age': age,
        'Gender': gender,
        'Symptoms': symptom_str,
        'Symptom_Count': symptom_count,
        'Disease': disease
    })

df = pd.DataFrame(records)
print("Generated shape:", df.shape)
df.to_csv("dataset.csv", index=False)
print("Saved new logical dataset to dataset.csv")

# Train and check model accuracy
all_symptoms_sorted = sorted(symptoms)

def encode_symptoms(symptom_str):
    present = [s.strip().lower() for s in str(symptom_str).split(',')]
    return [1 if s in present else 0 for s in all_symptoms_sorted]

X = pd.DataFrame(df['Symptoms'].apply(encode_symptoms).tolist(), columns=all_symptoms_sorted)
le = LabelEncoder()
y = le.fit_transform(df['Disease'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)
print("Train accuracy:", model.score(X_train, y_train))
print("Test accuracy:", model.score(X_test, y_test))
