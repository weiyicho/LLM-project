import cv2
import speech_recognition as sr

import torch
import requests


import json
def chat(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llava:7b", "prompt": prompt, "stream": True},
        stream=True
    )
    full_response = ""
    for line in response.iter_lines():
        if line:
            try:
                decoded = line.decode("utf-8")
                data = json.loads(decoded)
                text = data.get("response", "")
                print(text, end="", flush=True)
                full_response += text
            except Exception as e:
                print("Streaming error:", e)

    print()  # newline at end
    return full_response