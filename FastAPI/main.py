from abc import ABC, abstractmethod
from fastapi import FastAPI
import random

app = FastAPI()

class DiceGame(ABC):
    @abstractmethod
    def roll_dice(self):
        pass

    def play(self):
        result = self.roll_dice()
        return result

class WarDiceGame(DiceGame):
    def roll_dice(self):
        return random.randint(1, 6)

@app.get("/")
def play_war_dice_game():
    game = WarDiceGame()
    result = game.play()
    return {"result": result}
