# Test Cases

| Test Case ID | Test Scenario | Test Steps | Expected Result | Test Type | Priority |
|---|---|---|---|---|---|
| TC_001 | Validate ETL output file creation | Run `python src/etl_pipeline.py` | transformed_transactions.csv should be created | Functional Testing | High |
| TC_002 | Validate required columns | Compare transformed columns with required schema | All required columns should exist | Database Testing | High |
| TC_003 | Validate critical field nulls | Check transaction_id, customer_id, date, category, net_amount | No null values should exist | Data Validation | High |
| TC_004 | Validate duplicate transaction IDs | Check duplicate count for transaction_id | Duplicate count should be 0 | Regression Testing | High |
| TC_005 | Validate successful payments only | Check payment_status in transformed data | Only Success records should exist | Functional Testing | High |
| TC_006 | Validate net amount calculation | Compare calculated net amount with output net_amount | Values should match | Data Validation | High |
| TC_007 | Validate KPI transaction count | Compare transformed row count with expected summary | Count should match expected value | UAT | Medium |
| TC_008 | Validate total revenue KPI | Compare net_amount sum with expected summary | Revenue should match expected value | UAT | Medium |
| TC_009 | Validate unique customers KPI | Compare unique customer count with expected summary | Count should match expected value | UAT | Medium |
| TC_010 | Validate Selenium UI page load | Run Selenium browser check | Page title should load correctly | UI Testing | Low |
