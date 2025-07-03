import random

def generate_number():
    return random.randint(1, 100)

def take_guess():
    while True:  
        try:
            return int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.\n")

def check_guess(answer, number):
    if answer < number:
        return "Too low!\n"
    elif answer > number:
        return "Too high!\n"
    else:
        return "Correct!\n"

def main(): #Changed for stretch
    high_score = 100
    play = 'y'

    while play in ['y', 'yes']:
        tries = 0
        number = generate_number()
        guess_result = ''
    
        while guess_result != "Correct!\n":
            answer = take_guess()
            guess_result = check_guess(answer, number)
            print(guess_result)
            tries += 1

        print(f"You took {tries} tries.")
        if tries < high_score:
            high_score = tries
            print(f"New high score: {high_score} tries.")
        else:
            print(f"You couldn't beat your high score of {high_score} tries.")
        play = input("Play again? (y/n): ").lower().strip()

main()