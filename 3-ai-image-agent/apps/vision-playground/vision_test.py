from ollama import chat

image_path = 'example.jpg'
prompt = "What's happening in this image?"

response = chat(
    model="gemma4:latest",
    messages=[
        {
            'role': 'user',
            'content': prompt,
            'images': [image_path],
        }
    ]
)

print(response['message']['content'])
