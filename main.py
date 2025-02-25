import os
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Load OpenAI API Key from Render environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

class GoalRequest(BaseModel):
    goal: str

@app.get("/")
def home():
    return {"message": "AI Execution Planner is Ready!"}

@app.post("/plan/")
def generate_plan(request: GoalRequest):
    """
    Generates an execution plan using GPT-4.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant helping with structured execution planning."},
                {"role": "user", "content": f"Create a structured execution plan to achieve this goal: {request.goal}"}
            ]
        )
        return {"plan": response["choices"][0]["message"]["content"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

