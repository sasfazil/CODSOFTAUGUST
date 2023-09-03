import random

def start_game():
    return random.randint(1,3)

def comparision(user_input,computer_guess):
    if (user_input == 1 and computer_guess == 3) or \
    (user_input == 3 and computer_guess == 2) or \
    (user_input == 2 and computer_guess == 1):
        return "Congratulations You Won the match"
    elif user_input == computer_guess :
        return "It's a Tie"
    else:
        return "Computer Won the match. Better Luck Next Time"

def willing_to_play():
    return input("\nDo you want to continue the game (yes/no): ").lower().startswith("y")


def main():
    print("Welecome to Rock, Paper, Scissor game!")
    user_score = 0
    computer_score = 0
    while True:
        print("\nYour Current Score: {} | Computers Score: {}".format(user_score,computer_score))
        print("\nChoose from below: ")
        print("1.Rock")
        print("2.Paper")
        print("3.Scissors")
        user_input = int(input("Enter the option number: "))
        if 0 < user_input < 4:
            computer_guess = start_game()
            result = comparision(user_input,computer_guess)
            print("\nYou have Choosen : {} | Computer Choosen : {}\n".format(user_input,computer_guess))
            print("{}\n{}\n{}".format("-"*(len(result)),result,"-"*(len(result))))
        else:
            print("Enter the proper value")
        if "Computer" in result:
            computer_score += 1
        elif "You" in result:
            user_score += 1
        if not willing_to_play():
            print("Thanks For participating!")
            break
main()