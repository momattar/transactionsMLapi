# 🔄 Transactions Fraud Detection API

A Flask-based API that predicts fraudulent online payment transactions using a machine learning model trained on real transaction data.

---

## 🌐 Hosted API



---

## 📌 Overview

This API accepts JSON-formatted transaction details and returns a fraud prediction based on a trained ML model.  
It is intended to be used by external applications (e.g., an ASP.NET MVC).

---

## 🧠 Machine Learning Model

- **Algorithm:** *(e.g., Random Forest / XGBoost)*
- **Training Notebook:** [`Online-Payment-Fraud-Detection.ipynb`](./Online-Payment-Fraud-Detection.ipynb)
- **Model Input:** Cleaned and one-hot encoded transaction data
- **Output:**  
  - `0` → Legitimate transaction  
  - `1` → Fraudulent transaction

---

## 🔧 API Usage

### `POST /predict`

**URL:**  
`https://transactionsmlapi-production.up.railway.app/predict`

**Request Headers:**
```http
Content-Type: application/json
```
### 📥 Request Format

Send a JSON object with the following structure (sample):

```json
{
  "type": "CASH_OUT",
  "amount": 9800,
  "oldbalanceOrg": 9800,
  "newbalanceOrig": 0,
  "oldbalanceDest": 0,
  "newbalanceDest": 0
}
```

### 📥 Response Format
```json
{
  "prediction": "Fraud"  // or "Not Fraud"
}
```

