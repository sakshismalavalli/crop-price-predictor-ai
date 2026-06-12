from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model, le = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    crop = data["crop"].lower().strip()

    try:
        crop_encoded = le.transform([crop])[0]

        prediction = model.predict([[crop_encoded]])

        return jsonify({
            "price": round(float(prediction[0]))
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)