from flask import Flask, request, jsonify
import joblib
import numpy as np


app = Flask(__name__)

#@app.route("/")  # ✅ Ensure this route exists
#def home():
#    return "Hello, Flask in Docker!"


# Configure Flask logging
#logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def health_check():
    return "Model is running!"

print("Loading model...")
model = joblib.load('/app/model.pkl')
print("Model loaded successfully")

print(app.url_map)
@app.route('/predict', methods=['POST'])
def predict():
    # Get the features from the request
    data = request.get_json()
    app.logger.debug("Received data for prediction: %s", data)  

    features = np.array(data['features']).reshape(1, -1)
    app.logger.debug("Features reshaped: %s", features) 

    # Make the prediction
    prediction = model.predict(features)
    app.logger.debug("Prediction: %s", prediction)  

    # Return the prediction as a JSON response
    app.logger.debug("Returning prediction: %d", prediction[0]) 
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)