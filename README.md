--------Supplier Performance & SLA Dashboard--------

--Project Overview--
This project is a Supplier Performance & SLA Dashboard built using Python, Pandas, Plotly Dash, and Machine Learning.
It analyzes supplier data to calculate key performance indicators (KPIs) such as on-time delivery, invoice accuracy, average payment days, and outstanding days, and predicts vendor risk using a machine learning model.The dashboard provides interactive visualizations, filters, and tables for business decision-making.

--Objectives-- 
1. Analyze supplier performance using KPIs
2. Visualize supplier metrics interactively
3. Predict vendor risk using Machine Learning
4. Ensure correctness using unit testing

--Technologies Used-- 
1. Python 3.7+
2. Pandas - Data processing
3. Plotly Dash - Dashboard & UI
4. Scikit-learn - Machine Learning (Random Forest)
5. Pytest - Unit Testing
6. PostgreSQL / CSV - Data source
7. Conda Environment

--project structure-- 
supplier_dashboard_project/
│
├── app.py                  # Dash application
├── kpi_engine.py           # KPI calculations
├── ml_model.py             # Risk prediction model
├── data/
│   └── supplier_data.csv   # Supplier dataset
│
├── tests/
│   └── test_kpis.py        # Unit tests (pytest)
│
├── requirements.txt
└── README.md

--KPIs Calculated--
1. On-Time Delivery (%)
2. Invoice Accuracy (%)
3. Average Payment Days
4. Average Outstanding Days
5. Predicted Vendor Risk (HIGH / LOW)

--Sample Data Explanation--
The project uses a synthetic supplier dataset stored in a CSV file (supplier_data.csv).
Each row represents a purchase order and invoice transaction for a supplier.
This data is used to calculate performance KPIs and predict supplier risk.

Dataset Columns Description:
| Column Name         | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `supplier_name`     | Name of the supplier/vendor                          |
| `po_date`           | Purchase order creation date                         |
| `expected_delivery` | Expected delivery date as per agreement              |
| `actual_delivery`   | Actual delivery date of goods                        |
| `invoice_amount`    | Invoice amount for the order                         |
| `invoice_status`    | Invoice verification status (`Correct` / `Rejected`) |
| `payment_date`      | Date when payment was made                           |
| `due_date`          | Invoice due date                                     |

How the Data Is Used:

1. On-Time Delivery (%)
Calculated by comparing actual_delivery with expected_delivery
2. Invoice Accuracy (%)
Based on the percentage of invoices marked as Correct
3. Average Payment Days
Difference between payment_date and actual_delivery
4. Average Outstanding Days
Difference between due_date and payment_date (non-negative)
5. Vendor Risk Prediction
Suppliers with low performance metrics are classified as High Risk using a Machine Learning model

Sample Data (Example):
supplier_name,po_date,expected_delivery,actual_delivery,invoice_amount,invoice_status,payment_date,due_date
Supplier A,2024-01-01,2024-01-05,2024-01-04,12000,Correct,2024-01-10,2024-01-20
Supplier B,2024-01-02,2024-01-06,2024-01-08,18000,Rejected,2024-01-12,2024-01-22
Supplier C,2024-01-03,2024-01-07,2024-01-07,9000,Correct,2024-01-15,2024-01-25

Importance of Sample Data:
1. Enables KPI validation
2. Supports unit testing using pytest
3. Helps visualize supplier performance trends
4. Ensures consistent ML model training


--How to Run the Project--
1️.Clone or Download the Project
git clone <repository_url>
cd supplier_dashboard_project
2️.Create & Activate Conda Environment
conda create -n supplierdash python=3.7 -y
conda activate supplierdash
3. Install Required Libraries
pip install -r requirements.txt
4️. Run the Dashboard
python app.py
The dashboard will open automatically in your browser at:
http://127.0.0.1:8050/

--Unit Testing--
Testing Framework : pytest
Run Tests:
pytest
Sample Test Output:
==================== test session starts ====================
collected 1 item
tests/test_kpis.py .
1 passed in 1.55s

--Machine Learning Model--
1. Algorithm: Random Forest Classifier
2. Input Features:
3. On-Time Delivery %
4. Invoice Accuracy %
5. Avg Payment Days
6. Avg Outstanding Days
7. Output: Vendor Risk (High / Low)

--Dashboard Features--
1. Supplier-wise filtering
2. KPI summary tables
3. Interactive bar charts
4. Auto-open browser functionality
5. Real-time KPI updates

--Output--
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/c4b8cbd6-ca32-4fe4-87c8-2df141e0639c" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/8a6e6fa7-9060-48b6-85e9-03a6ca5dcf1e" />


   

Author
Rakshitha HS
Project: Supplier Performance & SLA Dashboard


