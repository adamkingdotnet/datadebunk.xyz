import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.stats import linregress


def fetch_and_parse_data(file_path):
    print("Reading data...")

    # Load the data
    data = pd.read_csv(file_path)

    # Extract the relevant columns
    year = data["year"]
    incidents = data["total incidents of all crime per 100k people"]

    print("Data read and parsed.")
    return year, incidents


def generate_crime_plot():
    file_path = "crime.csv"
    year, incidents = fetch_and_parse_data(file_path)

    print("Generating plot...")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=year, y=incidents, name="Data", line=dict(color="royalblue")))

    mean_data = incidents.mean()
    std_data = incidents.std()

    fig.add_trace(go.Scatter(x=year, y=[mean_data] * len(year), name="Average", line=dict(color="red", dash="dash")))

    fig.add_trace(go.Scatter(x=year, y=incidents + std_data, line=dict(width=0), showlegend=False))

    fig.add_trace(
        go.Scatter(
            x=year,
            y=incidents - std_data,
            name="Std. Dev.",
            line=dict(width=0),
            fillcolor="rgba(225, 100, 100, 0.2)",
            fill="tonexty",
            showlegend=True,
        )
    )

    slope, intercept, r_value, p_value, std_err = linregress(year, incidents)
    trendline = slope * np.array(year) + intercept

    fig.add_trace(go.Scatter(x=year, y=trendline, name="Trendline", line=dict(color="green", dash="dot")))

    fig.update_yaxes(title_text="<b>Incidents of Crime per 100k People</b>", range=[0, max(incidents) + std_data])
    fig.update_xaxes(title_text="<b>Year</b>")

    fig.update_layout(
        {
            "dragmode": False,
        }
    )

    latest_sign = "increase" if incidents.iloc[-1] > incidents.iloc[-2] else "decrease"
    latest_significance = (
        "significant" if abs(incidents.iloc[-1] - incidents.iloc[-2]) > std_data else "not significant"
    )

    print("Plot generated.")
    return fig, latest_sign, latest_significance


if __name__ == "__main__":
    fig, latest_sign, latest_significance = generate_crime_plot()
    fig.show()
