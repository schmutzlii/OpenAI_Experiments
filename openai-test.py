import os
import base64
import time
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""
client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_chart(chart_path):
    base64_image = encode_image(chart_path)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user", 
                "content": "What can you see describe the picture",
            },
            {
                "role": "user",
                "content": f"data:image/jpeg;base64,{base64_image}"
            }
        ]
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    chart_filename = "test.PNG"
    analysis = analyze_chart(chart_filename)
    print(analysis)
