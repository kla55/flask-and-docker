from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")  # ✅ Ensure this route exists
def home():
    return "Hello, Flask in Docker!"


model = joblib.load('/app/model.pkl')

def predict():
    data = request.json['features']
    prediction = model.predict([np.array(data)]).tolist()
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)