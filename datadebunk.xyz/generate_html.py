# File: generate_html.py

from temperature_data import generate_temperature_plot
from house_prices import generate_price_plot


def generate_html():
    fig_temperature, latest_sign_temperature, latest_significance_temperature = generate_temperature_plot()
    fig_price, latest_sign_price, latest_significance_price = generate_price_plot()

    # Add annotation to temperature prices plot
    fig_temperature.add_annotation(
        x=0.5,
        y=-0.2,
        xref="paper",
        yref="paper",
        text="Source: <a href='https://data.giss.nasa.gov/gistemp/' target='_blank'>nasa.gov</a>",
        showarrow=False,
        font=dict(size=10)
    )

    # Add annotation to house prices plot
    fig_price.add_annotation(
        x=0.5,
        y=-0.2,
        xref="paper",
        yref="paper",
        text="Source: <a href='https://dqydj.com/historical-home-prices/' target='_blank'>dqydj.com</a>",
        showarrow=False,
        font=dict(size=10)
    )

    # Convert the plotly figures to HTML strings
    plot_html_temperature = fig_temperature.to_html(include_plotlyjs='cdn', full_html=False)
    plot_html_price = fig_price.to_html(include_plotlyjs='cdn', full_html=False)

    # Write the HTML strings to a file
    with open("../docs/index.html", "w") as file:
        file.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>DataDebunk.xyz</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
                }}
                .container {{
                    max-width: 50%;
                    margin-right: auto;
                    text-align: left;
                }}
                .container p {{
                    text-align: left;
                }}
                .center {{
                    text-align: center;
                }}
                .bmc-button-container {{
                    display: flex;
                    justify-content: center;
                    width: 100%;
                }}
            </style>
        </head>
        <body>
            <h1>DataDebunk.xyz</h1>
            <div class="container">
                <p>Welcome to DataDebunk.xyz! I'm <a href="https://adamking.net" target="_blank">Adam King</a>. 
                This website is a passion project and a learning opportunity for me. 
                It was born out of a common pattern I've noticed while watching and listening to the news. 
                Politicians, news agencies, and pundits often make claims based on an incomplete or naive 
                understanding of data, or in an attempt to mislead.</p>

                <p>In particular, there is a propensity for these individuals to compare only two data 
                points without providing context or information on variance. This approach can lead to 
                erroneous conclusions. As Donald J. Wheeler puts it in his book, <em>Understanding 
                Variation: the Key to Managing Chaos</em>, such comparisons are "limited because of the amount 
                of data used, ..., and weak because both of the numbers are subject to variation."</p>

                <p>The code behind these analyses is completely open-source. Feel free to explore it on 
                <a href="https://github.com/adamkingdotnet/datadebunk.xyz" target="_blank">my GitHub</a>. 
                I'll be updating the data on this site on a yearly basis once all the available data sets 
                have been updated.</p>
            </div>
            <br>
            <br>
            <br>
            <br>
            <h2>Average Global Temperature</h2>
            {plot_html_temperature}
            <p>The latest change is {"an" if latest_sign_temperature == "increase" else "a"} {latest_sign_temperature} and it is {latest_significance_temperature} compared to last year.</p>
            <br>
            <br>
            <br>
            <br>
            <h2>Average Home Prices, United States</h2>
            <h3>Adjusted for Inflation</h3>
            {plot_html_price}
            <p>The latest change is {"an" if latest_sign_price == "increase" else "a"} {latest_sign_price} and it is {latest_significance_price} compared to last year.</p>
            <br>
            <br>
            <hr>
            <div class="center">
                <br>
                <br>
                <p>
                If you found this website helpful, I would appreciate your support.
                </p>
                <div class="bmc-button-container">
                    <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="adamking" data-color="#BD5FFF" data-emoji=""  data-font="Inter" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>
                </div>
            </div>
            <br>
            <br>
            <br>
            <br>
        </body>
        </html>
        """)


if __name__ == "__main__":
    generate_html()
