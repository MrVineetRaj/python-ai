
import os
from dotenv import load_dotenv
load_dotenv() 


import google.generativeai as genai


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

def get_response(message):
  prompt = f"For this project you are virtual assistant named as jarvis skills in general tasks like alex and google assistant so give me response to {message} in short"
  response = chat_session.send_message(prompt)

  final_response = response.text.replace("*", "").replace("#", "")
  return final_response

