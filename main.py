
def get_city_input():
    while True:
        city = input("请输入城市名称: ").strip()
        if city == "":
            print("输入不能为空，请重新输入。")
        else:
            return city

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

def print_weather(city,weather):
    print(f"{city}的天气是: {weather}")

def main():
    city = get_city_input()
    weather = get_weather(city)
    print_weather(city, weather)

if __name__ == "__main__":
    main()
