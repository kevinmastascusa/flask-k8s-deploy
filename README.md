# 🐳 Flask ML API + Kubernetes Deployment

This project demonstrates how to containerize a simple Flask-based machine learning API, deploy it to a Kubernetes cluster with Minikube, and serve predictions through a `/predict` endpoint.

## 🚀 Features
- Flask API for serving ML model predictions
- Docker containerization
- Kubernetes deployment via Minikube
- RESTful `/predict` endpoint
- Local testable setup with curl/Postman
- SSH-authenticated GitHub repository

## 📁 Project Structure

```
.
├── app.py                # Flask API app
├── model.pkl             # Serialized ML model (generated)
├── generate_model.py     # Script to create model.pkl
├── requirements.txt      # Python dependencies
├── Dockerfile            # Image definition
├── deployment.yaml       # Kubernetes deployment config
├── service.yaml          # Kubernetes service config
└── .gitignore
```

---

## 🧰 Prerequisites

- Python 3.9+
- Docker Desktop
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- GitHub SSH key setup (for pushing)

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone git@github.com:kevinmastascusa/flask-k8s-deploy.git
cd flask-k8s-deploy
```

### 2. Generate the model file
```bash
pip install -r requirements.txt
python generate_model.py
```

### 3. Build and push Docker image
```bash
docker build -t kzmastascusa/flask-model-api:latest .
docker push kzmastascusa/flask-model-api:latest
```

### 4. Start Minikube and deploy
```bash
minikube start
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 5. Access the service
```bash
minikube service flask-api-service
```

You’ll get a URL like `http://127.0.0.1:64893`

---

## 📡 Test the API

### POST /predict

**Request**
```bash
curl -X POST http://127.0.0.1:64893/predict   -H "Content-Type: application/json"   -d '{"features": [1, 2]}'
```

**Response**
```json
{
  "prediction": 0
}
```

---

## 🧠 Author

**Kevin Mastascusa**  
🧑‍💻 GitHub: [@kevinmastascusa](https://github.com/kevinmastascusa)

---

## 📄 License

MIT License – free to use, share, or build on.
