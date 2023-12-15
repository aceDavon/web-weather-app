from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from configure_logging import configure_logging

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = 'abuja'

    weather = get_current_weather(city)

    if not weather['cod'] == 200:
        return render_template('not_found.html', city=city)

    if weather:
        return render_template('weather.html', title=weather['name'], temp=f"{weather['main']['temp']:.1f}", feels_like=f"{weather['main']['feels_like']:.1f}", description=f"{weather['weather'][0]['description']}")
    else:
        return render_template('weather.html', title="Error", temp="N/A", feels_like="N/A")


if __name__ == '__main__':
    configure_logging()
    try:
        serve(app, host='localhost', port=8000)
    except Exception as e:
        print(f"An error occurred: {e}")
