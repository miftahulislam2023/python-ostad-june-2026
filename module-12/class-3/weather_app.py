import urllib.request
import json

API_KEY = "cf9fb599cc3b4cc1b00162720261507"
city = "Melbourne"
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode("utf-8"))

print(f"Time Fetched: {data['current']['last_updated']}")
print(f"City: {data['location']['name']}, {data['location']['country']}")
print(f"Condition: {data['current']['condition']['text']}")
print(f"Temperature: {data['current']['temp_c']}°C")
print(f"Humidity: {data['current']['humidity']}%")

dummy_result = {
    "location": {
        "name": "Dhaka",
        "region": "",
        "country": "Bangladesh",
        "lat": 23.7231,
        "lon": 90.4086,
        "tz_id": "Asia/Dhaka",
        "localtime_epoch": 1788710095,
        "localtime": "2026-09-06 21:54"
    },
    "current": {
        "last_updated_epoch": 1788709500,
        "last_updated": "2026-09-06 21:45",
        "temp_c": 29.4,
        "temp_f": 85.0,
        "is_day": 0,
        "condition": {
            "text": "Partly Cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
            "code": 1003
        },
        "wind_mph": 8.1,
        "wind_kph": 13.0,
        "wind_degree": 188,
        "wind_dir": "S",
        "pressure_mb": 1009.0,
        "pressure_in": 29.78,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 71,
        "cloud": 30,
        "feelslike_c": 33.9,
        "feelslike_f": 93.0,
        "windchill_c": 29.4,
        "windchill_f": 85.0,
        "heatindex_c": 34.0,
        "heatindex_f": 93.1,
        "dewpoint_c": 23.7,
        "dewpoint_f": 74.6,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 0.0,
        "gust_mph": 13.6,
        "gust_kph": 22.0,
        "will_it_rain": 0,
        "chance_of_rain": 8,
        "will_it_snow": 0,
        "chance_of_snow": 0,
        "wetbulb_c": 25.2,
        "wetbulb_f": 77.4
    }
}