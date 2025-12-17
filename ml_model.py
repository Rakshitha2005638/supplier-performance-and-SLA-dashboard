import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def build_risk_model(kpi_df):
    kpi_df["risk"] = (kpi_df["On-Time Delivery %"] < 70).astype(int)

    X = kpi_df[[
        "On-Time Delivery %",
        "Invoice Accuracy %",
        "Avg Payment Days",
        "Avg Outstanding Days"
    ]]
    y = kpi_df["risk"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    kpi_df["Predicted Risk"] = model.predict(X)
    return kpi_df, model
