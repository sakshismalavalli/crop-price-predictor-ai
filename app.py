from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model, le = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        crop = data["crop"].lower().strip()

        crop_encoded = le.transform([crop])[0]
        prediction = model.predict([[crop_encoded]])

        return jsonify({"price": float(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)