import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("dataset/network_traffic.csv")

# Select input features
X = data.drop("label", axis=1)
y = data["label"]

# Create Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.20,
    random_state=42
)

# Train model without using labels
model.fit(X)

# Predict anomalies
# Isolation Forest: 1 = normal, -1 = anomaly
predictions = model.predict(X)

# Convert predictions to our label format
predictions = [0 if p == 1 else 1 for p in predictions]

# Evaluate on this demonstration dataset
print("MODEL EVALUATION")
print("----------------")
print("Accuracy:", accuracy_score(y, predictions))
print("\nClassification Report:")
print(classification_report(
    y, predictions,
    target_names=["Normal", "Anomaly"]
))

# Save trained model
with open("output/anomaly_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")