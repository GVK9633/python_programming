from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model and label encoder
with open('credit_risk_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Assuming manual mapping was used:
risk_mapping_reverse = {0: 'Low', 1: 'Medium', 2: 'High'}

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Create feature array
    features = np.array([[
        data['age'],
        data['income'],
        data['debt'],
        data['employment_length'],
        data['credit_history_length'],
        data['num_credit_cards'],
        data['missed_payments']
    ]])
    
    # Predict
    prediction = model.predict(features)
    predicted_risk = int(prediction[0])  # Ensure it's serializable
    
    return jsonify({
        'risk_level': risk_mapping_reverse[predicted_risk],
        'encoded_risk_level': predicted_risk
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
