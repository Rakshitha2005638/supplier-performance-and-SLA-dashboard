import pandas as pd

def load_data(path="data/supplier_data.csv"):
    df = pd.read_csv(path, parse_dates=[
        "po_date", "expected_delivery", "actual_delivery",
        "payment_date", "due_date"
    ])
    return df


def calculate_kpis(df):
    df["on_time"] = df["actual_delivery"] <= df["expected_delivery"]
    df["invoice_correct"] = df["invoice_status"] == "Correct"
    df["payment_days"] = (df["payment_date"] - df["actual_delivery"]).dt.days
    df["outstanding_days"] = (df["due_date"] - df["payment_date"]).dt.days.clip(lower=0)

    kpi = df.groupby("supplier_name").agg({
        "on_time": "mean",
        "invoice_correct": "mean",
        "payment_days": "mean",
        "outstanding_days": "mean"
    }).reset_index()

    kpi["On-Time Delivery %"] = (kpi["on_time"] * 100).round(2)
    kpi["Invoice Accuracy %"] = (kpi["invoice_correct"] * 100).round(2)
    kpi["Avg Payment Days"] = kpi["payment_days"].round(2)
    kpi["Avg Outstanding Days"] = kpi["outstanding_days"].round(2)

    return kpi
