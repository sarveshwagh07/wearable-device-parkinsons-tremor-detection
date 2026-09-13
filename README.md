# Wearable Parkinsonian Tremor Detection

A wearable sensing and machine learning prototype for detecting tremor patterns using ESP32, MPU6050, signal processing, FFT-based frequency analysis, and Random Forest classification.

> **Note:** This repository is a research/engineering prototype and is not a medical diagnostic system. The included implementation uses synthetic data for demonstration and development purposes.

## Overview

This project explores a wearable approach for capturing motion data using an MPU6050 accelerometer and gyroscope connected to an ESP32. The recorded sensor signals are processed to extract time-domain and frequency-domain characteristics and are then used by a machine learning model to classify tremor-related movement patterns.

The project demonstrates an end-to-end pipeline from wearable sensing to signal processing, feature extraction, machine learning, and tremor prediction.

## Objectives

- Acquire motion data using a wearable inertial sensing system.
- Process accelerometer and gyroscope signals.
- Analyze tremor-related frequency components using FFT.
- Extract time-domain and frequency-domain features.
- Train a machine learning classifier for tremor-pattern detection.
- Generate binary tremor predictions.
- Develop a reproducible Python-based analysis pipeline.

## System Architecture

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

## Technologies Used

- ESP32
- MPU6050
- Python
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib
- FFT
- Random Forest
- Signal Processing
- Machine Learning
- Inertial Sensor Data Analysis

## Methodology

### 1. Wearable Data Acquisition

The ESP32 is interfaced with an MPU6050 inertial sensor to acquire accelerometer and gyroscope motion data.

### 2. Signal Processing

The recorded sensor signals are processed to prepare them for analysis and extract meaningful motion characteristics.

### 3. FFT-Based Frequency Analysis

Fast Fourier Transform (FFT) is applied to analyze the frequency spectrum of the motion signal. Frequency-domain characteristics are used as important features for identifying tremor-related movement patterns.

### 4. Feature Extraction

The pipeline extracts features including:

- RMS
- Standard deviation
- Variance
- Signal energy
- Dominant frequency
- 4–6 Hz band power
- Spectral entropy

### 5. Machine Learning

A Random Forest classifier is used to classify motion patterns into tremor and non-tremor categories based on the extracted sensor features.

### 6. Prediction

The classification pipeline produces a binary prediction:

Tremor Detected → TRUE  
No Tremor → FALSE

## Testing and Evaluation

The project includes scripts for:

- Synthetic sensor-data generation
- Signal processing
- Feature extraction
- Machine learning model training
- Tremor prediction
- Signal visualization

The model can be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Project Structure

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

## How to Run

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/wearable-tremor-detection.git

cd wearable-tremor-detection

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Generate Prototype Data

python src/generate_data.py

### 4. Train the Model

python src/train_model.py

### 5. Run Prediction

python src/predict_tremor.py

### 6. Visualize Sensor Signals

python src/plot_signal.py

## Prototype Dataset

The current GitHub implementation uses synthetically generated inertial sensor data to demonstrate the complete signal-processing and machine-learning pipeline.

The synthetic signals include simulated tremor components in the relevant frequency range.

No patient-identifiable or clinical data is included in this repository.

## Future Improvements

- Integrate real-time ESP32 sensor streaming.
- Add Bluetooth/Wi-Fi based data transmission.
- Implement real-time tremor detection.
- Expand the dataset with more diverse motion patterns.
- Compare Random Forest with SVM, LSTM, and other classifiers.
- Add additional sensor features and signal-processing techniques.
- Develop a wearable visualization dashboard.
- Validate the system using appropriately collected and ethically approved datasets.

## Disclaimer

This project is an engineering and machine-learning prototype intended for research and educational purposes.

It should not be used for medical diagnosis or clinical decision-making. Detection of tremor patterns alone does not establish the presence or absence of Parkinson's disease.

## Author

Sarvesh Wagh

Electronics & Communication Engineering (AIML)
MIT World Peace University, Pune

---

This project demonstrates practical experience in Embedded Systems, Wearable Sensors, Signal Processing, FFT, Machine Learning, and Python-based Data Analysis.
