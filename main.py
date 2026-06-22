from fastapi import FastAPI
import random

app = FastAPI()  # Вот эта строка создает объект "app"

quotes = [
    "Дорогу осилит идущий.",
    "Программирование — это искусство.",
    "Код должен быть чистым, как слеза младенца."
     "Лучший код — тот, который не нужно писать."
]

@app.get("/")
def read_root():
    return {"message": "Привет! Это мой тестовый сервер."}

@app.get("/quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}