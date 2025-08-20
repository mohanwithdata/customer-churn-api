# 📊 Customer Churn Prediction API  

![Last Commit](https://img.shields.io/github/last-commit/mohanwithdata/customer-churn-api)  
![Repo Size](https://img.shields.io/github/repo-size/mohanwithdata/customer-churn-api)  
![Languages](https://img.shields.io/github/languages/count/mohanwithdata/customer-churn-api)  
![Top Language](https://img.shields.io/github/languages/top/mohanwithdata/customer-churn-api)  
![Issues](https://img.shields.io/github/issues/mohanwithdata/customer-churn-api)  
![Pull Requests](https://img.shields.io/github/issues-pr/mohanwithdata/customer-churn-api)  
![License](https://img.shields.io/github/license/mohanwithdata/customer-churn-api)  

This repository contains a **Customer Churn Prediction API** built with **FastAPI** and powered by a **machine learning model** trained on customer behavior data. The API helps businesses identify customers at risk of leaving (churning) so that retention strategies can be applied proactively.  

---

## 🚀 Features  
- ✅ RESTful API built with **FastAPI**  
- ✅ Predict customer churn probability in real-time  
- ✅ Pre-trained ML model (Logistic Regression / Random Forest / XGBoost etc.)  
- ✅ Easy to deploy on **Docker, AWS, or GCP**  
- ✅ Interactive API docs with **Swagger UI** (`/docs`)  

---

## 📂 Project Structure  

```
customer-churn-api/
│── app/
│   ├── main.py          # FastAPI entry point  
│   ├── model.py         # ML model loading & prediction logic  
│   ├── schemas.py       # Pydantic models for request/response  
│   ├── utils.py         # Helper functions  
│── model/
│   ├── churn_model.pkl  # Trained machine learning model  
│── requirements.txt     # Python dependencies  
│── Dockerfile           # Docker setup  
│── README.md            # Project documentation  
```

---

## ⚡ Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/mohanwithdata/customer-churn-api.git
cd customer-churn-api
```

### 2️⃣ Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API  

### Local Run  
```bash
uvicorn app.main:app --reload
```

Visit API Docs here 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

### Docker Run  
```bash
docker build -t customer-churn-api .
docker run -d -p 8000:8000 customer-churn-api
```

---

## 📬 Example Request  

### Endpoint: `POST /predict`  

**Request JSON:**  
```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "InternetService": "Fiber optic",
  "Contract": "Month-to-month",
  "MonthlyCharges": 70.35,
  "TotalCharges": 845.5
}
```

**Response JSON:**  
```json
{
  "churn_probability": 0.82,
  "churn_prediction": "Yes"
}
```

---

## 🛠 Tech Stack  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)  
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)  

---

## 📊 Dataset Used  
- [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  

---

## 🌍 Deployment  
You can deploy this API on:  
- **AWS EC2 / SageMaker**  
- **Google Cloud Run**  
- **Heroku**  
- **Docker Hub + Kubernetes**  

---

## 📸 Demo  

### Swagger UI (`/docs`)
![Swagger Demo](https://raw.githubusercontent.com/mohanwithdata/customer-churn-api/main/demo/swagger.png)  

### Example Prediction Request  
![Prediction Demo](https://raw.githubusercontent.com/mohanwithdata/customer-churn-api/main/demo/prediction.png)  

---

## 🤝 Contributing  
Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and create a pull request.  

--- 
