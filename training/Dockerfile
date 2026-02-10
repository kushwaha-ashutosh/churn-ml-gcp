FROM python:3.10-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install gsutil via Python
RUN pip install --no-cache-dir gsutil

COPY training/ training/
COPY data/ data/

ENTRYPOINT ["python", "training/train_vertex.py"]
