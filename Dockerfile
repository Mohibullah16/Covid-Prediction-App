# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend source and frontend templates
COPY backend/ backend/
COPY frontend/ frontend/

# Copy model files to root (or backend if your code expects that)
COPY backend/covid_mobilenetv2.keras .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Launch FastAPI app without reload (for production)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

