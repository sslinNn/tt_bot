import json
import requests



def getLocationFromCoordinates(TOKEN: str, latitude: float, longitude: float):
    location_from_coordinates = f"https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={TOKEN}"
    response = requests.get(url=location_from_coordinates).text
    location_res = json.loads(response)
    return location_res['address']['city']


if __name__ == '__main__':
    print(getLocationFromCoordinates(TOKEN="...", latitude=50.43477, longitude=30.53375))