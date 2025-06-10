# 🦠 COVID-19 X-ray Classification Web App 🔬

> An AI-powered web application to predict COVID-19 status from chest X-ray images using a trained MobileNetV2 model, powered by FastAPI and deployed on AWS EC2.

---

## 📂 Dataset


📈 **Dataset Source:**  
[Kaggle - COVID-19 X-ray Image Dataset (Large Sample)](https://www.kaggle.com/datasets/mr3suvhro/covid-19-xray-image-dataset-with-huge-samples)

- Over **2000+ X-ray images**
- Pre-labeled into categories: `COVID-19`, `Covid Negative`, and `Covid Positive`
- Ideal for deep learning-based binary or multiclass classification

---

## 🚀 Features

✅ Predicts COVID-19 status from uploaded chest X-ray images  
✅ Built with **FastAPI** for high-performance REST APIs  
✅ Trained on **MobileNetV2** for real-time inference  
✅ Fully containerized with **Docker**  
✅ Deployable on **AWS EC2** with public access

---

## 🛠️ Tech Stack

| Layer       | Technology                   |
|-------------|------------------------------|
| Backend     | Python, FastAPI, TensorFlow  |
| Frontend    | HTML/CSS + Jinja Templates   |
| Model       | MobileNetV2 (.keras format)  |
| Deployment  | Docker, AWS EC2              |

---

## 📦 Project Structure

```

Covid App/
├── backend/
│   ├── main.py               # FastAPI app
│   ├── mobilenetv2.keras  # Trained model
├── frontend/
├── requirements.txt

````

---

## 🧪 Local Setup

### 🔹 Step 1: Clone the Repo

## python version 3.11 is required
```bash
git clone https://github.com/Mohammad-Sofyan-Abdullah/Covid-Prediction-App.git
cd Covid-Prediction-App
````


### 🔹 Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run the App

```bash
cd backend
python main.py
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger API docs.

---

## 🐳 Docker Setup

### 🔹 Step 1: Build Docker Image

```bash
docker build -t covid-app_demo .
```

### 🔹 Step 2: Run the Container

```bash
docker run -p 8000:8000 covid-app_demo
```

---


## 🧑‍💻 Author

**Mohammad Sofyan Abdullah**
📧 [LinkedIn](https://www.linkedin.com/in/mohammad-sofyan-abdullah/)
🐙 GitHub: [@Mohammad-Sofyan-Abdullah](https://github.com/Mohammad-Sofyan-Abdullah)

---

