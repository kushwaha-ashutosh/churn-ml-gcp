import os
import joblib
import pandas as pd
from sklearn.metrics import roc_auc_score

from model import build_model
from utils import split_data


def load_training_data(path):
    """
    Load training data from CSV or BigQuery export.
    """
    df = pd.read_csv(path)
    return df


def train_model(data_path, model_output_path):
    df = load_training_data(data_path)

    X_train, X_test, y_train, y_test = split_data(df)

    model = build_model()
    model.fit(X_train, y_train)

    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)

    print(f"Validation AUC: {auc:.4f}")

    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(model, model_output_path)

    print(f"Model saved to {model_output_path}")


if __name__ == "__main__":
    data_path = os.environ.get("TRAINING_DATA", "data/sample_features.csv")
    model_output = os.environ.get("MODEL_OUTPUT", "artifacts/model.joblib")

    train_model(data_path, model_output)
