from fastapi import FastAPI
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

main_prompt = '' # A placeholder variable to store the main prompt

@app.get("/get_response")
async def get_response(prompt:str):
    """
    GET request to retrieve a response based on the current prompt.
    """
    global main_prompt
    main_prompt = prompt

    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": main_prompt}
                    ]
                    )
    return {response.choices[0].message.content}


@app.post("/set_prompt")
async def set_prompt(change_prompt:str):
    """
    POST request to set a new prompt for generating responses.
    """
    updated_response=openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f'{main_prompt + change_prompt}' }
                    ]
                    )
    
    return {updated_response.choices[0].message.content}
