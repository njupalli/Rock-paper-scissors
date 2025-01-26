rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors
'''
import random
game = [rock, paper, scissors]


your_choice = input("Type r for rock, p for paper, or s for scissors\n").casefold()


computer_choice = random.choice(game)


if your_choice == "r":
    print("You chose" + rock)
    print("The computer chose " + computer_choice)
    if computer_choice == rock:
        print("Draw")
    elif computer_choice == paper:
        print("You lose")
    elif computer_choice == scissors:
        print("You win!")
    else:
        print("fix code")
elif your_choice == "p":
    print("You chose" + paper)
    print("The computer chose " + computer_choice)
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("Draw")
    elif computer_choice == scissors:
        print("You lose!")
    else:
        print("fix code")

elif your_choice == "s":
    print("You chose" + scissors)
    print("The computer chose " + computer_choice)
    if computer_choice == rock:
        print("You lose")
    elif computer_choice == paper:
        print("You win!")
    elif computer_choice == scissors:
        print("Draw!")
    else:
        print("fix code")
else:
    print("Type r, p, or, s")




