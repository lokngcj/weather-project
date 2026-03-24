import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

def generate_advice(city,weather):
    prompt = f"""
你是一个专业的生活助手。

已知信息：
城市: {city}
天气: {weather}

要求：
1、只输出一句话
2、必须包含穿衣建议
3、不要编造天气信息
4、不要超过30字

请给出建议：。
"""
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt},
    ],
    stream=False
)
    # response = client.responses.create(
    #     model = "gpt-5-mini",
    #     input = prompt,
    # )
    return response.choices[0].message.content

if __name__ == "__main__":
    city = "北京"
    weather = "晴朗，温度25°C"
    advice = generate_advice(city, weather)
    print(f"穿衣建议: {advice}")