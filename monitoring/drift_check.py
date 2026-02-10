import pandas as pd
from scipy.stats import ks_2samp


def detect_drift(train_df, live_df, threshold=0.1):
    drifted_features = []

    for col in train_df.columns:
        if col == "label_churned":
            continue

        stat, p_value = ks_2samp(train_df[col], live_df[col])

        if p_value < threshold:
            drifted_features.append(col)

    return drifted_features
