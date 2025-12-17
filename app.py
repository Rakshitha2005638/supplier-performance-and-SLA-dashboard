import dash
from dash import dcc, html, dash_table
import dash.dependencies as dep
import plotly.express as px
from kpi_engine import load_data, calculate_kpis
from ml_model import build_risk_model
import threading
import webbrowser

# ---------------------------
# Load data and compute KPIs
# ---------------------------
df = load_data()
kpi = calculate_kpis(df)
kpi, model = build_risk_model(kpi)

app = dash.Dash(__name__)
app.title = "Supplier Dashboard"


# ---------------------------
# Layout
# ---------------------------
app.layout = html.Div([

    html.H1("📊 Supplier Performance & SLA Dashboard"),

    html.Div([
        html.Label("Filter by Supplier"),
        dcc.Dropdown(
            id="supplier_dropdown",
            options=[{"label": s, "value": s} for s in df["supplier_name"].unique()],
            value=df["supplier_name"].unique()[0],
            clearable=False
        )
    ], style={"width": "20%", "float": "left", "padding": "20px"}),

    html.Div([

        html.H2("📁 Data Preview"),
        dash_table.DataTable(
            id='data_table',
            data=df.head().to_dict("records"),
            columns=[{"name": i, "id": i} for i in df.columns],
            page_size=5,
            style_table={"overflowX": "scroll"}
        ),

        html.H2("📊 Supplier KPI Summary (All Suppliers)"),
        dash_table.DataTable(
            id='kpi_table',
            data=kpi.to_dict("records"),
            columns=[{"name": i, "id": i} for i in kpi.columns],
            page_size=10,
            style_table={"overflowX": "scroll"}
        ),

        html.H2("📊 Supplier KPI Summary (Filtered Supplier)"),
        dash_table.DataTable(
            id='kpi_filtered',
            page_size=1,
            style_table={"overflowX": "scroll"}
        ),

        html.H2("📈 KPI Overview"),
        html.Div(id="kpi_cards"),

        dcc.Graph(id="chart_delivery"),
        dcc.Graph(id="chart_payment"),
        dcc.Graph(id="chart_risk")

    ], style={"width": "75%", "float": "right", "padding": "20px"}),

])


# ---------------------------
# CALLBACKS
# ---------------------------
@app.callback(
    [
        dep.Output("kpi_filtered", "data"),
        dep.Output("kpi_cards", "children"),
        dep.Output("chart_delivery", "figure"),
        dep.Output("chart_payment", "figure"),
        dep.Output("chart_risk", "figure")
    ],
    [dep.Input("supplier_dropdown", "value")]
)
def update_dashboard(supplier):

    filtered = df[df["supplier_name"] == supplier]
    supplier_kpi = kpi[kpi["supplier_name"] == supplier].iloc[0]

    kpi_data = supplier_kpi.to_frame().T.to_dict("records")

    cards = html.Div([
        html.H3(f"{supplier}'s KPIs"),
        html.H4(f"On-Time Delivery: {supplier_kpi['On-Time Delivery %']}%"),
        html.H4(f"Invoice Accuracy: {supplier_kpi['Invoice Accuracy %']}%"),
        html.H4(f"Avg Payment Days: {supplier_kpi['Avg Payment Days']}"),
        html.H4(f"Outstanding Days: {supplier_kpi['Avg Outstanding Days']}"),
        html.H4(f"Predicted Risk: {'HIGH' if supplier_kpi['Predicted Risk']==1 else 'LOW'}"),
    ])

    delivery_fig = px.bar(
        kpi,
        x="supplier_name",
        y="On-Time Delivery %",
        title="On-Time Delivery % by Supplier"
    )

    payment_fig = px.bar(
        kpi,
        x="supplier_name",
        y="Avg Payment Days",
        title="Average Payment Days"
    )

    risk_fig = px.bar(
        kpi,
        x="supplier_name",
        y="Predicted Risk",
        title="Vendor Risk Level"
    )

    return kpi_data, cards, delivery_fig, payment_fig, risk_fig


# ---------------------------
# Auto Open Browser
# ---------------------------
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")


if __name__ == "__main__":
    threading.Timer(1.2, open_browser).start()
    app.run_server(debug=True)
