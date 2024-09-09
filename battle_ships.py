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

failure = [0, 0, 0, 0, 0, 0]
ship_count = 6

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