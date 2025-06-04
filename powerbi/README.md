# Telecom Customer Churn Dashboard (Power BI)

📊 **Interactive Power BI Dashboard to analyze customer churn behavior in a telecom company.**  
This 3-page report highlights key churn patterns by customer profiles, service types, tenure, and pricing tiers.

---

## 🔍 Objectives

- Identify customer segments with high churn risk
- Analyze impact of pricing, contracts, and services
- Propose data-driven retention strategies

---

## 📁 Dataset

- **Source**: IBM Telco Customer Churn Dataset
- **Rows**: ~7,000 customers  
- **Key fields**: `customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `Contract`, `MonthlyCharges`, `Churn`

---

## 📊 Dashboard Pages Overview

### 1️⃣ Overview
- Total Customers / Churn Rate KPIs
- Churn breakdown by Contract Type, Tenure Group, and Payment Method

### 2️⃣ Customer Profile & Services
- Churn breakdown by Gender, Senior Citizen, Internet Service, Tech Support, Online Security
- Visualized using clustered bar charts and slicers

### 3️⃣ Churn Drivers & Retention Insights
- Tenure vs Monthly Charges scatterplot with churn overlay
- Histogram of MonthlyCharges by churn status
- Insights suggest high churn in 71–90 price tier with short tenure
- Slicer and annotation added for possible dissatisfaction reasons

---

## 🛠️ Tools & Skills Used

- **Power BI**: Dashboard, DAX, Visualizations
- **Data Preparation**: Power Query Editor
- **Data Modeling**: Calculated columns, measures
- **Visuals**: KPI, Bar Charts, Histogram, Scatterplot, Slicer

---

## 🧠 Key Insights

- Month-to-month contract and electronic checks have highest churn rates
- Customers with tenure under 12 months are most likely to churn
- Users in $71–90 monthly tier show notably higher churn — requires pricing review
- Absence of Tech Support and Online Security correlates with higher churn

---

## 🔗 Screenshots

- [Page 1 – Overview](./page1%20-%20overview.png)
- [Page 2 – Customer Profile and Services](./page2%20-%20customer%20profile%20and%20service.png)
- [Page 3 – Churn Factors and Retention](./page3%20-%20churn%20factors%20and%20retention.png)

---

## 📄 PDF Version (optional)

You can also find the exported PDF report [here](./telco-churn-dashboard.pdf)

---

## 💼 Author

- **Name**: Shek Yu Wong
- **Background**: Data Analyst with telecom + reporting experience (SQL, Power BI, Tableau)
