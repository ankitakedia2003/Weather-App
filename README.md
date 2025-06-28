# 🌦️ Weather Forecast App

An interactive **Weather Forecast Web App** built using **Python** and **Streamlit**, fetching real-time weather data from the **OpenWeatherMap API**. The app allows users to check the current weather, a short-term forecast, and even fetch weather based on IP-based geolocation.

> Built to explore real-time APIs, geolocation, and clean UI development with Streamlit and Python.

---

## 🚀 Features

- 🔍 View **current weather** for any city
- 📅 Get **5-point weather forecast** (next intervals)
- 📍 **Auto-detect your location** using IP and show local weather
- 🎨 Clean layout with HTML/CSS integration via `st.markdown`
- ⚠️ Handles API errors (invalid keys, city not found, etc.)

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit + HTML/CSS (via `st.markdown`)
- **Backend**: Python
- **APIs**:
  - [OpenWeatherMap](https://openweathermap.org/api)
  - [Geocoder](https://geocoder.readthedocs.io/)
- **Packages**:
  - `streamlit`
  - `requests`
  - `datetime`
  - `geocoder`

---

## 📁 Project Structure
```
Weather-App/
├── Img.jpg # App image or background
├── weather_app.py # Main Streamlit script
├── requirements.txt # All required Python packages
└── README.md # Project overview
```

---

## 📦 Installation & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/ankitakedia2003/Weather-App.git
cd Weather-App

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .streamlit/secrets.toml and add your API key
mkdir .streamlit
echo 'api_key = "your_openweather_api_key"' > .streamlit/secrets.toml

# 4. Run the app
streamlit run weather_app.py
```

## 🌐 Live Demo
[https://my-weather-app.streamlit.app/](https://my-weather-app.streamlit.app/)

## ✨ Future Enhancements

- Add charts for temperature trends
- Style using custom CSS/Streamlit themes
- Support more granular forecasts (hourly, weekly)
- Add background images based on weather

## 📬 Contact

Feel free to connect with me:  
🔗 [LinkedIn](https://www.linkedin.com/in/ankita-kedia-787343305)  
📧 kediaankita2003@gmail.com

---

🌈 Thank you for checking out this project!
