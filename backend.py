import requests


def get_data(place, days, condition):
    api = "19b04692cac7c78d7c9c2a6612da14e0"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    response = requests.get(url)
    data = response.json()
    filtered = data["list"][:(8 * days)]
    # return data.keys()

    if condition == "Temperature":
        filtered = [i["main"]["temp"] for i in filtered]
    else:
        filtered = [i["weather"][0]["main"] for i in filtered]
    return filtered


if __name__ == "__main__":
    print(get_data("Tokyo", 4, "Sky"))
