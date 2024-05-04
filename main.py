from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
from genai_assistant import GenAI_Assistant
app = FastAPI()
genai = GenAI_Assistant()


class Prompt(BaseModel):
    prompt: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/submit-feelings")
async def send_prompt(prompt: Prompt):
    response = genai.generate_response(prompt.prompt)
    return response
