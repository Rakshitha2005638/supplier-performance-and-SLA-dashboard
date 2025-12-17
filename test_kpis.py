import pandas as pd
from kpi_engine import calculate_kpis


# ---------- sample data used for all tests ----------
def get_sample_df():
    df = pd.DataFrame({
        "supplier_name": ["Test Supplier"],
        "po_date": ["2024-01-01"],
        "expected_delivery": ["2024-01-05"],
        "actual_delivery": ["2024-01-04"],
        "invoice_amount": [5000],
        "invoice_status": ["Correct"],
        "payment_date": ["2024-01-10"],
        "due_date": ["2024-01-20"]
    })

    date_cols = [
        "po_date", "expected_delivery",
        "actual_delivery", "payment_date", "due_date"
    ]
    df[date_cols] = df[date_cols].apply(pd.to_datetime)

    return df


# ---------- TEST 1 ----------
def test_on_time_delivery_percentage():
    df = get_sample_df()
    kpi = calculate_kpis(df)
    assert kpi["On-Time Delivery %"].iloc[0] == 100


# ---------- TEST 2 ----------
def test_invoice_accuracy_percentage():
    df = get_sample_df()
    kpi = calculate_kpis(df)
    assert kpi["Invoice Accuracy %"].iloc[0] == 100


# ---------- TEST 3 ----------
def test_avg_payment_days_positive():
    df = get_sample_df()
    kpi = calculate_kpis(df)
    assert kpi["Avg Payment Days"].iloc[0] >= 0


# ---------- TEST 4 ----------
def test_avg_outstanding_days_positive():
    df = get_sample_df()
    kpi = calculate_kpis(df)
    assert kpi["Avg Outstanding Days"].iloc[0] >= 0


# ---------- TEST 5 ----------
def test_kpi_columns_exist():
    df = get_sample_df()
    kpi = calculate_kpis(df)

    required_columns = [
        "On-Time Delivery %",
        "Invoice Accuracy %",
        "Avg Payment Days",
        "Avg Outstanding Days"
    ]

    for col in required_columns:
        assert col in kpi.columns
