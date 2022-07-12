import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/roll-dice")
async def roll_dice():
    """A super fast random Dice Roller"""
    return {'num': random.randint(1, 6)}
