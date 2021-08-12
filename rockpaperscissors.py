
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print("******************************\n")
    print("Rock, Paper, Scissors - Shoot!\n")
    print("******************************\n")
    ChosedWeapon = raw_input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", ChosedWeapon):
        print "Please choose a letter:"
        print "[R]ock, [S]cissors or [P]aper."
        continue
    # Confirming the user's weapon choice.
    print "You chose: " + ChosedWeapon
    weapons = ['R', 'P', 'S']
    # Assigning a weapon to the computer.
    OpponentWeapon = random.choice(choices)
    # Informing the computer's weapon of choice.
    print "I chose: " + opponentChoice
    if OpponentWeapon == str.upper(ChosedWeapon):
        print "That was a tie!! "
    elif OpponentWeapon == 'R' and ChosedWeapon.upper() == 'S':
        print "Scissors beats rock, I win!! "
        continue
    elif OpponentWeapon == 'S' and ChosedWeapon.upper() == 'P':
        print "Scissors beats paper! I win!! "
        continue
    elif OpponentWeapon == 'P' and ChosedWeapon.upper() == 'R':
        print "Paper beat rock, I win!! "
        continue
    else:
        print "You win! Congratulations!! "