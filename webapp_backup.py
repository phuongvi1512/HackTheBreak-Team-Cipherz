from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search_2.html')

@app.route('/search', methods=['POST'])
def search():
    # Get selected countries from request body
    data = request.get_json()
    selected_countries = data['countries']

    # Read unemployment rates from CSV file
    with open('unemployment_rates.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader) # skip headers
        unemployment_rates = {}
        for row in reader:
            if row[0] in selected_countries:
                unemployment_rates[row[0]] = float(row[1])

    # Prepare data for bar chart
    countries = []
    rates = []
    for country, rate in unemployment_rates.items():
        countries.append(country)
        rates.append(rate)

    return jsonify({
        'countries': countries,
        'unemploymentRates': rates
    })

if __name__ == '__main__':
    app.run(debug=True)