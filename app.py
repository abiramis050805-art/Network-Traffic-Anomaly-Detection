from flask import Flask, request, render_template_string
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("output/anomaly_model.pkl", "rb") as file:
    model = pickle.load(file)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Network Traffic Anomaly Detection</title>
    <style>
        body {
            font-family: Arial;
            background: #101827;
            color: white;
            text-align: center;
            padding: 40px;
        }
        .container {
            background: #1e293b;
            padding: 25px;
            max-width: 450px;
            margin: auto;
            border-radius: 12px;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 8px;
        }
        button {
            padding: 12px 25px;
            background: #16a34a;
            color: white;
            border: none;
            cursor: pointer;
        }
        h2 { color: #38bdf8; }
    </style>
</head>
<body>
<div class="container">
    <h2>Network Traffic Anomaly Detection</h2>
    <p>Enter sample network traffic details</p>

    <form method="POST">
        <input type="number" name="packet_size"
        placeholder="Packet Size" required min="1">

        <input type="number" step="any" name="duration"
        placeholder="Duration" required min="0.001">

        <input type="number" name="protocol"
        placeholder="Protocol (6=TCP, 17=UDP, 1=ICMP)"
        required>

        <input type="number" name="source_bytes"
        placeholder="Source Bytes" required min="0">

        <input type="number" name="destination_bytes"
        placeholder="Destination Bytes" required min="0">

        <button type="submit">Detect Anomaly</button>
    </form>

    {% if result %}
        <h2>{{ result }}</h2>
        <p>{{ message }}</p>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = None

    if request.method == "POST":
        try:
            traffic = pd.DataFrame([{
                "packet_size": int(request.form["packet_size"]),
                "duration": float(request.form["duration"]),
                "protocol": int(request.form["protocol"]),
                "source_bytes": int(request.form["source_bytes"]),
                "destination_bytes": int(request.form["destination_bytes"])
            }])

            prediction = model.predict(traffic)[0]

            if prediction == -1:
                result = "ANOMALOUS TRAFFIC"
                message = "The model identified an unusual traffic pattern."
            else:
                result = "NORMAL TRAFFIC"
                message = "The model identified a normal traffic pattern."

        except (ValueError, TypeError):
            result = "INVALID INPUT"
            message = "Please enter valid numeric values."

    return render_template_string(
        HTML, result=result, message=message
    )

if __name__ == "__main__":
    app.run(debug=True, port=5002)