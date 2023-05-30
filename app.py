from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_summarizer.pipeline.prediction_pipeline import PredictionPipeline

text: str = "What is Text Summarization?"
app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    try:
        os.system("python3 main.py")
    except Exception as e:
        raise e


@app.post("/predict")
async def predict(text: str):
    try:
        pipeline = PredictionPipeline()
        result = pipeline.predict(text)
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0000000", port=8000)