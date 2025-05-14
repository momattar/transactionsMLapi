# 🔄 Transactions Fraud Detection API

A Flask-based API that predicts fraudulent online payment transactions using a machine learning model trained on real transaction data.

---

## 🌐 Live Demo

🚀 Hosted API:  
**https://transactionsmlapi-production.up.railway.app/predict**

Send a POST request with transaction data to get a fraud prediction (0 = Not Fraud, 1 = Fraud).

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
