# Class - 32

## Today's Topic
- Mini Project – API-based app (weather/news)

## Notes

### Mini Project: Weather API Requester
Demonstrating how to request mock API data or real internet data using standard library `urllib` or third-party `requests`.

```python
import json
import urllib.request

def get_weather():
    # Free Mock / Open API URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&current_weather=true"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            temp = data["current_weather"]["temperature"]
            wind = data["current_weather"]["windspeed"]
            print(f"Weather in Dhaka, Bangladesh:")
            print(f"Temperature: {temp}°C")
            print(f"Wind Speed: {wind} km/h")
    except Exception as e:
        print("Failed to fetch weather data:", e)

if __name__ == "__main__":
    get_weather()
```
