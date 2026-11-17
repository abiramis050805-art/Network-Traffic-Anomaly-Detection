import pandas as pd
import numpy as np

np.random.seed(42)

# Generate normal network traffic
normal = pd.DataFrame({
    "packet_size": np.random.randint(100, 1500, 800),
    "duration": np.random.uniform(0.1, 5, 800),
    "protocol": np.random.choice([6, 17], 800),
    "source_bytes": np.random.randint(100, 5000, 800),
    "destination_bytes": np.random.randint(100, 5000, 800),
    "label": 0
})

# Generate unusual network traffic
anomaly = pd.DataFrame({
    "packet_size": np.random.randint(3000, 10000, 200),
    "duration": np.random.uniform(0.001, 0.05, 200),
    "protocol": np.random.choice([1, 6, 17], 200),
    "source_bytes": np.random.randint(10000, 50000, 200),
    "destination_bytes": np.random.randint(100, 1000, 200),
    "label": 1
})

# Combine and shuffle data
data = pd.concat([normal, anomaly])
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Save dataset
data.to_csv("dataset/network_traffic.csv", index=False)

print("Dataset generated successfully!")
print(data.head())
print("\nDataset shape:", data.shape)
print("\nTraffic distribution:")
print(data["label"].value_counts())