from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model, le = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Crop Price Predictor API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    crop = data["crop"].lower().strip()

    crop_encoded = le.transform([crop])[0]
    prediction = model.predict([[crop_encoded]])

    return jsonify({
        "price": round(float(prediction[0]))
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)