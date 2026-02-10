# Customer Churn Prediction Platform (GCP)

Production-grade cloud-native ML system built on Google Cloud using Vertex AI.

## Architecture

Data → GCS → Feature pipeline → Vertex AI training → Model registry → Endpoint

## Tech Stack

- Google Cloud (Vertex AI, GCS, Artifact Registry)
- Docker
- Python (scikit-learn)
- Terraform (IaC)
- GitHub Actions (CI/CD)

## Key Features

- End-to-end ML lifecycle
- Containerized training
- Cloud-native deployment
- Infrastructure as Code
- Automated CI pipeline

## Results

- Validation AUC: ~0.76–0.81
- Model trained on Telco churn dataset

## How to run locally

```bash
pip install -r requirements.txt
python pipelines/feature_engineering/transform_telco.py
python training/train.py
