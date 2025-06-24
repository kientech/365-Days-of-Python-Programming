# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 12

# Weather App from a public API
# This script requires the 'requests' library: pip install requests
# You also need a free API key from OpenWeatherMap: https://openweathermap.org/appid
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        weather_data = response.json()
        
        # Extract and display relevant information
        main = weather_data['main']
        weather = weather_data['weather'][0]
        
        print(f"Weather in {weather_data['name']}:")
        print(f"  - Temperature: {main['temp']}°C")
        print(f"  - Feels like: {main['feels_like']}°C")
        print(f"  - Description: {weather['description'].capitalize()}")
        print(f"  - Humidity: {main['humidity']}%")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError:
        print("Error: Could not parse weather data. The city might not be found or the API response changed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Example Usage ---
# IMPORTANT: Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key.
API_KEY = "YOUR_API_KEY" 
city_name = "Hanoi"

if API_KEY == "YOUR_API_KEY":
    print("Please replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key.")
else:
    get_weather(API_KEY, city_name) 