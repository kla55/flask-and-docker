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

model = joblib.load('/app/model.pkl')

#def predict():
#    data = request.json['features']
#    prediction = model.predict([np.array(data)]).tolist()
#    return jsonify({'prediction': prediction})

#def predict():
#    # Get the features from the request
#    data = request.get_json()
#    print("Received data for prediction:", data)
#    features = np.array(data['features']).reshape(1, -1)
#    print("Features reshaped:", features)
#    # Make the prediction
#    prediction = model.predict(features)
#    print("Prediction:", prediction)
#    # Return the prediction as a JSON response
#    return jsonify({"prediction": int(prediction[0])})
def predict():
    # Get the features from the request
    data = request.get_json()
    app.logger.debug("Received data for prediction: %s", data)  # Log incoming data
    
    features = np.array(data['features']).reshape(1, -1)
    app.logger.debug("Features reshaped: %s", features)  # Log reshaped features

    # Make the prediction
    prediction = model.predict(features)
    app.logger.debug("Prediction: %s", prediction)  # Log the prediction

    # Return the prediction as a JSON response
    app.logger.debug("Returning prediction: %d", prediction[0])  # Log response
    return jsonify({"prediction": int(prediction[0])})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)