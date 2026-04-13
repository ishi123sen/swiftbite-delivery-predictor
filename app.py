from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Train model at startup ────────────────────────────────────────────────────
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

def build_model():
    rng = np.random.default_rng(42)
    n   = 2000
    distance  = rng.uniform(0.5, 20, n)
    prep_time = rng.uniform(5, 40, n)
    traffic   = rng.integers(0, 3, n).astype(float)   # 0=Low 1=Med 2=High
    delivery  = np.clip(
        distance * 3.5 + prep_time * 0.8 + traffic * 7 + rng.normal(0, 2, n),
        10, 120
    )
    X      = np.column_stack([distance, prep_time, traffic])
    scaler = StandardScaler()
    model  = LinearRegression()
    model.fit(scaler.fit_transform(X), delivery)
    return model, scaler

MODEL, SCALER = build_model()
TRAFFIC_MAP   = {"low": 0, "medium": 1, "high": 2}

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    return send_from_directory(os.path.join(BASE_DIR, "templates"), "index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        distance  = float(data["distance"])
        prep_time = float(data["prep_time"])
        traffic   = TRAFFIC_MAP[data["traffic"].lower()]
        X         = SCALER.transform([[distance, prep_time, traffic]])
        pred      = MODEL.predict(X)[0]
        return jsonify({
            "success":    True,
            "prediction": round(pred),
            "range_low":  max(5, round(pred * 0.85)),
            "range_high": round(pred * 1.15),
            "distance":   round(distance, 2),
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
