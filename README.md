# Wearable Parkinsonian Tremor Detection

A wearable sensing and machine learning prototype for detecting tremor patterns using an ESP32, MPU6050 inertial sensor, signal processing, FFT-based frequency analysis, and Random Forest classification.

> **Note:** This repository is a research/engineering prototype and is not a medical diagnostic system. The included implementation uses synthetic data for demonstration and development purposes.

## 📌 Overview

Parkinsonian tremor is commonly characterized by rhythmic involuntary movement, which can be analyzed using inertial sensors and signal-processing techniques.

This project explores a wearable approach for capturing motion data using an **MPU6050 accelerometer and gyroscope connected to an ESP32**. The recorded sensor signals are processed to extract time-domain and frequency-domain characteristics and are then used by a machine learning model to classify tremor-related movement patterns.

The project demonstrates an end-to-end pipeline from **wearable sensing → signal processing → feature extraction → machine learning → tremor prediction**.

## 🎯 Objectives

- Acquire motion data using a wearable inertial sensing system.
- Process accelerometer and gyroscope signals.
- Analyze tremor-related frequency components using FFT.
- Extract relevant time-domain and frequency-domain features.
- Train a machine learning classifier for tremor-pattern detection.
- Generate binary tremor predictions.
- Develop a reproducible Python-based analysis pipeline.

## 🏗️ System Architecture

MPU6050
      ↓
Accelerometer + Gyroscope
      ↓
ESP32
      ↓
Motion Data
      ↓
Signal Preprocessing
      ↓
FFT / Frequency Analysis
      ↓
Feature Extraction
      ↓
Random Forest Classifier
      ↓
Tremor / Non-Tremor Prediction

## 🛠️ Technologies Used

- **ESP32**
- **MPU6050**
- **Python**
- **NumPy**
- **Pandas**
- **SciPy**
- **Scikit-learn**
- **Matplotlib**
- **FFT**
- **Random Forest**
- **Signal Processing**
- **Machine Learning**
- **Inertial Sensor Data Analysis**

## 🔧 Methodology

### 1. Wearable Data Acquisition

The ESP32 is interfaced with an MPU6050 inertial measurement unit to acquire:

- Accelerometer data
- Gyroscope data

The sensor data represents the motion of the wrist/hand during recorded movement sessions.

### 2. Signal Processing

The recorded sensor signals are processed to reduce noise and prepare the data for analysis.

The project uses frequency-domain analysis to identify periodic components within the motion signal.

### 3. FFT-Based Frequency Analysis

Fast Fourier Transform (FFT) is applied to the sensor signal to analyze its frequency spectrum.

Frequency-domain characteristics are used as important features for identifying tremor-related movement patterns.

### 4. Feature Extraction

The pipeline extracts features such as:

- RMS
- Standard deviation
- Variance
- Signal energy
- Dominant frequency
- 4–6 Hz band power
- Spectral entropy

These features provide both time-domain and frequency-domain information about the recorded motion.

### 5. Machine Learning

A **Random Forest classifier** is used to classify motion patterns into tremor and non-tremor categories.

The model uses the extracted sensor features as input.

### 6. Prediction

The final classification pipeline produces a binary prediction:

```text
Tremor Detected → TRUE
No Tremor      → FALSE

Raw Sensor Data
      ↓
Data Cleaning
      ↓
Signal Processing
      ↓
Windowing
      ↓
FFT Analysis
      ↓
Feature Extraction
      ↓
Feature Dataset
      ↓
Random Forest
      ↓
Prediction
wearable-tremor-detection/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
└── src/
    ├── generate_data.py
    ├── signal_processing.py
    ├── feature_extraction.py
    ├── train_model.py
    ├── predict_tremor.py
    └── plot_signal.py
