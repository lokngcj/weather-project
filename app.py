
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

@app.get("/chat")
def chat(query:str = Query(...,min_length=1)):
    city = llm_service.extract_city(query)
    if city == "unknown":
        return {
            "success": False,
            "message": "无法识别城市，请提供更明确的信息。"
        }
    # 下面的代码只会返回null，因为python不会自动把“子函数的返回值”继续往外传
    # read_weather(city) 
    # 因此必须明确写明如下代码：但是这样写依旧不符合规范。
    # return read_weather(city)
    # 因为read_weather函数的职责是“获取天气信息”，而不是“获取天气信息并返回给用户”。
    # 因此应该把获取天气信息的代码单独抽离出来，放在一个新的函数里，
    # 比如叫build_weather_response(city:str)，然后在read_weather里调用build_weather_response(city)，在chat里也调用build_weather_response(city)。
    # 这样才符合单一职责原则。

    weather = get_weather(city)

    if weather is None:
        return {
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