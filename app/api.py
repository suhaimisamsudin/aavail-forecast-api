# test endpoint - 26.03.2026 Suhaimi
# not fully working. need to debug further

from flask import Flask, request, jsonify
from model.train import train_model
from model.predict import predict_revenue
import logging
import os

app = Flask(__name__)
logging.basicConfig(filename='logs/api.log', level=logging.INFO)

@app.route('/train', methods=['POST'])
def train():
    try:
        train_model()
        return jsonify({"status": "success", "message": "Model trained successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/predict', methods=['GET'])
def predict():
    country = request.args.get('country')
    date = request.args.get('date')
    try:
        forecast = predict_revenue(country, date)
        logging.info(f"Prediction for {country} on {date}: {forecast}")
        return jsonify({"country": country, "date": date, "forecast": forecast})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/logfile', methods=['GET'])
def logfile():
    if os.path.exists('logs/api.log'):
        with open('logs/api.log', 'r') as f:
            logs = f.read()
        return jsonify({"logs": logs})
    else:
        return jsonify({"logs": "No logs found"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


