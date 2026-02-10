import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df, label_column="label_churned"):
    X = df.drop(columns=[label_column, "customer_id"])
    y = df[label_column]

    return train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
