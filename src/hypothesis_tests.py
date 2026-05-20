import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind


def chi_square_test(
    data: pd.DataFrame,
    group_col: str,
    target_col: str,
) -> float:
    """Run chi-square test for categorical risk differences."""
    table = pd.crosstab(data[group_col], data[target_col])
    _, p_value, _, _ = chi2_contingency(table)
    return p_value


def t_test_between_groups(
    data: pd.DataFrame,
    group_col: str,
    value_col: str,
    group_a,
    group_b,
) -> float:
    """Run Welch t-test between two groups."""
    a_values = data[data[group_col] == group_a][value_col].dropna()
    b_values = data[data[group_col] == group_b][value_col].dropna()

    _, p_value = ttest_ind(
        a_values,
        b_values,
        equal_var=False,
    )
    return p_value


def hypothesis_decision(
    p_value: float,
    alpha: float = 0.05,
) -> str:
    """Return decision based on p-value."""
    if p_value < alpha:
        return "Reject H0"
    return "Fail to Reject H0"
