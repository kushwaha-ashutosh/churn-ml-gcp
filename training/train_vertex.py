import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from google.cloud import storage


def upload_to_gcs(local_path, bucket_name, blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_path)
    print(f"Model uploaded to gs://{bucket_name}/{blob_name}")


def train():
    data_path = "data/sample_features.csv"
    df = pd.read_csv(data_path)

    X = df.drop(columns=["customer_id", "label_churned"])
    y = df["label_churned"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    print(f"Validation AUC: {auc:.4f}")

    os.makedirs("model", exist_ok=True)
    local_model_path = "model/model.joblib"
    joblib.dump(model, local_model_path)

    print("Model saved locally. Uploading to GCS...")

    bucket_name = "churn-ml-demo-bucket"
    blob_name = "model/model.joblib"

    upload_to_gcs(local_model_path, bucket_name, blob_name)


if __name__ == "__main__":
    train()
