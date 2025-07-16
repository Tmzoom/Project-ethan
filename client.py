from openai import OpenAI

client = OpenAI(
    api_key="api key here",  # Consider using environment variables for security
    base_url="https://api.deepseek.com/v1"  # Added /v1 to the base URL
)

response = client.chat.completions.create(
    model="deepseek-chat",  # Corrected model name (removed space and updated to valid name)
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)