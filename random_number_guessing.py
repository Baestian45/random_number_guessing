import better_random

def guess_number():
    random_number = better_random.random_int(1, 100)
    attempts = 0

    print("Welcome to my great number game")
    print("Just try guessing a number between 1 and 100 duh")

    while True:
        user_guess = int(input("What number do i think of: "))
        attempts += 1

        if user_guess > random_number:
            print("too high looser")
        elif user_guess < random_number:
            print("too low :((((")
        else:
            print(f"wow, u finally got it. it only took pathetic {attempts} attempts")
            break
    
guess_number()                
