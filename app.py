from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"msg": "Python Flask rodando em produção com Gunicorn no EasyPanel!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    values = data.get("values", [])
    arr = np.array(values, dtype=float)
    return jsonify({
        "sum": float(arr.sum()),
        "mean": float(arr.mean())
    })
