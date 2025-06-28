import streamlit as st
import requests
from datetime import datetime
import geocoder

# API key and URL
API_KEY = st.secrets["api_key"]
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        st.error("City not found. Please enter a valid city name.")
    elif response.status_code == 401:
        st.error("Invalid API key. Please check your API key.")
    else:
        st.error("An error occurred. Please try again later.")
    return None

def get_forecast(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        st.error("City not found. Please enter a valid city name.")
    elif response.status_code == 401:
        st.error("Invalid API key. Please check your API key.")
    else:
        st.error("An error occurred. Please try again later.")
    return None

def get_weather_icon(icon_code):
    return f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

def main():
    st.title('Weather App')
    st.image("Img.jpg")
    city = st.text_input('Enter city name:')
    st.markdown("""
        <style>
        .info-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .info-box h2 {
            color: #007BFF;
            margin-bottom: 10px;
        }
        .info-box p {
            color: #555555;
            margin: 5px 0;
        }
        </style>
    """, unsafe_allow_html=True)


    if st.button('**Get Current Weather**'):
        if city:
            weather_data = get_weather(city)
            if weather_data:
                st.markdown("""
                <div class="info-box">
                    <h2>Weather Information</h2>
                    <p><strong>City:</strong> {name}</p>
                    <p><strong>Temperature:</strong> {temp} °C</p>
                    <p><strong>Weather:</strong> {weather}</p>
                    <p><strong>Humidity:</strong> {humidity}%</p>
                    <p><strong>Wind Speed:</strong> {wind_speed} m/s</p>
                    <p><strong>Sunrise:</strong> {sunrise}</p>
                    <p><strong>Sunset:</strong> {sunset}</p>
                    <p><strong>Visibility:</strong> {visibility} meters</p>
                </div>
            """.format(
                name=weather_data['name'],
                temp=weather_data['main']['temp'],
                weather=weather_data['weather'][0]['description'].title(),
                humidity=weather_data['main']['humidity'],
                wind_speed=weather_data['wind']['speed'],
                sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M:%S'),
                sunset = datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M:%S'),
                visibility = weather_data['visibility']
            ), unsafe_allow_html=True)
                
                icon_code = weather_data['weather'][0]['icon']
                icon_url = get_weather_icon(icon_code)
                st.image(icon_url)
            else:
                st.error('City not found, please try again.')

    if st.button('**Get Forecast**'):
        if city:
            forecast_data = get_forecast(city)
            if forecast_data:
                st.write(f"**Forecast for {city}:**")
                for item in forecast_data['list'][:5]:
                    dt = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
                    temp = item['main']['temp']
                    description = item['weather'][0]['description'].title()
                    st.markdown(f"""
                    <div class="info-box">
                        <p><strong>{dt}:</strong> {temp} °C, {description}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.error('Could not retrieve forecast, please try again.')
        else:
            st.error('Please enter a city name to get the forecast.')

    if st.button('**Get My Location Weather**'):
        g = geocoder.ip('me')
        if g.ok:
            city = g.city
            weather_data = get_weather(city)
            if weather_data:
            # Extract necessary data
                name = weather_data['name']
                temp = weather_data['main']['temp']
                weather = weather_data['weather'][0]['description'].title()
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M:%S')
                sunset = datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M:%S')
                visibility = weather_data['visibility']

            # Display the data in Streamlit using st.markdown
                st.markdown(f"""
                <div class="info-box">
                    <h2>Weather Information</h2>
                    <p><strong>City:</strong> {name}</p>
                    <p><strong>Temperature:</strong> {temp} °C</p>
                    <p><strong>Weather:</strong> {weather}</p>
                    <p><strong>Humidity:</strong> {humidity}%</p>
                    <p><strong>Wind Speed:</strong> {wind_speed} m/s</p>
                    <p><strong>Sunrise:</strong> {sunrise}</p>
                    <p><strong>Sunset:</strong> {sunset}</p>
                    <p><strong>Visibility:</strong> {visibility} meters</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error('City not found, please try again.')
        else:
            st.error('Could not retrieve your location. Please try again.')
if __name__ == '__main__':
    main()
