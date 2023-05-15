import requests
from google.cloud import translate_v2 as translate
translate_client = translate.Client()


def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    response = requests.get(base_url, params=params)
    return response.json()

def translate_weather_data(weather_data):
    translation = translate_client.translate(weather_data, target_language="my")
    translated_text = translation["translatedText"]
    return translated_text

def main():
    api_key = "YOUR_WEATHER_API_KEY"
    city = "Yangon,MM"
    weather_data = get_weather_data(api_key, city)
    translated_weather = translate_weather_data(weather_data)
    print(translated_weather)

if __name__ == "__main__":
    main()