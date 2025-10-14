import random


def set_speed():
    """ Set the speed of all horses in a single turn. """

    for i in range(0, len(horses)):
        if horses[i] in finished_horses:
            continue

        horses[i]["speed"] += velocity_change(random.randint(0, 5), horses[i])
        horses[i]["score"] += horses[i]["speed"] * TURN_LENGTH

        if horses[i]["score"] >= RACE_LENGTH:
            finished_horses.append(horses[i])


def velocity_change(_nb, _horse):
    """ Update de speed of a horse base on the dice roll and its current speed.

    :param _nb: Rolled number from the dice.
    :param _horse: Current horse getting its speed updated.
    :return: Returns the new speed.
    """

    new_vel = velocity_list[_horse["speed"]][_nb]

    if _horse["speed"] == 6 and _nb+1 == 6:
        _horse["dq"] = True
        finished_horses.append(_horse)

    return new_vel


def is_valid_input():
    """ Checks if the input is in 'RACE_TYPE'. """

    _input = input(f"Select a race type in the list:{list(RACE_TYPE.keys())} (in letters or numbers) : ")
    result = ""

    if _input.isdigit():
        result = [key for key, val in RACE_TYPE.items() if val == int(_input)]
        result = result[0]
    elif _input.lower() in RACE_TYPE:
        result = _input

    return result


HORSE_AMOUNT = 12
RACE_LENGTH = 2400
TURN_LENGTH = 23
RACE_TYPE = {"three":3, "four":4, "five":5}

horses = [{"speed":0, "score":0, "dq":False} for _ in range(HORSE_AMOUNT)]
finished_horses = []

velocity_list = [
    [0, 1, 1, 1, 2, 2],
    [0, 0, 1, 1, 1, 2],
    [0, 0, 1, 1, 1, 2],
    [-1, 0, 0, 1, 1, 1],
    [-1, 0, 0, 0, 1, 1],
    [-2, -1, 0, 0, 0, 1],
    [-2, -1, 0, 0, 0, 0]
]

if __name__ == "__main__":
    turn = 0
    race_type = is_valid_input()

    while race_type not in RACE_TYPE:
        race_type = is_valid_input()

    if race_type.isalnum():
        race_type = RACE_TYPE[race_type]

    while len(finished_horses) < HORSE_AMOUNT:
        set_speed()

        turn += 1

    sorted_horses = sorted(finished_horses, key = lambda x:x["score"], reverse = True)

    if sorted_horses[0]["score"] < RACE_LENGTH:
        print("All horses are disqualified...")

    print(sorted_horses[:race_type])