from random import randint
from collections import Counter


class GameLogic:
    def __init__(self):
        self.head = None

    @staticmethod
    def calculate_score(dice_roll):
        # dice_roll is a tuple
        score = 0
        roll = Counter(dice_roll).most_common()

        if len(dice_roll) == 0:
            return score

        # straight
        if len(roll) == 6:
            return 1500

        # 3 pairs
        if len(roll) > 2:
            if roll[0][1] == 2 and roll[1][1] == 2 and roll[2][1] == 2:
                score += 1500
                return score

        # 2 sets of 3
        if len(roll) == 2:
            if roll[0][1] == 3 and roll[1][1] == 3:
                score += 1200
                return score

        for num in roll:
            # Score cases for 1
            if num[0] == 1:
                if num[1] == 1:
                    score += 100
                if num[1] == 2:
                    score += 200
                if num[1] == 3:
                    score += 1000
                if num[1] == 4:
                    score += 2000
                if num[1] == 5:
                    score += 3000
                if num[1] == 6:
                    score += 4000

            # Score cases for 2
            if num[0] == 2:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 200
                if num[1] == 4:
                    score += 400
                if num[1] == 5:
                    score += 600
                if num[1] == 6:
                    score += 800

            # Score cases for 3
            if num[0] == 3:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 300
                if num[1] == 4:
                    score += 600
                if num[1] == 5:
                    score += 900
                if num[1] == 6:
                    score += 1200

            # Score cases for 4
            if num[0] == 4:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 400
                if num[1] == 4:
                    score += 800
                if num[1] == 5:
                    score += 1200
                if num[1] == 6:
                    score += 1600

            # Score cases for 5
            if num[0] == 5:
                if num[1] == 1:
                    score += 50
                if num[1] == 2:
                    score += 100
                if num[1] == 3:
                    score += 500
                if num[1] == 4:
                    score += 1000
                if num[1] == 5:
                    score += 1500
                if num[1] == 6:
                    score += 2000

            # Score cases for 6
            if num[0] == 6:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 600
                if num[1] == 4:
                    score += 1200
                if num[1] == 5:
                    score += 1800
                if num[1] == 6:
                    score += 2400

        return score

    @staticmethod
    def roll_dice(num_dice):
        results = []
        for num in range(num_dice):
            roll = randint(1, 6)
            results.append(roll)
        return tuple(results)

    @staticmethod
    def validate_keepers(roll, keepers):
        roll_count = Counter(sorted(roll)).most_common()
        keepers_count = Counter(sorted(keepers)).most_common()

        r_qty = []
        k_qty = []
        for num in roll_count:
            r_qty.append(num[1])
        for bum in keepers_count:
            k_qty.append(bum[1])
        if set(sorted(keepers)).issubset(sorted(roll)) and sorted(k_qty) <= sorted(r_qty):
            return True
        return False

    @staticmethod
    def get_scorers(tup):
        scorers = ()
        losers = ()
        index = 0
        for num in tup:
            index += 1

        # empty case
        if tup == ():
            return scorers

        # Check first value from input
        if index >= 1:
            one = tup[0],
            if GameLogic.calculate_score(one) > 0:
                scorers += one
            else:
                losers += one

        # Check second value from input
        if index >= 2:
            two = tup[1],
            if GameLogic.calculate_score(two) > 0:
                scorers += two
            else:
                losers += two
        else:
            return scorers

        # Check third value from input
        if index >= 3:
            three = tup[2],
            if GameLogic.calculate_score(three) > 0:
                scorers += three
            else:
                losers += three

        # Check fourth value from input
        if index >= 4:
            four = tup[3],
            if GameLogic.calculate_score(four) > 0:
                scorers += four
            else:
                losers += four

        # Check fifth value from input
        if index >= 5:
            five = tup[4],
            if GameLogic.calculate_score(five) > 0:
                scorers += five
            else:
                losers += five

        # Check six value from input
        if index >= 6:
            six = tup[5],
            if GameLogic.calculate_score(six) > 0:
                scorers += six
            else:
                losers += six

        print(losers)
        return tuple(sorted(scorers))

    def play_dice(self):
        print("Welcome to Ten Thousand!")
        while True:
            score_points = 0
            print("(y)es to play or (n)o to decline.")
            choice = input("> ")
            round_num = 1
            if choice == "n":
                print("OK. Maybe another time.")
                break
            elif choice == "y":
                while True:
                    print(f"Starting round {round_num}")
                    num_di = 6
                    roll_values = []
                    roll = GameLogic.roll_dice(num_di)
                    roll_length = len(roll)
                    print(f"Rolling {roll_length} dice...")
                    for value in roll:
                        roll_values.append(str(value))

                    formatted_roll = " ".join(roll_values)
                    print(f"*** {formatted_roll} ***")

                    print("Enter dice to keep, or (q)uit:")
                    choice = input("> ")

                    if choice == "q":
                        print(f"Thanks for playing. You earned {score_points} points")
                        break

                    else:
                        keepers = [int(d) for d in str(choice)]
                        # TODO: Why is line 243 - 254 being skipped????
                        # attempting to validate cheat_and_fix.sim.txt
                        test = GameLogic.validate_keepers(tuple(roll), tuple(keepers))
                        print(test)
                        if test == True:
                            continue
                        if test == False:
                            while test == False:
                                print("Cheater!!! Or possibly made a typo...")
                                print(f"*** {formatted_roll} ***")
                                print("Enter dice to keep, or (q)uit:")
                                choice = input("> ")
                                if test == True:
                                    break
                                break

                        points_potential = [int(d) for d in str(choice)]

                        for point in points_potential:
                            num_di -= 1
                        points = GameLogic.calculate_score(tuple(points_potential))
                        print(f"You have {points} unbanked points and {num_di} dice remaining")
                        while True:

                            print("(r)oll again, (b)ank your points or (q)uit:")
                            choice = input("> ")
                            if choice == "b":
                                score_points += points
                                print(f"You banked {points} in round {round_num}")
                                print(f"Total score is {score_points} points")
                                round_num += 1
                                break
                            elif choice == "q":
                                break
                            break

                break


if __name__ == "__main__":

    test2 = GameLogic.roll_dice(6)

    test3 = GameLogic.play_dice(test2)
    # test4 = GameLogic.get_scorers((3,3,3,1,1))
    # print(test4)
    # roll = (5,5,1,4,4,2)
    # points = [int(d) for d in str(555)]
    # test5 = GameLogic.validate_keepers(roll, tuple(points))
    # print(test5)