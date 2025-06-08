from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tensorflow.keras.models import load_model
from io import BytesIO
from tensorflow.keras.preprocessing import image
import numpy as np
import uvicorn
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
templates = Jinja2Templates(directory=FRONTEND_DIR)

# Load your model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "covid_mobilenetv2.keras")
model = load_model(MODEL_PATH)
prediction_stats = {"total": 0, "positive": 0, "negative": 0}

# Landing Page
@app.get("/", response_class=HTMLResponse)
async def serve_landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

# Predict Page
@app.get("/index", response_class=HTMLResponse)
async def serve_predict_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Dashboard Page
@app.get("/dashboard", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# About Page
@app.get("/about", response_class=HTMLResponse)
async def serve_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Predict API
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = image.load_img(BytesIO(contents), target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]
    label = "Covid Positive" if prediction > 0.5 else "Covid Negative"

    prediction_stats["total"] += 1
    prediction_stats["positive" if label == "Covid Positive" else "negative"] += 1

    return JSONResponse({"label": label, "confidence": float(prediction)})

# Stats API
@app.get("/stats")
def stats():
    print("Current Prediction Stats:", prediction_stats)
    return prediction_stats

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8000)