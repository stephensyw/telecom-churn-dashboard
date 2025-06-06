# 📁 Dataset – IBM Telco Customer Churn

This folder contains the raw dataset used in the Power BI and Tableau dashboards for analyzing customer churn patterns in the telecom industry.

---

## 📊 Dataset Overview

- **Source**: IBM Sample Dataset – Telco Customer Churn  
- **Format**: CSV (`dataset.csv`)  
- **Rows**: ~7,043 records  
- **Columns**: 21 fields

The dataset represents anonymized customer information from a fictional telecom company, used to predict customer churn behavior.

---

## 🔑 Key Fields

| Column Name         | Description                                      |
|---------------------|--------------------------------------------------|
| `customerID`        | Unique customer identifier                       |
| `gender`            | Gender (Male / Female)                           |
| `SeniorCitizen`     | 1 = Yes, 0 = No                                   |
| `Partner`           | Whether customer has a partner (Yes/No)          |
| `Dependents`        | Whether customer has dependents (Yes/No)         |
| `tenure`            | Number of months as a customer                   |
| `PhoneService`      | Whether phone service is active (Yes/No)         |
| `MultipleLines`     | Whether customer has multiple lines              |
| `InternetService`   | DSL / Fiber optic / No                           |
| `OnlineSecurity`    | Whether customer has online security             |
| `OnlineBackup`      | Whether customer has online backup               |
| `DeviceProtection`  | Whether customer has device protection           |
| `TechSupport`       | Whether customer has tech support                |
| `StreamingTV`       | Whether customer has streaming TV                |
| `StreamingMovies`   | Whether customer has streaming movies            |
| `Contract`          | Month-to-month / One year / Two year             |
| `PaperlessBilling`  | Whether customer uses paperless billing (Yes/No) |
| `PaymentMethod`     | Method used to pay (e.g. Electronic check)       |
| `MonthlyCharges`    | Current monthly charges                          |
| `TotalCharges`      | Lifetime total charges                           |
| `Churn`             | Whether customer churned (Yes/No)                |

---

## ⚙️ Preprocessing Notes

- All columns used **as-is** in the Power BI and Tableau dashboards  
- Calculated fields (e.g. `TenureGroup`, `MonthlyChargesGroup`) were created within each tool, not modified in the dataset
- Nulls in `TotalCharges` were filtered or handled during transformation

---

## 📂 Usage

This dataset is read into both:
- [Power BI Dashboard] (../dashboards/powerbi/telecom-churn.pbix)
- [Tableau Dashboard] (../dashboards/tableau/telecom-churn.twbx)

For consistent reproducibility, the CSV is shared as a single source of truth.

---

## 📄 License & Acknowledgment

This dataset is publicly available and intended for educational or portfolio use only.  
All rights and credit belong to the original data publisher:

- 📎 [IBM Telco Customer Churn Dataset on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

> © IBM. No commercial usage. Dataset used strictly for analysis and demonstration purposes.