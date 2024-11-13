from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
from utils.mainchat import base_chat  # 导入 base_chat 函数
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# 添加CORS支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str
    history: list = []  # 添加 history 字段

@app.post("/chat")
async def chat(chat_message: ChatMessage):
    response, history = await base_chat(chat_message.message, chat_message.history)
    return {"response": response, "history": history}
