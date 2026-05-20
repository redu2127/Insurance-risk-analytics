# Insurance Risk Analytics and Predictive Modeling

## Project Overview

This project analyzes insurance risk patterns and develops predictive models for claim severity and claim probability. The objective is to support risk-based pricing strategies using statistical analysis and machine learning techniques.

---

# Task 1: Exploratory Data Analysis (EDA)

## Objectives

- Understand claim distribution
- Explore premium and loss behavior
- Detect risk patterns across customer segments
- Identify data quality issues

## Key Findings

- Certain provinces showed higher claim frequencies.
- Claim distributions were highly skewed.
- Premium values varied significantly across customer groups.
- Missing values were identified in several categorical variables.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# Task 2: Data Version Control (DVC)

## Objectives

- Track large datasets efficiently
- Ensure reproducibility
- Separate code and data versioning

## DVC Pipeline

- Initialized DVC repository
- Added dataset tracking
- Configured remote storage
- Versioned insurance dataset

## Benefits

- Reproducibility
- Scalable data management
- Collaboration support

---

# Task 3: A/B Hypothesis Testing

## Objectives

Evaluate statistical risk differences across customer groups.

## Hypotheses Tested

1. Risk differences across provinces
2. Risk differences between postal codes
3. Margin differences between postal codes
4. Risk differences between genders

## Statistical Methods

- Chi-Square Test
- Welch T-Test

## Key Results

- Significant provincial risk differences were detected.
- Postal code margin differences were identified.
- Gender-based differences were comparatively smaller.

## Business Impact

The findings support:
- region-based pricing,
- targeted underwriting,
- profitability optimization.

---

# Task 4: Predictive Modeling

## Objectives

Build predictive models for:
- claim severity,
- claim probability,
- premium recommendation.

## Models Implemented

### Regression Models

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

### Classification Models

- Random Forest Classifier
- XGBoost Classifier

## Evaluation Metrics

### Regression

- RMSE
- R² Score

### Classification

- Accuracy
- Precision
- Recall
- F1 Score

## Feature Importance

Important predictors included:
- Province
- Vehicle age
- Vehicle type
- Vehicle value
- Postal code

## Risk-Based Pricing Framework

Recommended Premium:

Premium = Claim Probability × Claim Severity × (1 + Expense Loading + Profit Margin)

This framework supports data-driven insurance pricing strategies.

---

# Conclusion

This project successfully combined:
- exploratory data analysis,
- statistical testing,
- predictive modeling,
- and pricing optimization

to support insurance risk assessment and evidence-based decision-making.

The final solution provides a scalable workflow for actuarial analytics and predictive insurance pricing.