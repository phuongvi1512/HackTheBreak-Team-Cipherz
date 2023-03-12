from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Define the path to the CSV file
CSV_PATH = 'unemployment_rates.csv'

# Read the CSV file into a Pandas dataframe
df = pd.read_csv(CSV_PATH)

@app.route('/')
def index():
    # Get the list of available countries
    countries = df['countries'].unique()

    return render_template('index.html', countries=countries)

@app.route('/chart')
def chart():
    # Get the list of selected countries from the form
    selected_countries = request.args.getlist('country')

    # Filter the dataframe to only include the selected countries
    filtered_df = df[df['countries'].isin(selected_countries)]

    # Group the data by country and compute the average unemployment rate
    avg_unemployment_rates = filtered_df.groupby('countries').mean().reset_index()

    # Convert the data to a list of dictionaries
    data = avg_unemployment_rates.to_dict('records')

    return render_template('chart.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)