def get_guess():
    guess = int(input("Enter your guess: "))
    return guess


def main():
    guess = get_guess()
    if guess == 50:
        print(str(guess) + " is correct!")
    else:
        print(str(guess) + " is incorrect!")

main()
