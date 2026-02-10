import os
import joblib
import pandas as pd
from sklearn.metrics import roc_auc_score
from model import build_model
from utils import split_data


def train():
    data_path = os.environ.get("TRAINING_DATA", "data/sample_features.csv")
    model_dir = os.environ.get("AIP_MODEL_DIR", "artifacts")

    df = pd.read_csv(data_path)
    X_train, X_test, y_train, y_test = split_data(df)

    model = build_model()
    model.fit(X_train, y_train)

    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)

    print(f"Validation AUC: {auc:.4f}")

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(model, model_path)

    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    train()
