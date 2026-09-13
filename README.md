# Wearable Tremor Detection — Prototype

A prototype pipeline for detecting tremor-like movement patterns from wearable accelerometer signals using signal processing, FFT-based frequency analysis, feature extraction, and machine learning.

> **Project status:** Prototype. The included dataset is synthetically generated for demonstration and development. It is not a medical diagnostic system and is not trained on clinical patient data.

## Pipeline

Accelerometer Signal → Preprocessing → FFT / Frequency Analysis → Feature Extraction → Random Forest → Tremor / Non-Tremor

## Technologies

- Python
- NumPy, Pandas, SciPy
- Matplotlib
- Scikit-learn
- FFT / frequency-domain signal analysis
- Random Forest

## Features

The prototype extracts time- and frequency-domain features including RMS, standard deviation, signal energy, dominant frequency, 4–6 Hz band power, and spectral entropy.

## Run

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/train_model.py
python src/predict_tremor.py
```

The scripts save demonstration plots and model outputs in `results/`.

## Important note

This repository is an engineering/research prototype for signal-processing and machine-learning experimentation. It does not diagnose Parkinson's disease or provide medical advice.
