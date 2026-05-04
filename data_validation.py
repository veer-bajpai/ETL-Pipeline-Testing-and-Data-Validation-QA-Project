# JIRA-Style Defect Log

| Defect ID | Summary | Severity | Priority | Status | Root Cause | Resolution |
|---|---|---|---|---|---|---|
| QA-101 | Failed payment record included in reporting layer | High | P1 | Closed | Missing payment_status filter in ETL logic | Added business rule to include only Success payments |
| QA-102 | Net amount mismatch for discounted transactions | High | P1 | Discount formula was not applied during transformation | Added gross_amount, discount_amount, and net_amount calculation |
| QA-103 | Reporting month column missing | Medium | P2 | Month derivation was not included in ETL output | Added reporting_month from transaction_date |
| QA-104 | Duplicate transaction check not automated | Medium | P2 | No regression test existed for duplicate IDs | Added Pytest validation for duplicate transaction IDs |
| QA-105 | KPI summary not validated | Medium | P2 | Expected KPI file was not compared with actual output | Added KPI validation checks for count, revenue, and customers |
