
from fastapi import FastAPI, Query
import llm_service

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
        return None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/weather")
def read_weather(city: str = Query(...,min_length=1)):
    weather = get_weather(city)

    if weather is None:
        return{
            "success": False,
            "message": "城市不存在或暂无数据。"
        }
    
    advice = llm_service.generate_advice(city, weather)

    return {
        "success": True,
        "data": {
            "city": city,
            "weather": weather,
            "advice": advice
        }
    }