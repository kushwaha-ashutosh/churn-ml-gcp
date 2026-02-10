import os
import pandas as pd
import numpy as np


RAW_PATH = "data/raw/telco_churn.csv"
OUTPUT_PATH = "data/sample_features.csv"


def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Standardize column names
    df.columns = [c.strip() for c in df.columns]

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Drop rows with missing critical values
    df = df.dropna(subset=["TotalCharges"])

    return df


def engineer_features(df):
    """
    Convert telco dataset into production-style churn features.
    """

    features = pd.DataFrame()

    # Customer ID
    features["customer_id"] = df["customerID"]

    # Simulated usage features
    features["avg_usage_30d"] = df["MonthlyCharges"]

    # Login frequency proxy using tenure
    features["login_frequency_30d"] = df["tenure"] / 2.0

    # Simulated support tickets
    # Customers with fiber + high charges likely to complain more
    features["support_tickets_60d"] = (
        (df["InternetService"] == "Fiber optic").astype(int)
        + (df["MonthlyCharges"] > df["MonthlyCharges"].median()).astype(int)
    )

    # Label
    features["label_churned"] = (
        df["Churn"].map({"Yes": 1, "No": 0})
    )

    return features


def save_features(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Feature file saved to {path}")
    print(f"Rows: {len(df)}")
    print(df.head())


def main():
    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError(
            f"Raw dataset not found at {RAW_PATH}. "
            "Place telco_churn.csv in data/raw/"
        )

    df = load_data(RAW_PATH)
    df = clean_data(df)
    features = engineer_features(df)
    save_features(features, OUTPUT_PATH)


if __name__ == "__main__":
    main()
