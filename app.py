from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        feels_like = main_data["feels_like"]
        description = data["weather"][0]["description"]

        return {
            "temperature": temperature,
            "feels_like": feels_like,
            "description": description
        }
    else:
        return {"error": "City not found"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        API_KEY = "3ccb53d4c43819a246d23fa0381a146b"  
        weather_data = get_weather(API_KEY, city)
        return render_template('index.html', weather=weather_data, city=city)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
