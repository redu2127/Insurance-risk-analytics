import pandas as pd


def calculate_loss_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """Add loss ratio column."""
    df = df.copy()
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]
    return df


def calculate_margin(df: pd.DataFrame) -> pd.DataFrame:
    """Add margin column."""
    df = df.copy()
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df
