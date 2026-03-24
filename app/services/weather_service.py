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