import random

random_code = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
random_code = str(random_code[0]) + str(random_code[1]) + str(random_code[2])

number_of_guesses = 0

while True:
    correct_numbers = 0
    user_guess = input("Guess the code! Enter a 3 digit number: ")
    number_of_guesses += 1
    if len(user_guess) > 3:
        print("Too many characters, try again!")
    else:
        if user_guess[0] == random_code[0]:
            correct_numbers += 1
        if user_guess[1] == random_code[1]:
            correct_numbers += 1
        if user_guess[2] == random_code[2]:
            correct_numbers += 1
        if correct_numbers == 3:
            print(f"You guessed the code! You guessed the number {random_code} in {number_of_guesses} guesses!")
            break
        else:
            print(f"{correct_numbers} numbers correct, try again!")
