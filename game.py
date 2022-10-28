import random

def game():
  while True:
    user_action = input("Enter a choice of yours(rock,paper,scisors)")
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
      print("Both players selected the same options, its a tie")
    elif user_action == "paper":
      if computer_action == "rock":
        print("paper covers rock, You win")
      else:
        print("scissors beats paper, You loose")
    elif user_action == "scissors":
      if computer_action == "paper":
        print("scissors beats paper, You win")
      else:
          print("rock beats scissors, You loose")
    elif user_action == "rock":
      if computer_action == "scissors":
        print("rock beats scissors, You win")
      else:
        print("paper covers rock, You loose")
    play_again = input("Play again y/n")
    if play_again.lower() != 'y':
      break
      
 game()
