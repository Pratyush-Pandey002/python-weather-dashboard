Live Weather Dashboard
This is a simple command-line application built with Python that fetches and displays live weather data for any city entered by the user. The project serves as a practical example of working with third-party APIs and handling JSON data.

Features
Live Data: Fetches up-to-the-minute weather information from a REST API.

User-Friendly CLI: Prompts the user for a city and provides clear output.

Structured Output: Displays key metrics like temperature, humidity, and wind speed in a readable format.

Technologies
Python: The core language for the application logic.

requests library: Used to make HTTP requests to the weather API.

How to Run the Code
Get an API Key:
You will need a free API key from a weather service like OpenWeatherMap. After signing up, copy your API key.

Replace the Placeholder:
Open the weather_dashboard.py file and replace the placeholder API key with your own.

API_KEY = "YOUR_API_KEY_GOES_HERE"

Install Dependencies:
This project requires the requests library. Install it using pip in your terminal or PyCharm:

pip install requests

Run the Script:
Execute the Python file from your terminal:

python weather_dashboard.py

Example Output
Here is what the dashboard looks like in action:

Enter a city name to get the weather forecast: Paris
Weather in Paris, France:
Temperature: 15.1°C
Humidity: 87%
Wind Speed: 5.14 m/s
Description: overcast clouds
