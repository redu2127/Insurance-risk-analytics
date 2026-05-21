import numpy as np

from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def regression_metrics(y_true, y_pred):
    """Return regression evaluation metrics."""

    rmse = np.sqrt(
        mean_squared_error(y_true, y_pred)
    )

    r2 = r2_score(
        y_true,
        y_pred
    )

    return {
        "RMSE": rmse,
        "R2 Score": r2,
    }


def classification_metrics(y_true, y_pred):
    """Return classification evaluation metrics."""

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred
    )

    recall = recall_score(
        y_true,
        y_pred
    )

    f1 = f1_score(
        y_true,
        y_pred
    )

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
    }


def calculate_recommended_premium(
    claim_probability,
    claim_severity,
    expense_loading=0.10,
    profit_margin=0.15,
):
    """Calculate recommended premium."""

    premium = (
        claim_probability *
        claim_severity
    ) * (
        1 + expense_loading + profit_margin
    )

    return premium



