from pathlib import Path
import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split

from signal_processing import bandpass_filter
from feature_extraction import extract_features

FS = 100
data = pd.read_csv("data/synthetic_accelerometer.csv")

features = []
labels = []
for sample_id, group in data.groupby("sample_id"):
    signal = group["accel_x"].to_numpy()
    label = int(group["label"].iloc[0])
    filtered = bandpass_filter(signal, FS)
    features.append(extract_features(filtered, FS))
    labels.append(label)

X = pd.DataFrame(features)
y = pd.Series(labels, name="label")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=150, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred, target_names=["Non-Tremor", "Tremor"]))

Path("results").mkdir(exist_ok=True)
ConfusionMatrixDisplay.from_predictions(
    y_test, pred, display_labels=["Non-Tremor", "Tremor"]
)
plt.title("Tremor Detection - Confusion Matrix")
plt.tight_layout()
plt.savefig("results/confusion_matrix.png", dpi=160)
plt.close()

joblib.dump({"model": model, "features": list(X.columns)}, "results/tremor_rf_model.pkl")
print("Saved model to results/tremor_rf_model.pkl")
