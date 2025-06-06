# Telecom Customer Churn Dashboard (Tableau)

📊 **Interactive Tableau Dashboard to analyze customer churn behavior in a telecom company.**  
This 3-page report explores churn patterns across customer profiles, service usage, tenure, and pricing levels using intuitive Tableau visualizations.

---

## 🔍 Objectives

- Identify customer groups with high churn risk
- Visualize how contract type, pricing, and services affect churn
- Support retention strategy with actionable insights

---

## 📁 Dataset

- **Source**: IBM Telco Customer Churn Dataset
- **Rows**: ~7,000 customers  
- **Key fields**: `customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `Contract`, `MonthlyCharges`, `Churn`

---

## 📊 Dashboard Pages Overview

### 1️⃣ Overview
- KPIs showing Total Customers, Churned Customers, and Churn Rate
- Churn breakdown by Contract Type and Payment Method
- Highlighted insights for high-risk churn segments

### 2️⃣ Customer Profile & Services
- Churn visualization by Gender, Dependents, Internet Service, Tech Support, and Online Security
- Combination of bar charts and bubble charts for segmentation

### 3️⃣ Churn Drivers & Retention Insights
- Faceted charts of Tenure vs MonthlyCharges grouped by customer age
- Analysis of churn concentration in high-price, low-tenure segments
- Interactive filters to drill down by services and demographics
- Text-based Retention Insight summary provided

---

## 🛠️ Tools & Skills Used

- **Tableau Public**: Worksheets, Dashboards, Filters, Parameters
- **Data Preparation**: Calculated fields, groupings (tenure, charges)
- **Visuals**: KPI Cards, Bar Charts, Donut Charts, Bubble Charts, Small Multiples
- **Design**: Slicers, annotations, clean layout for PDF export

---

## 🧠 Key Insights

- Customers on month-to-month contracts using electronic checks churn the most
- Tenure under 12 months is strongly linked with high churn
- Churn peaks for users paying $71–90/month — possibly due to unmet expectations
- Lack of Tech Support or Online Security significantly increases churn risk

---

## 🔗 Screenshots

- [Page 1 – Overview](./screenshots/page1%20-%20overview.png)
- [Page 2 – Customer Profile and Services](./screenshots/page2%20-%20customer%20profile%20and%20service.png)
- [Page 3 – Churn Factors and Retention](./screenshots/page3%20-%20churn%20factors%20and%20retention.png)

---

## 📄 PDF Version

You can also find the exported Tableau report [here](../../reports/telecom-churn-combined-dashboards.pdf)

---

## 💼 Author

- **Name**: Shek Yu Wong  
- **Background**: Data Analyst with telecom & reporting expertise (SQL, Power BI, Tableau)
