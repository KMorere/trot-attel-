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
        if len(result) == 1:
            result = result[0]
        else:
            result = ""
    elif _input.lower() in RACE_TYPE:
        result = _input

    return result


def display_results():
    """ Display the horses ranking. """

    # [!] Sorting through all horses to find the first isn't optimal.
    _sorted_horses = sorted(horses, key=lambda x: x["score"], reverse=True)
    highest = _sorted_horses[0]["score"]

    for i in range(0, HORSE_AMOUNT):
        # Display the numbers with spacing between single and double digits.
        print("[{:>2}] ".format(horses[i]["number"]), end='')

        # Uniform spacing of each travalled distance based on the current head of the race.
        for n in range(highest):
            # Display a character or empty space based on the travelled distance.
            if n <= horses[i]["score"]:
                if horses[i]["score"] >= RACE_LENGTH:
                    print("\x1b[32m█\x1b[0m", end='') # Green.
                else:
                    print("\x1b[39m█\x1b[0m", end='') # Default(white).
            else:
                print(" ", end='')

        # Distance travalled by each horse.
        print(" [{0}/{1}]".format(horses[i]["score"], RACE_LENGTH))


def end_game():
    """ Display end results. """

    # Sort all horses in the list from first to last.
    sorted_horses = sorted(finished_horses, key=lambda x: x["score"], reverse=True)

    if sorted_horses[0]["score"] < RACE_LENGTH:
        print("All horses are disqualified...")

    print(f"The top {race_type} of the race is :")

    for i in range(race_type):
        print(f"Number {sorted_horses[i]["number"]}.")


HORSE_AMOUNT = 12
RACE_LENGTH = 240
TURN_LENGTH = 2
RACE_TYPE = {"trifecta":3, "quartet":4, "quintet":5}

horses = [{"number":x+1, "speed":0, "score":0, "dq":False} for x in range(HORSE_AMOUNT)]
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

    while len(finished_horses) < HORSE_AMOUNT: # Continue the race until all horses are finished.
        set_speed()
        display_results()

        turn += 1

        input(f"Turn [{turn}], press enter to continue...")
    else: # Game is finished, display end results.
        end_game()