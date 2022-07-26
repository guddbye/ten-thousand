from collections import Counter
import random

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def get_random_number(self):
        return random.randint(1,6)
    def calculate_score(roll):
        banked_score = tuple(roll)
        if banked_score == (1,):
            return 100
        elif banked_score == (1,1):
            return 200

    @staticmethod
    def roll_dice(dice):
        roll = []
        for i in range(dice):
            roll.append(random.randint(0,6))
            return tuple(roll)