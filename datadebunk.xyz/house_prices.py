import pandas as pd
import numpy as np
from scipy.stats import linregress
import plotly.graph_objects as go

def fetch_and_parse_data(file_path):
    print("Reading data...")

    # Load the data
    data = pd.read_csv(file_path)

    # Remove the '$' sign and ',' from 'price' column, and convert it to float
    data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)

    # Convert 'month' to datetime
    data['month'] = pd.to_datetime(data['month'])

    # Extract the year from 'month' and create a new 'year' column
    data['year'] = data['month'].dt.year

    print("Data read and parsed.")
    return data

def generate_price_plot():
    file_path = "house_price_data.csv"
    data = fetch_and_parse_data(file_path)

    print("Calculating yearly averages...")

    # Exclude years with incomplete data
    year_counts = data['year'].value_counts()
    full_years = year_counts[year_counts == 12].index

    data = data[data['year'].isin(full_years)]

    # Calculate yearly averages
    yearly_data = data.groupby('year')['price'].mean().reset_index()

    print("Generating plot...")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=yearly_data["year"], y=yearly_data["price"], name='Data', line=dict(color='royalblue'))
    )

    mean_data = np.mean(yearly_data["price"][:-1])  # Exclude the last data point
    std_data = np.std(yearly_data["price"][:-1])  # Exclude the last data point

    fig.add_trace(
        go.Scatter(x=yearly_data["year"], y=[mean_data] * len(yearly_data["year"]), name='Average',
                   line=dict(color='red', dash='dash'))
    )

    fig.add_trace(
        go.Scatter(x=yearly_data["year"], y=[mean_data + std_data] * len(yearly_data["year"]), line=dict(width=0), showlegend=False)
    )

    fig.add_trace(
        go.Scatter(x=yearly_data["year"], y=[mean_data - std_data] * len(yearly_data["year"]), name='Std. Dev.', line=dict(width=0),
                   fillcolor='rgba(225, 100, 100, 0.2)', fill='tonexty', showlegend=True)
    )

    slope, intercept, r_value, p_value, std_err = linregress(yearly_data.index, yearly_data["price"])
    trendline = slope * np.array(yearly_data.index) + intercept

    fig.add_trace(
        go.Scatter(x=yearly_data["year"], y=trendline, name='Trendline', line=dict(color='green', dash='dot'))
    )

    fig.update_yaxes(
        title_text="<b>Price ($)</b>",
        range=[0, max(yearly_data["price"]) + std_data])
    fig.update_xaxes(title_text="<b>Year</b>")

    fig.update_layout(
        {
            "dragmode": False,
        }
    )

    latest_sign = "increase" if yearly_data["price"].iloc[-1] > yearly_data["price"].iloc[-2] else "decrease"
    latest_significance = "significant" if abs(
        yearly_data["price"].iloc[-1] - yearly_data["price"].iloc[-2]) > std_data else "not significant"

    print("Plot generated.")
    return fig, latest_sign, latest_significance

if __name__ == "__main__":
    fig, latest_sign, latest_significance = generate_price_plot()
    fig.show()
