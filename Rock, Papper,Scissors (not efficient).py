import random
random.randint(1, 3)

while True:
    player = int(input("1 for rock, 2 for paper , and 3 for scissors and 0 to quit"))
    if player == 1:
        print("You threw Rock")
    elif player == 2:
        print("You threw Paper")
    elif player == 3:
        print("You threw Scissors")
 
        


    computer = random.randint(1, 3)


    #finished computer part
    if computer == 3:
        print("computer throws Scissors")
    elif computer == 2: 
        print("Computer throws Paper")
    else:
        print("Computer throws Rock")

    #rock
    if computer == player:
     print("Try again")
    elif computer == 1 and player == 2:
        print("Player Wins!!!")
    elif computer == 1 and player == 3:
        print("Computer Wins!!!")
    #paper
    if computer == 2 and player == 1:
        print("Computer Wins!")
    
    elif computer == 2 and player == 3:
        print("Player Wins!!!")
    #scissors
    if computer == 3 and player == 1:
        print("Computer lost!")
    elif computer == 3 and player == 2:
        print("Player lost!")
    elif player == 0: 
        print("Bye")
    break
