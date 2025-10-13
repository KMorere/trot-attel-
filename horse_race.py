import random

def set_speed():
    """ Set the speed of all horses. """

    for i in range(0, len(horses)):
        # if horses[i]["dq"] == True:
        #     continue
        # if horses[i]["speed"] == 6:
        #     horses[i]["dq"] = True
        #     horses.remove(horses[i])
        horses[i]["speed"] = random.randint(1, 6)
        horses[i]["score"] += horses[i]["speed"] * TURN_LENGTH

        if horses[i]["score"] >= RACE_LENGTH:
            winners.append(horses[i])


def velocity_change(_nb, _speed): # TO IMPLEMENT
    match _nb:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass


HORSE_AMOUNT = 12
RACE_LENGTH = 2400
TURN_LENGTH = 23
RACE_TYPE = {"three":3, "four":4, "five":5}

horses = [{"speed":0, "score":0, "dq":False} for _ in range(HORSE_AMOUNT)]
winners = []

if __name__ == "__main__":
    while len(winners) < HORSE_AMOUNT:
        set_speed()
    print(winners[:3])