from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        zip_code = request.form['zip_code']
        term = request.form['term']
        restaurants = get_restaurants(zip_code, term)
        return render_template('index.html', restaurants=restaurants)
    return render_template('index.html')

def get_restaurants(zip_code, term):
    api_url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY"
    }
    params = {
        "term": term,
        "location": zip_code,
        "categories": "restaurants",
        "limit": 5
    }
    response = requests.get(api_url, headers=headers, params=params)
    print(response.status_code)
    print(response.json())
    if response.status_code == 200:
        return response.json().get('businesses', [])
    return []

if __name__ == '__main__':
    app.run(debug=True)
