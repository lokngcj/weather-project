
def get_city_input():
    while True:
        city = input("请输入城市名称: ").strip()
        if city == "":
            print("输入不能为空，请重新输入。")
        else:
            return city

def print_city(city):
    print(f"你查询的城市是: {city}")

def main():
    city = get_city_input()
    print_city(city)

if __name__ == "__main__":
    main()
