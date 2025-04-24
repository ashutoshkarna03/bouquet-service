FROM python:3.11-slim

# Set working directory
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bouquet.py .

# Set entrypoint to run the application
ENTRYPOINT ["python", "bouquet.py"]
