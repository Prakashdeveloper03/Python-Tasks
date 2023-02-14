import requests


def get_weather(api_key: str, city_name: str) -> None:
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        fetch_details(response, city_name)
    else:
        print("Request failed!\nCheck your API key, City name and Internet connection.")


def fetch_details(response, city_name):
    data = response.json()
    main = data["main"]
    temperature = main["temp"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    report = data["weather"]
    print(f"{city_name:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")


if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    city_name = input("Enter the city : ").capitalize()
    get_weather(api_key, city_name)
