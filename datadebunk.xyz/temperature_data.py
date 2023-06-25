import pandas as pd
import numpy as np
from scipy.stats import linregress
import plotly.graph_objects as go


def fetch_and_parse_data(file_path):
    print("Reading data...")

    # Load the data
    data = pd.read_csv(file_path, skiprows=1)

    # Exclude rows where 'J-D' column contains '*'
    data = data[~data['J-D'].str.contains('\*')]

    # Convert 'J-D' column to numeric
    data['J-D'] = pd.to_numeric(data['J-D'])

    print("Data read and parsed.")
    return data


def generate_temperature_plot():
    file_path = "temperature_data.csv"
    data = fetch_and_parse_data(file_path)

    print("Generating plot...")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=data["Year"], y=data["J-D"], name='Data', line=dict(color='royalblue'))
    )

    mean_data = np.mean(data["J-D"][:-1])  # Exclude the last data point
    std_data = np.std(data["J-D"][:-1])  # Exclude the last data point

    fig.add_trace(
        go.Scatter(x=data["Year"], y=[mean_data] * len(data["Year"]), name='Average',
                   line=dict(color='red', dash='dash'))
    )

    fig.add_trace(
        go.Scatter(x=data["Year"], y=[mean_data + std_data] * len(data["Year"]), line=dict(width=0), showlegend=False)
    )

    fig.add_trace(
        go.Scatter(x=data["Year"], y=[mean_data - std_data] * len(data["Year"]), name='Std. Dev.', line=dict(width=0),
                   fillcolor='rgba(225, 100, 100, 0.2)', fill='tonexty', showlegend=True)
    )

    slope, intercept, r_value, p_value, std_err = linregress(data["Year"], data["J-D"])
    trendline = slope * np.array(data["Year"]) + intercept

    fig.add_trace(
        go.Scatter(x=data["Year"], y=trendline, name='Trendline', line=dict(color='green', dash='dot'))
    )

    fig.update_yaxes(title_text="<b>Temperature (℃)</b>")
    fig.update_xaxes(title_text="<b>Year</b>")

    latest_sign = "increase" if data["J-D"].iloc[-1] > data["J-D"].iloc[-2] else "decrease"
    latest_significance = "significant" if abs(
        data["J-D"].iloc[-1] - data["J-D"].iloc[-2]) > std_data else "not significant"

    print("Plot generated.")
    return fig, latest_sign, latest_significance


if __name__ == "__main__":
    fig, latest_sign, latest_significance = generate_temperature_plot()
    fig.show()
