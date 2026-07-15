# Dynamic Pricing Optimization Platform

A machine learning-powered analytics platform that helps financial institutions optimize product pricing, segment customers, validate pricing strategies through A/B testing, and estimate long-term business impact using statistical and financial analysis.

The platform simulates how organizations can make data-driven pricing decisions by combining customer analytics, predictive machine learning models, hypothesis testing, and revenue forecasting into a single interactive dashboard.

---

## Business Problem

Financial institutions continuously struggle with determining optimal pricing for products such as personal loans, credit cards, and mortgages.

Pricing products too low reduces profitability, while pricing them too high decreases customer conversion and market competitiveness.

Traditional pricing approaches often fail to simultaneously consider:

- Customer behavior
- Risk profiles
- Expected conversion rates
- Revenue impact
- Statistical significance of pricing changes
- Long-term business outcomes

This project addresses these challenges by providing an end-to-end pricing optimization platform that enables data-driven decision making.

---

## Solution

The platform consists of four integrated analytical modules:

### 1. Customer Segmentation

- K-Means clustering
- Customer profiling
- Segment comparison
- Customer Lifetime Value (CLV) analysis
- Strategic recommendations
- Interactive visualization dashboard

---

### 2. Price Optimization

Gradient Boosting models predict:

- Optimal product pricing
- Expected customer conversion
- Revenue lift
- Price sensitivity

Includes:

- Feature importance analysis
- Business simulator
- Revenue optimization
- Scenario analysis

---

### 3. A/B Testing Framework

Statistically validates pricing strategies using:

- Hypothesis testing
- Confidence intervals
- Chi-Square Test
- Independent T-Test
- Statistical Power Analysis
- Effect Size (Cohen's d)
- Decision Framework
- Risk Assessment

---

### 4. Revenue Impact Analysis

Evaluates business impact through:

- Revenue forecasting
- ROI estimation
- Multi-year projections
- CLV analysis
- Financial health indicators
- Executive summary
- Strategic recommendations

---

# Features

- Interactive Streamlit dashboard
- Customer segmentation using K-Means
- Gradient Boosting pricing engine
- Conversion prediction
- Price sensitivity analysis
- Statistical A/B testing
- Revenue optimization
- Customer Lifetime Value analysis
- ROI calculator
- Financial projections
- Exportable analytical reports
- Business recommendation engine

---

# Machine Learning Models

| Task | Algorithm |
|-------|-----------|
| Customer Segmentation | K-Means Clustering |
| Price Prediction | Gradient Boosting Regressor |
| Conversion Prediction | Gradient Boosting Regressor |

---

# Statistical Methods

The platform incorporates multiple statistical techniques including:

- Hypothesis Testing
- Chi-Square Test
- Independent Sample T-Test
- Confidence Interval Estimation
- Statistical Power Analysis
- Effect Size (Cohen's d)
- Revenue Impact Analysis

---

# Dashboard Modules

## Home Dashboard

Provides a high-level overview of:

- Customer segments
- Product categories
- Active experiments
- Revenue insights
- Market trends

---

## Customer Segmentation

- Customer distribution
- Cluster visualization
- Radar chart comparison
- Segment profiles
- CLV analysis
- Model evaluation

---

## Price Optimization

- Pricing recommendations
- Model performance
- Feature importance
- Revenue simulator
- Price sensitivity analysis

---

## A/B Testing

- Statistical significance testing
- Confidence intervals
- Daily performance tracking
- Statistical power
- Decision framework
- Risk assessment

---

## Revenue Analysis

- Revenue projection
- ROI analysis
- CLV impact
- Multi-year forecast
- Executive summary
- Strategic recommendations

---

# Project Structure

```
Dynamic-Pricing-Optimization-Platform
│
├── app.py
├── pages
│   ├── Customer_Segmentation.py
│   ├── Price_Optimization.py
│   ├── AB_Testing.py
│   └── Revenue_Analysis.py
│
├── data
├── models
├── utils
├── requirements.txt
└── README.md
```

---

# Technology Stack

### Programming

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Data Processing

- Pandas
- NumPy
- SciPy

### Visualization

- Plotly
- Matplotlib

### Web Framework

- Streamlit

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/dynamic-pricing-optimization-platform.git
```

Move into the project directory

```bash
cd dynamic-pricing-optimization-platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Sample Workflow

Customer Data

↓

Customer Segmentation

↓

Price Optimization

↓

A/B Testing

↓

Revenue Forecasting

↓

Business Decision

---

# Business Value

The platform enables organizations to:

- Improve pricing decisions using machine learning
- Identify high-value customer segments
- Quantify pricing impact before deployment
- Validate pricing experiments statistically
- Forecast long-term revenue outcomes
- Estimate return on investment
- Support business stakeholders with data-driven insights

---

# Screenshots

### Home

![Home](assets\home.png)

### Customer Segmentation

![Customer Segmentation](assets\customer-segmentation.png)

### Price Optimization

![Price Optimization](assets\price-optimisation.png)

### A/B Testing

![A/B Testing](assets\ab-testing.png)

### Revenue Analysis

![Revenue Analysis](assets\revenue-impact.png)

---

# Future Improvements

Planned enhancements include:

- SHAP-based model explainability
- LLM-powered executive summaries
- FastAPI deployment for prediction APIs
- Real-time streaming data support
- PostgreSQL integration
- Automated report generation (PDF)
- Docker containerization
- Cloud deployment on AWS

---

# Author

**Kanishk Tiwari**

B.Tech Computer Science

Netaji Subhas University of Technology (NSUT)

Interested in Machine Learning, Data Science, Backend Development, and Business Analytics.

---