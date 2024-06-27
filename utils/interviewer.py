
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

def get_question(arg1,arg2):
  prompt = ""
  if(arg1 == "starting"):
    prompt = f"please start a interview stimulating a real interview with really important interview questions  for a job profile  {arg2["jobProfile"]} in {arg2["company"]} interview should be {arg2["duration"]} long and my resume is {str(arg2["resume"])} ask one question . "
  
  elif(arg1 == "continue"):
    prompt = f"my ans is {arg2} please ask next question don't forget the time limit. if time hits the limit please a text that says 'Ending this interview' so that my program could understand that resume is over"

  elif(arg1 == "ending"):
    prompt = "Provide me a deep analysis for all the questions asked."

  response = chat_session.send_message(prompt)

  final_response = response.text.replace("*", "").replace("#", "")
  return final_response

