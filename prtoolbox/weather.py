import requests

def weather_at_lewagon():

    url = "https://www.metaweather.com/api/location/44418/"
    response = requests.get(url).json()
    weather = response["consolidated_weather"][0]["weather_state_name"]

    return f'The weather at Le Wagon today is: {weather}'


if __name__ == "__main__":
    print(weather_at_lewagon())
