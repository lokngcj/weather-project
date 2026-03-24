
def get_city_input():
    city = input("Enter the city name: ")
    return city

def print_city(city):
    print(f"你查询的城市是: {city}")

def main():
    city = get_city_input()
    print_city(city)

if __name__ == "__main__":
    main()
