
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
    
# 本质就是：字符串匹配→判断问题类型
def is_weather_query(query:str) -> bool:
    keywords = ["天气", "穿", "温度", "热", "冷", "带伞"]
    
    for word in keywords:
        if word in query:
            return True
    return False

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

@app.get("/chat") # LLM→提取城市→调用工具→生成建议（可控可拓展，但是存在多次调用的情况）——Tool-based（工程派）
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

@app.get("/smart_chat") # LLM一次完成所有逻辑（简洁、成本低，但是可控性弱）——Prompt-based（智能派）
def smart_chat(query:str = Query(...,min_length=1)):
    result = llm_service.smart_weather_assistant(query)
    return {
        "success": True,
        "data": {
            "query": query,
            "answer": result
        }
    }

@app.get("/chat_router")
def chat_router(query:str = Query(...,min_length=1)):
    
    if is_weather_query(query):
        mode = "tool"

        city = llm_service.extract_city(query)
        if city == "unknown":
            return {
                "success": False,
                "mode": mode,
                "message": "无法识别城市，请提供更明确的信息。"
            }
        weather = get_weather(city)
        if weather is None:
            return {
                "success": False,
                "mode": mode,
                "message": "城市不存在或暂无数据。"
            }
        advice = llm_service.generate_advice(city, weather)
        return {
            "success": True,
            "mode": mode,
            "data": {
                "city": city,
                "weather": weather,
                "advice": advice
            }
        }
    else:
        mode = "smart"
        result = llm_service.smart_weather_assistant(query)
        return {
            "success": True,
            "mode": mode,
            "data": {
                "query": query,
                "answer": result
            }
        }