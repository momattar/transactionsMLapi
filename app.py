from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("fraud_model.pkl")  # pipeline includes preprocessing

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])  # expects exact feature names

    prediction = model.predict(df)[0]

    return jsonify({
        "prediction": int(prediction),
        "message": "This transaction can be fraud" if prediction == 1 else "This transaction looks like it is not a fraud"
    })

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.json

#         # Extract 'type' and one-hot encode it manually
#         type_value = data.pop('type')
#         transaction_types = ['CASH_OUT', 'PAYMENT', 'TRANSFER', 'DEBIT']
#         for t in transaction_types:
#             data[f'type_{t}'] = 1 if t == type_value else 0

#         df = pd.DataFrame([data])

#         prediction = model.predict(df)[0]
#         return jsonify({
#             "prediction": int(prediction),
#             "message": "This transaction can be fraud" if prediction == 1 else "This transaction looks like it is not a fraud"
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

