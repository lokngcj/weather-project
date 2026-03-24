from fastapi import FastAPI

app = FastAPI()

def get_weather(city):
    weather_data = {
        "beijing": "晴朗，温度25°C",
        "shanghai": "多云，温度28°C",
        "guangzhou": "雨天，温度30°C",
        "shenzhen": "晴朗，温度27°C"
    }
    city_key = city.lower()

    if city_key in weather_data:
        return weather_data[city_key]
    else:
        return "暂无该城市的天气信息。"
    
@app.get("/weather")
def read_weather(city: str):
    weather = get_weather(city)
    return {
        "city": city, 
        "weather": weather
        }