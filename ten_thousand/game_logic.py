import random
from collections import Counter

class Banker:
    score = 0

    def __init__(self):
        pass

    @staticmethod
    def add_to_score(points):
        Banker.score = Banker.score + points

    @staticmethod
    def get_score():
        return Banker.score

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def dice_shelf(num_str):
        dice = list(num_str)
        return tuple(dice)

    @staticmethod
    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))
        return tuple(rolls)

    @staticmethod
    def calculate_score(tup):
        score = 0
        str_list = list(tup)
        nums = [int(num) for num in str_list]
        roll = Counter(nums).most_common()

        if len(tup) == 0:
            return score

        # straight
        if len(roll) == 6:
            return 1500

        #6 of a kind
        if roll[0][1] == 6:
            if roll[0][0] == 1:
                return 4000
            return int(roll[0][0]) * 400

        #5 of a kind
        if roll[0][1] == 5:
            if len(roll) == 2:
                if roll[1][0] == 5:
                    score += 50

                if roll[1][0] == 1:
                    score += 100

            if roll[0][0] == 1:
                return score + 3000

            score += int(roll[0][0]) * 300
            return score

        #4 of a kind
        if roll[0][1] == 4:
            if len(roll) >= 2:
                if roll[1][0] == 5:
                    score += 50 * roll[1][1]

                if roll[1][0] == 1:
                    score += 100 * roll[1][1]

            if len(roll) == 3:
                if roll[2][0] == 5:
                    score += 50 * roll[2][1]

                if roll[2][0] == 1:
                    score += 100 * roll[2][1]

            if roll[0][0] == 1:
                return score + 2000

            score += int(roll[0][0]) * 200
            return score

        # double 3 of a kind
        if len(roll) == 2:
            if roll[0][1] == 3 and roll[1][1] == 3:
                if roll[0][0] == 1:
                    score += 1000
                    return score + roll[1][0] * 100

                if roll[1][0] == 1:
                    score += 1000
                    return score + roll[0][0] * 100

                return roll[0][0] * 100 + roll[1][0] * 100

        # 3 of a kind
        if roll[0][1] == 3:
            if len(roll) >= 2:
                if roll[1][0] == 5:
                    score += 50 * roll[1][1]

                if roll[1][0] == 1:
                    score += 100 * roll[1][1]

            if len(roll) >= 3:
                if roll[2][0] == 5:
                    score += 50 * roll[2][1]

                if roll[2][0] == 1:
                    score += 100 * roll[2][1]

            if len(roll) == 4:
                if roll[3][0] == 5:
                    score += 50 * roll[3][1]

                if roll[3][0] == 1:
                    score += 100 * roll[3][1]

            if roll[0][0] == 1:
                return score + 1000

            score += int(roll[0][0]) * 100
            return score

        # 3 pairs
        if len(roll) > 2:
            if roll[0][1] and roll[1][1] and roll[2][1] == 2:
                score += 1500
                return score

        # handle single 1's and 5's
        one_counter = 0
        five_counter = 0
        for num in nums:
            if num == 1:
                one_counter += 1
            if num == 5:
                five_counter += 1
        score += one_counter * 100
        score += five_counter * 50

        # default/catch all return
        return score