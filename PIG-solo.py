import random
print("Hello there! Welcome to PIG, a simple game of luck! \n")
print("Score ceiling is 50! Try and get the highest score possible without rolling a 1. \n")
roll = input("Do you want to Roll? (yes/no): ").lower()

while roll != "yes" and roll != "no":
    print('Please type Yes or No')
    roll = input("Do you want to Roll? (yes/no): ").lower()
    
     

score = 0

while roll == "yes" and score < 50:
    add = random.randint(1, 6)
    score += add
    print(f"Your current score is: {score}")
    if add == 1:
        print('Oh no, You rolled a 1 and lost all your score! Game over.')
        score -= score
        print(f"Your new score is: {score}, Better luck next time!")
        break
    roll = input("Do you want to Roll? (yes/no): ").lower()
    if roll == "no":
        print("Thanks For Playing!")
        print(f"You ended with a total score of {score}. Congrats on not rolling a 1!")
        break