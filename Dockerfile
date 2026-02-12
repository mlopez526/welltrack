FROM python:3.11-slim

WORKDIR /app

# Copy backend files
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app.py .

# Copy frontend files to the correct location
RUN mkdir -p frontend
COPY frontend/index.html ./frontend/

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
