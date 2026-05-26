# Weather_app
Weather Analysis &amp; Visualization System is a Python-based desktop application that provides real-time and multi-day weather insights using a clean graphical user interface built with Tkinter. It integrates live API data, data visualization, voice feedback, file export, and statistical analysis into one unified tool.


# Weather Application (Tkinter + OpenWeather API)

This project is a desktop Weather Application built during my first semester.  
It uses **Tkinter** for the GUI and the **OpenWeatherMap API** to fetch real-time weather data.  
The app can display:
- Current weather of a city  
- Comparison of weather between two cities  
- Three-day weather variation  
- Data visualization using Matplotlib  
- Saving weather data to CSV  
- Optional text-to-speech announcements  

---

## 🚀 Features

### ✅ Current Weather
- Fetch temperature, pressure, humidity, wind speed, sunrise & sunset.
- Display detailed weather info in a clean format.
- Convert UNIX timestamps to readable GMT.

### ✅ Compare Two Cities
- Bar graph comparison (temperature, humidity, pressure, etc.)
- Shows difference between parameters with correct units.
- Voice output using SAPI voice.

### ✅ 3-Day Weather Visualization
- Line graph of selected parameter for 3-day forecast.
- Animated graph (optional feature).

### ✅ Save Weather Data
- Save the comparison data to **CSV, TXT, XLSX** using file dialog.

### ✅ GUI
- Built fully using Tkinter windows & widgets.

---

## 🏗 Project Structure

-
  --app.py
  --weather_ui.py
  --three_day_ui.py	
  --three_day_data.py
  --current_weather_api.py
  --table_formatter.py
  --plot_utils.py	
  --file_export.py	
  --table_ui.py	
  --param_difference.py	
  --unit_utils.py	
  --voice_output.py	
  --graph_animation.py
  --param_summary.py	
  --time_utils.py

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
pip install -r requirements.txt
python main.py
```

🧰 API Used
OpenWeatherMap APIs:

Current Weather
https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY



