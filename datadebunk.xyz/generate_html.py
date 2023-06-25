# File: generate_html.py

from temperature_data import generate_temperature_plot
from house_prices import generate_price_plot
from crime_data import generate_crime_plot



def generate_html():
    fig_temperature, latest_sign_temperature, latest_significance_temperature = generate_temperature_plot()
    fig_price, latest_sign_price, latest_significance_price = generate_price_plot()
    fig_crime, latest_sign_crime, latest_significance_crime = generate_crime_plot()

    # Convert the plotly figures to HTML strings
    plot_html_temperature = fig_temperature.to_html(include_plotlyjs='cdn', full_html=False)
    plot_html_price = fig_price.to_html(include_plotlyjs='cdn', full_html=False)
    plot_html_crime = fig_crime.to_html(include_plotlyjs='cdn', full_html=False)

    # Write the HTML strings to a file
    with open("../docs/index.html", "w") as file:
        file.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>DataDebunk.xyz</title>
            <meta property="og:title" content="DataDebunk.xyz by Adam King">
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
                .toc {{
                    padding: 20px;
                    background-color: #f0f0f0;
                    border: 1px solid #ddd;
                    max-width: 33%;
                    text-align: left;
                }}
                .toc ul {{
                    list-style-type: none;
                    margin: 0;
                    padding: 0;
                }}
                .toc ul li {{
                    margin: 5px 0;
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
                erroneous conclusions. As Donald J. Wheeler puts it in his book, <em><a target="_blank" 
                href="https://www.amazon.com/Understanding-Variation-Key-Managing-Chaos/dp/0945320531/ref=sr_1_1?crid=XZO7ENO0700L&amp;keywords=understanding+variation&amp;qid=1687715542&amp;sprefix=understanding+variation%252Caps%252C136&amp;sr=8-1&_encoding=UTF8&tag=atomking-20&linkCode=ur2&linkId=c441eb07106620e15f4cc7112bec1bbf&camp=1789&creative=9325">Understanding Variation</a>:
                The Key to Managing Chaos</em>, such comparisons are "limited because of the amount 
                of data used, ..., and weak because both of the numbers are subject to variation."</p>

                <p>The code behind these analyses is completely open-source. Feel free to explore it on 
                <a href="https://github.com/adamkingdotnet/datadebunk.xyz" target="_blank">my GitHub</a>. 
                I'll be updating the data on this site on a yearly basis once all the available data sets 
                have been updated.</p>
            </div>
            <br>
            <br>
            <div class="toc">
                <h2>Vizualizations</h2>
                <ul>
                    <li><a href="#temperature">Average Global Temperature</a></li>
                    <li><a href="#house-prices">Average Home Prices, United States</a></li>
                    <li><a href="#crime-incidents">Crime Incidents per Capita, United States</a></li>
                </ul>
            </div>
            <br>
            <br>
            <br>
            <br>
            <h2 id="temperature">Average Global Temperature</h2>
            {plot_html_temperature}
            <br>
            <br>
            <br>
            <br>
            <h2 id="house-prices">Average Home Prices, United States</h2>
            <h3>Adjusted for Inflation</h3>
            {plot_html_price}
            <br>
            <br>
            <br>
            <br>
            <h2 id="crime-incidents">Crime Incidents per Capita, United States</h2>
            {plot_html_crime}
            <br>
            <br>
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
