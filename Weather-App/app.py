import requests
from flask import Flask, request, render_template
from config import API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        weather = None

    return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
