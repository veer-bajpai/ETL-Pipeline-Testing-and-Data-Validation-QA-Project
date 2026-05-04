# ETL Pipeline Testing and Data Validation QA Project

A QA-focused project designed to validate an ETL pipeline using manual test cases, SQL-based data validation, Python automation, and basic Selenium UI checks. This project demonstrates software testing, quality assurance, functional testing, regression testing, database testing, defect tracking, and Business User Acceptance Testing UAT concepts.

## Project Objective

The goal of this project is to test whether customer transaction data is accurately extracted, transformed, and loaded into a reporting-ready dataset. The framework validates data accuracy, completeness, transformation logic, duplicate handling, null checks, KPI calculations, and dashboard readiness.

## Resume Alignment

This project supports the following resume bullet points:

- Designed and executed 30+ test cases and validation scenarios for ETL pipelines
- Reduced critical defects through SQL-based validation checks
- Tracked defects using a JIRA-style defect log
- Automated validation checks using Python and basic Selenium UI checks
- Improved test coverage across source, transformed, and reporting layers

## Tools and Technologies

- Python
- SQL SQLite
- Pandas
- Pytest
- Selenium WebDriver Basics
- JIRA-style defect tracking
- Excel or CSV datasets

## Folder Structure

```text
qa-testing-etl-validation-framework/
│
├── data/
│   ├── raw_transactions.csv
│   ├── transformed_transactions.csv
│   └── expected_kpi_summary.csv
│
├── src/
│   ├── etl_pipeline.py
│   ├── data_validation.py
│   └── db_setup.py
│
├── tests/
│   ├── test_data_validation.py
│   └── test_basic_ui_selenium.py
│
├── docs/
│   ├── test_cases.md
│   └── defect_log.md
│
├── reports/
│   └── qa_summary_report.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

| Testing Area | Validation Performed |
|---|---|
| Data Completeness | Null checks for transaction ID, customer ID, amount, and date |
| Data Accuracy | Revenue and KPI totals matched against expected outputs |
| Duplicate Testing | Duplicate transaction IDs detected |
| Transformation Testing | Discounted amount calculated correctly |
| Regression Testing | Re-runnable automated validation checks using Pytest |
| Database Testing | SQL queries validate row count, revenue, and category-level metrics |
| Basic UI Testing | Selenium checks page title and page load behavior |

## Dataset Description

The dataset represents customer transactions from a retail analytics workflow.

| Column | Description |
|---|---|
| transaction_id | Unique transaction identifier |
| customer_id | Unique customer identifier |
| transaction_date | Date of purchase |
| category | Product category |
| quantity | Number of units purchased |
| unit_price | Price per unit |
| discount_pct | Discount percentage |
| payment_status | Payment status |

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/qa-testing-etl-validation-framework.git
cd qa-testing-etl-validation-framework
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

Mac or Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run ETL pipeline

```bash
python src/etl_pipeline.py
```

### 6. Run validation checks

```bash
python src/data_validation.py
```

### 7. Run automated tests

```bash
pytest tests/
```

## Sample Validation Checks

- Validate no missing transaction IDs
- Validate no duplicate transaction IDs
- Validate discounted amount formula
- Validate only successful payments are included in reporting output
- Validate total revenue matches expected KPI summary
- Validate transformed file contains required reporting columns

## QA Summary

This project simulates a real-world quality assurance workflow where a tester validates ETL output before it is used for dashboards or business reporting. It combines functional testing, database testing, regression testing, defect tracking, and test documentation in one end-to-end framework.

## Author

Veer Bajpai
