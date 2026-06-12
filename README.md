# Nifty100 Financial Intelligence

A comprehensive FinTech Data Engineering project focused on building a complete financial intelligence platform for Nifty 100 companies listed on the Indian stock market.

## Project Overview

This project aims to develop an end-to-end financial intelligence system that enables investors, analysts, and business users to analyze the financial performance of Nifty 100 companies through dashboards, analytics, APIs, and a web application.

The system covers approximately 12 years of historical financial data and includes ETL pipelines, a PostgreSQL data warehouse, Power BI dashboards, machine learning-based health scoring, and a Django-based web application.

---

## Project Status

🚧 **Work in Progress**

### Current Phase
- Data Engineering Foundation

### Completed
- Repository setup
- GitHub version control setup
- Professional project folder structure
- Initial ETL planning
- README documentation

### Upcoming
- Data extraction from source files
- Data cleaning and transformation
- PostgreSQL star schema implementation
- Power BI dashboard development
- Machine learning health scoring
- Django web application
- REST API development
- Docker containerization

---

## Objectives

- Build a financial intelligence platform for Nifty 100 companies.
- Design and implement a clean star-schema data warehouse.
- Develop ETL pipelines for data extraction and transformation.
- Create interactive Power BI dashboards.
- Generate machine learning-based company health scores.
- Build a Django web application with REST APIs.
- Containerize the application using Docker.

---

## Dataset

The project uses historical financial data for Nifty 100 companies exported from MariaDB and provided as Excel files.

### Source Tables

- Companies
- Analysis
- Balance Sheet
- Profit and Loss
- Cash Flow
- Pros and Cons
- Documents

### Companies Covered

The dataset includes leading companies across multiple sectors such as:

- Information Technology
- Banking
- NBFC
- Insurance
- Energy
- Power
- Cement
- Healthcare
- Consumer Goods
- Automobile
- Paints
- Finance

---

## Technology Stack

### Data Engineering
- Python 3
- Pandas
- NumPy
- SQLAlchemy

### Database
- PostgreSQL

### Business Intelligence
- Microsoft Power BI
- DAX
- Power Query

### Machine Learning
- Scikit-learn
- SciPy
- Matplotlib
- Seaborn

### Web Development
- Django
- Django REST Framework
- Chart.js

### Background Processing
- Celery
- Redis

### Containerization
- Docker
- Docker Compose

### Version Control
- Git
- GitHub

---

## Project Structure

```text
nifty100-financial-intelligence/
│
├── api_docs/
├── data/
│   ├── raw/
│   ├── clean/
│   └── processed/
├── django_app/
├── docker/
├── etl/
├── ml/
├── notebooks/
├── powerbi/
├── warehouse/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ETL Workflow

```text
Excel Files
     ↓
Data Extraction
     ↓
Data Cleaning & Transformation
     ↓
Computed Financial Metrics
     ↓
PostgreSQL Data Warehouse
     ↓
Power BI Dashboards
     ↓
Machine Learning Scoring
     ↓
Django Web Application & APIs
```

---

## Planned Features

### Data Engineering
- Automated ETL pipelines
- Data quality validation
- Financial ratio calculations
- Star schema implementation

### Power BI Dashboards
- Company Overview Dashboard
- Profitability Dashboard
- Balance Sheet Dashboard
- Cash Flow Dashboard
- Growth Analysis Dashboard
- Sector Comparison Dashboard
- ML Health Score Dashboard

### Machine Learning
- Profitability scoring
- Growth scoring
- Leverage scoring
- Cash flow scoring
- Overall health classification

### Web Application
- Public financial dashboards
- Company profile pages
- REST APIs
- Swagger documentation

---

## Future Enhancements

- Scheduled ETL refresh using Celery
- Real-time data ingestion
- API authentication
- Cloud deployment
- CI/CD integration
- Advanced predictive analytics

---

## Author

**Srushti Rajput**

FinTech Data Engineering Project

---

## Disclaimer

This repository is being developed as part of a learning and internship project. Features and implementations will be added incrementally as development progresses.