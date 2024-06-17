import random

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
        break