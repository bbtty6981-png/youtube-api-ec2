
from fastapi import FastAPI
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/channel")
def get_channel(id: str):
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.channels().list(part="snippet,statistics", id=id)
    response = request.execute()
    return response

