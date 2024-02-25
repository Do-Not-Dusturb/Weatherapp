import requests

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

        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Weather description: {description}")
    else:
        print("City not found")
API_KEY = "3ccb53d4c43819a246d23fa0381a146b"
city_name = input("Enter city name: ")

get_weather(API_KEY, city_name)
