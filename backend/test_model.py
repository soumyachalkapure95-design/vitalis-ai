import joblib

model = joblib.load("arogya_model/disease_model.pkl")

sample = [[1,0,1,0,0,1]]

prediction = model.predict(sample)

print(prediction)