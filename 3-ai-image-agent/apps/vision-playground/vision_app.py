import gradio as gr
import os
from ollama import chat

def analyze_image(prompt, image_path):
    if image_path is None or not os.path.exists(image_path):
        return "Please upload a valid image."

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
    return response['message']['content']

gr.Interface(
    fn=analyze_image,
    inputs=[
        gr.Textbox(label="Prompt", placeholder="What's happening in this image?"),
        gr.Image(type="filepath", label="Upload Image")
    ],
    outputs="text",
    title="Gemma4 Vision Model (Local via Ollama)",
    theme="default"
).launch()
