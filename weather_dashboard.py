import requests
import json
import os

# --- Configuration ---
# You need a free API key from a weather service like OpenWeatherMap.
# Get your API key and paste it here.
# For example, you can get one from https://openweathermap.org/api
API_KEY = "715e916394829851c168a780f427b5c1"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name: str) -> dict:
    """
    Fetches weather data for a given city from the API.

    Args:
        city_name (str): The name of the city to get weather for.

    Returns:
        dict: A dictionary containing the weather data if successful, otherwise None.
    """
    print(f"Fetching weather data for '{city_name}'...")
    
    # Check if the API key has been replaced.
    if API_KEY == "Other":
        print("Error: Please replace 'Other' with your actual API key.")
        return None

    # Construct the full API URL with the city name and API key.
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit 'metric' for Celcius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        
        # Raise an HTTPError if the response status code is 4xx or 5xx.
        response.raise_for_status()

        # Parse the JSON response.
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as err_http:
        # Handle HTTP-specific errors, like city not found (404).
        print(f"HTTP Error: {err_http}")
        if response.status_code == 404:
            print("Error: City not found. Please check the spelling.")
        return None
    except requests.exceptions.RequestException as err:
        # Handle other request-related errors.
        print(f"An error occurred: {err}")
        return None

def display_weather_info(data: dict):
    """
    Displays the extracted weather information in a user-friendly format.

    Args:
        data (dict): The dictionary containing the weather data.
    """
    if data:
        # Extract relevant information from the JSON data.
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Print the information to the console.
        print("\n--- Current Weather Dashboard ---")
        print(f"Location: {city}, {country}")
        print(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
        print(f"Condition: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("---------------------------------")
    else:
        print("Failed to retrieve weather data. Please try again.")

def main():
    """
    Main function to run the weather dashboard script.
    """
    # Prompt the user for a city name.
    city_name = input("Enter a city name to get the weather forecast: ")

    # Check for empty input.
    if not city_name.strip():
        print("City name cannot be empty.")
        return

    # Fetch and display the weather data.
    weather_data = get_weather_data(city_name)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
