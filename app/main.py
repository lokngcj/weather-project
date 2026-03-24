import logging
from fastapi import FastAPI, Query
from app.services.weather_service import get_weather
from app.services import llm_service

# 配置日志格式和级别
logging.basicConfig(
# 表示显示INFO级别及以上的日志
    level=logging.INFO,
# 定义日志输出长什么样
    format='%(asctime)s - %(levelname)s - %(message)s',
)
# 创建当前文件的日志对象
logger = logging.getLogger(__name__)

app = FastAPI()


def is_weather_query(query: str) -> bool:
    keywords = ["天气", "穿", "带伞", "温度", "热", "冷"]

    for word in keywords:
        if word in query:
            return True

    return False


@app.get("/health")
def health_check():
    logger.info("health check called")
    return {"status": "ok"}


@app.get("/weather")
def read_weather(city: str = Query(..., min_length=1)):
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


@app.get("/chat")
def chat(query: str = Query(..., min_length=1)):
    city = llm_service.extract_city(query)

    if city == "unknown":
        return {
            "success": False,
            "message": "无法识别城市"
        }

    weather = get_weather(city)

    if weather is None:
        return {
            "success": False,
            "message": "城市不存在或暂无数据"
        }

    advice = llm_service.generate_advice(city, weather)

    return {
        "success": True,
        "data": {
            "query": query,
            "city": city,
            "weather": weather,
            "advice": advice
        }
    }


@app.get("/chat2")
def chat2(query: str = Query(..., min_length=1)):
    result = llm_service.smart_weather_assistant(query)

    return {
        "success": True,
        "data": {
            "query": query,
            "answer": result
        }
    }


@app.get("/chat_router")
def chat_router(query: str = Query(..., min_length=1)):
    logger.info(f"Received query: {query}")

    if is_weather_query(query):
        mode = "tool"
        logger.info(f"route mode selected: {mode}")

        city = llm_service.extract_city(query)
        logger.info(f"extracted city: {city}")

        if city == "unknown":
            logger.warning("city extraction failed")
            return {
                "success": False,
                "mode": mode,
                "message": "无法识别城市"
            }

        weather = get_weather(city)

        if weather is None:
            logger.warning(f"weather data not found for city: {city}")
            return {
                "success": False,
                "mode": mode,
                "message": "城市不存在或暂无数据"
            }

        advice = llm_service.generate_advice(city, weather)
        logger.info("tool mode response success")

        return {
            "success": True,
            "mode": mode,
            "data": {
                "query": query,
                "city": city,
                "weather": weather,
                "advice": advice
            }
        }

    else:
        mode = "fast"
        logger.info(f"route mode selected: {mode}")

        answer = llm_service.smart_weather_assistant(query)
        logger.info("fast mode response success")
        
        return {
            "success": True,
            "mode": mode,
            "data": {
                "query": query,
                "answer": answer
            }
        }