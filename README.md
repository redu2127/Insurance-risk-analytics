# Insurance Risk Analytics and Predictive Modeling

## Project Overview

This project analyzes insurance claim risk and develops predictive models for claim severity and claim probability. The objective is to support evidence-based insurance pricing strategies using exploratory data analysis, statistical hypothesis testing, and machine learning.

---

# Business Objective

The project aims to help insurers:

- identify high-risk customer segments,
- optimize underwriting strategies,
- improve premium pricing,
- reduce unexpected claim losses,
- support data-driven actuarial decision-making.

---

# Project Structure

insurance-risk-analytics/
│
├── .github/workflows/
├── data/
├── notebooks/
├── reports/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
---

# Tasks Completed

## Task 1 — Exploratory Data Analysis

- Data loading and preprocessing
- Missing value analysis
- Distribution analysis
- Claim and premium exploration
- Visual risk analysis

### Technologies
- Pandas
- Matplotlib
- Seaborn

---

## Task 2 — Data Version Control (DVC)

- DVC initialization
- Dataset version tracking
- Remote storage configuration
- Reproducible data pipeline

### DVC Commands

dvc init
dvc add data/MachineLearningRating_v3.txt
dvc push
dvc pull
---

## Task 3 — Hypothesis Testing

### Statistical Tests Performed

- Chi-Square Test
- Welch T-Test

### Hypotheses

1. Risk differences across provinces
2. Risk differences between postal codes
3. Margin differences between postal codes
4. Gender-based risk differences

### Key Findings

- Provincial claim differences were statistically significant.
- Margin variations existed across postal codes.
- Risk patterns varied across customer groups.

---

## Task 4 — Predictive Modeling

### Regression Models

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

### Classification Models

- Random Forest Classifier
- XGBoost Classifier

### Evaluation Metrics

#### Regression
- RMSE
- R² Score

#### Classification
- Accuracy
- Precision
- Recall
- F1 Score

---

# Risk-Based Pricing Framework

The recommended premium is calculated using:

Premium =
Claim Probability × Claim Severity ×
(1 + Expense Loading + Profit Margin)
This framework supports risk-sensitive insurance pricing.

---

# Installation

## Clone Repository

git clone <repository-url>
cd insurance-risk-analytics
## Create Virtual Environment

python -m venv venv
## Activate Environment

### Windows

venv\Scripts\activate
### Linux/Mac

source venv/bin/activate
## Install Dependencies

pip install -r requirements.txt
---

# Running Tests

python -m pytest
---

# Code Quality

flake8 src
---

