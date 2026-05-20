import pandas as pd

from src.eda_utils import calculate_loss_ratio, calculate_margin


def test_calculate_loss_ratio():
    df = pd.DataFrame({"TotalClaims": [50], "TotalPremium": [100]})
    result = calculate_loss_ratio(df)
    assert result["LossRatio"].iloc[0] == 0.5


def test_calculate_margin():
    df = pd.DataFrame({"TotalClaims": [50], "TotalPremium": [100]})
    result = calculate_margin(df)
    assert result["Margin"].iloc[0] == 50
    