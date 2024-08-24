import random  # allows for probability

random_code = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
# ^ creates random number for each digit of 3 digit code
random_code = str(random_code[0]) + str(random_code[1]) + str(random_code[2])
# converts all values to string for comparison

number_of_guesses = 0  # tally of how many guesses they user has taken

while True:  # loops until user correctly guesses code
    correct_numbers = 0
    user_guess = input("Guess the code! Enter a 3 digit number: ")  # user inputs their guess
    number_of_guesses += 1  # adds a guess to the value
    if len(user_guess) != 3:  # if input was not 3 digits long
        print("Invalid guess length, try again!")  # return to start of loop
    else:  # if they
        if user_guess[0] == random_code[0]:  # if user got first digit correct
            correct_numbers += 1  # add to value
        if user_guess[1] == random_code[1]:  # if user got second digit correct
            correct_numbers += 1  # add to value
        if user_guess[2] == random_code[2]:  # if user got third digit correct
            correct_numbers += 1  # add to value
        if correct_numbers == 3:  # if the user guessed all the digits correct then
            print(f"You guessed the code! You guessed the number {random_code} in {number_of_guesses} guesses!")
            # ^ paste guesses and real code
            break  # user guessed code, breaks from loop
        else:  # if they didn't get the code correct
            print(f"{correct_numbers} numbers correct, try again!")  # user got it wrong, loops back to start
