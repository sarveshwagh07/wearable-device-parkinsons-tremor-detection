import joblib
import pandas as pd
from signal_processing import bandpass_filter
from feature_extraction import extract_features

FS = 100
bundle = joblib.load("results/tremor_rf_model.pkl")
model = bundle["model"]

data = pd.read_csv("data/synthetic_accelerometer.csv")
sample = data[data["sample_id"] == data["sample_id"].iloc[0]]["accel_x"].to_numpy()

filtered = bandpass_filter(sample, FS)
features = extract_features(filtered, FS)
X = pd.DataFrame([features])[bundle["features"]]

prediction = int(model.predict(X)[0])
probability = float(model.predict_proba(X)[0][1])

print("Prediction:", "TREMOR" if prediction else "NON-TREMOR")
print(f"Tremor probability: {probability:.2%}")
print(f"Dominant frequency: {features['dominant_frequency_hz']:.2f} Hz")
