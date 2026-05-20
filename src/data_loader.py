import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load insurance data from a CSV file."""
    return pd.read_csv(filepath)
