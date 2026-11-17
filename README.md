# Network Traffic Anomaly Detection Using Machine Learning

## Project Description
This project identifies unusual network traffic patterns using the Isolation Forest machine learning algorithm.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS

## Dataset
A synthetic dataset containing 1000 records:
- 800 Normal traffic records
- 200 Anomalous traffic records

## Features
- Packet Size
- Duration
- Protocol
- Source Bytes
- Destination Bytes

## Algorithm
Isolation Forest (Unsupervised Machine Learning)

## Model Evaluation
Accuracy: 92.2% on the generated dataset.

Note: Evaluation was performed on the same dataset used for training. This is a demonstration result, not a measure of real-world performance.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Generate dataset:
   python generate_dataset.py

3. Train model:
   python train_model.py

4. Run application:
   python app.py

5. Open:
   http://127.0.0.1:5002

## Project Limitation
This prototype uses synthetic data and manually entered traffic values. It does not capture or monitor live network traffic.