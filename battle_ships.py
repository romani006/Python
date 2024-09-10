import random

user_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

opponent_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

user_guesses = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

failure = [0, 0, 0, 0, 0, 0]
ship_count = 6

def coordinate_converter(coordinate):
    if coordinate == 1:
        coordinate = 4
    elif coordinate == 2:
        coordinate = 3
    elif coordinate == 3:
        coordinate = 2
    elif coordinate == 4:
        coordinate = 1
    return coordinate

# user plots ships
for i in failure:
    locationx = (input(f"Enter an x coordinate for your ship (1-4, {ship_count} ships remaining): "))
    try:
        locationx = int(locationx)
    except ValueError or KeyError:
        print("Invalid number entered, try again.")
        failure.append(0)
        continue

    if locationx > 4 or locationx < 1:
        print("Invalid number entered, try again.")
        failure.append(0)
        continue

    locationy = (input(f"Enter an y coordinate for your ship (1-4, {ship_count} ships remaining): "))
    try:
        locationy = int(locationy)
    except ValueError or KeyError:
        print("Invalid number entered, try again.")
        failure.append(0)
        continue

    if locationy > 4 or locationy < 1:
        print("Invalid number entered, try again.")
        failure.append(0)
        continue

    locationx = coordinate_converter(locationx)
    locationy = coordinate_converter(locationy)

    locationx -= 1
    locationy -= 1

    if user_map[locationy][locationx] == 1:
        print("Coordinate already used, try again.")
        failure.append(0)
        continue
    else:
        user_map[locationy][locationx] = 1
        ship_count -= 1

    if ship_count == 0:
        break


print("Here are your ship locations: ")
print(user_map[0])
print(user_map[1])
print(user_map[2])
print(user_map[3])


# computer plots ships

failure = [0, 0, 0, 0, 0, 0]
ship_count = 6

for i in failure:
    locationx = (random.randint(1, 4))
    try:
        locationx = int(locationx)
    except ValueError or KeyError:
        failure.append(0)
        continue

    if locationx > 4 or locationx < 1:
        failure.append(0)
        continue

    locationy = (random.randint(1, 4))
    try:
        locationy = int(locationy)
    except ValueError or KeyError:
        failure.append(0)
        continue

    if locationy > 4 or locationy < 1:
        failure.append(0)
        continue

    locationx = coordinate_converter(locationx)
    locationy = coordinate_converter(locationy)

    locationx -= 1
    locationy -= 1

    if opponent_map[locationy][locationx] == 1:
        failure.append(0)
        continue
    else:
        opponent_map[locationy][locationx] = 1
        ship_count -= 1

    if ship_count == 0:
        break

print("Opponent ship locations (test)")
print(opponent_map[0])
print(opponent_map[1])
print(opponent_map[2])
print(opponent_map[3])

def ship_standings():
    print("Here are your ships standings: ")
    print(user_map[0])
    print(user_map[1])
    print(user_map[2])
    print(user_map[3])
    print()
    print("Here are the guesses you've made: ")
    print(user_guesses[0])
    print(user_guesses[1])
    print(user_guesses[2])
    print(user_guesses[3])

# game start

print("Opponent has chosen their ship locations. Game starting!")

user_ships = 6
opponent_ships = 6
user_turn = True
opponent_turn = False

while True:

    # user guesses

    if user_turn == True:
        user_guessx = (input(f"Enter an x coordinate for the location of an opponent ship (1-4, {opponent_ships} ships remaining): "))
        try:
            user_guessx = int(user_guessx)
        except ValueError or KeyError:
            print("Invalid number entered, try again.")
            continue

        if user_guessx > 4 or user_guessx < 1:
            print("Invalid number entered, try again.")
            continue

        user_guessy = (input(f"Enter an y coordinate for the location of an opponent ship (1-4, {opponent_ships} ships remaining): "))
        try:
            user_guessy = int(user_guessy)
        except ValueError or KeyError:
            print("Invalid number entered, try again.")
            continue

        if user_guessy > 4 or user_guessy < 1:
            print("Invalid number entered, try again.")
            continue

        user_guessx -= 1
        user_guessy -= 1

        if opponent_map[user_guessy][user_guessx] == 1:
            print("Hit!")
            opponent_map[user_guessy][user_guessx] = "X"
            user_guesses[user_guessy][user_guessx] = "X"
            opponent_ships -= 1
        elif opponent_map[user_guessy][user_guessx] == "X":
            print("Location already guessed, try again.")
            continue
        else:
            print("Miss...")
            user_guesses[user_guessy][user_guessx] = "X"

        if opponent_ships == 0:
            break

        user_turn = False
        opponent_turn = True

    # opponent guess

    if opponent_turn == True:
        print("Opponent is making their guess...")
        opponent_guessx = (random.randint(1, 4))
        try:
            opponent_guessx = int(opponent_guessx)
        except ValueError or KeyError:
            continue

        if opponent_guessx > 4 or opponent_guessx < 1:
            continue

        opponent_guessy = (random.randint(1, 4))
        try:
            opponent_guessy = int(opponent_guessy)
        except ValueError or KeyError:
            continue

        if opponent_guessy > 4 or opponent_guessy < 1:
            continue

        opponent_guessx -= 1
        opponent_guessy -= 1

        if user_map[opponent_guessy][opponent_guessx] == 1:
            print("Hit!")
            user_map[opponent_guessy][opponent_guessx] = "X"
            user_ships -= 1
        elif user_map[opponent_guessy][opponent_guessx] == "X":
            continue
        else:
            print("Miss...")
            user_map[opponent_guessy][opponent_guessx] = "X"


        ship_standings()

        if user_ships == 0:
            break

        user_turn = True
        opponent_turn = False


if user_ships == 0:
    print("You lose!")
elif opponent_ships == 0:
    print("You win!")
else:
    print("How did you get here?")