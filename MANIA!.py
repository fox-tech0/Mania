from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE
from colorama import Fore as f
from time import sleep as wait
from colorama import init as colin
from os import system as s
import time
import string
import random

# To get a random object from a list
def getRandom(list):
    return list[random.randrange(len(list))]

maniaLogo = """
--------------------------------------------------------------------------
███╗░░░███╗░█████╗░███╗░░██╗██╗░█████╗░██╗
████╗░████║██╔══██╗████╗░██║██║██╔══██╗██║      [ A Collection of Games ]
██╔████╔██║███████║██╔██╗██║██║███████║██║      By BrickLikesCoding
██║╚██╔╝██║██╔══██║██║╚████║██║██╔══██║╚═╝
██║░╚═╝░██║██║░░██║██║░╚███║██║██║░░██║██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝
--------------------------------------------------------------------------
"""

maniaLogo = maniaLogo.replace('█', f.LIGHTRED_EX + "█" + f.RESET)
maniaLogo = maniaLogo.replace('░', f.LIGHTBLACK_EX + "░" + f.RESET)
maniaLogo = maniaLogo.replace('[', f.LIGHTRED_EX + "[")
maniaLogo = maniaLogo.replace(']', f.LIGHTRED_EX + "]" + f.RESET)
maniaLogo = maniaLogo.replace('-', f"{f.LIGHTBLUE_EX}~")
maniaLogo = maniaLogo.replace('BrickLikesCoding', f.LIGHTYELLOW_EX + "BrickLikesCoding" + f.RESET)

guess = 0

def guess_the_number():
    print(f'What do you want the {f.LIGHTBLUE_EX}max{f.RESET} number to be?')
    max = int(input(f'{f.LIGHTRED_EX}->{f.RESET} '))
    num = random.randrange(max) + 1
    global guess
    numOfTries = 1
    # print(num)
    while (guess != num):
        answer = input(f'{f.LIGHTCYAN_EX}Guess: {f.LIGHTMAGENTA_EX}')
        try:
            guess = int(answer)
        except:
            if (answer == "cheat"):
                print(f"{f.LIGHTGREEN_EX}Correct Answer:{f.RESET} {str(num)}")
                print(f"Heh...")
            else:
                print(f'{f.LIGHTWHITE_EX}Yikes! Your answer must be a number!')
                pass
        if (guess == num):
            tries = str(numOfTries)
            print(f"{f.LIGHTGREEN_EX}Correct!")
            print(f"{f.LIGHTYELLOW_EX}It took you {tries} tries.")
            time.sleep(5)
            exit()
        else:
            if (answer == "cheat"):
                pass
            else: 
                numOfTries += 1
                print(f"{f.RED}Wrong! Try again...")

hasNumbers = True
hasLetters = True
hasSpecial = True

def generator():
    global hasNumbers, hasLetters, hasSpecial
    s('cls')
    print(f'{f.WHITE}E43Y P455W0RD G3N3R4T0R')
    print(f'{f.BLUE}>>>{f.RESET}Options')
    options = [
        "Has Numbers",
        "Has Letters",
        "Has Special Characters",
        "Generate"
    ]
    for i in range(len(options)):
        print(f"{f.LIGHTYELLOW_EX}{str(i+1)}. {f.WHITE}{options[i]}")
    choice = input(f'{f.LIGHTYELLOW_EX}>{f.RESET} ')
    if(choice == "1"):
        print('Has Numbers')
        print("Do you want numbers? (true/false)")
        truefalse = input(f"{f.LIGHTBLUE_EX}>{f.RESET} ")
        if truefalse.lower() in ['t', 'true']:
            hasNumbers = True
        else:
            hasNumbers = False
        generator()
    elif(choice == "2"):
        print('Has Letters')
        print("Do you want letters? (true/false)")
        truefalse = input(f"{f.LIGHTBLACK_EX}>{f.RESET} ")
        if truefalse.lower() in ['t', 'true']:
            hasLetters = True
        else:
            hasLetters = False
        generator()
    elif(choice == "3"):
        print('Has Special Characters')
        print("Do you want special characters? (true/false)")
        truefalse = input(f"{f.LIGHTBLACK_EX}>{f.RESET} ")
        if truefalse.lower() in ['t', 'true']:
            hasSpecial = True
        else:
            hasSpecial = False
        generator()
    elif(choice == "4"):
        print("Generate")
        print("How long do you want it to be?")
        length = int(input(f'{f.LIGHTBLACK_EX}>{f.RESET} '))
        special = list(string.punctuation)
        abc = list(string.ascii_letters)
        nums = list(string.digits)
        final = ""
        for i in range(length):
            choice = random.randrange(3)
            choice += 1
            # print(choice)
            if ( choice == 1 ):
                if( hasSpecial == True ):
                    final += getRandom(special)
                else:
                    if( hasNumbers == True ):
                        final += getRandom(nums)
                    else:
                        final += getRandom(abc)

            elif ( choice == 2 ):
                if( hasNumbers == True ):
                    final += getRandom(nums)
                else:
                    if ( hasSpecial == True ):
                        final += getRandom(special)
                    else:
                        final += getRandom(abc)
                    
            elif( choice == 3 ):
                if( hasLetters == True ):
                    final += getRandom(abc)
                else:
                    if ( hasSpecial == True ):
                        final += getRandom(special)
                    else:
                        final += getRandom(nums)
            
        print(f"{f.LIGHTRED_EX}Final Password:{f.RESET} {final}")
        print(f"{f.LIGHTGREEN_EX}Exiting in 10 seconds")
        print(f"{f.LIGHTMAGENTA_EX}The password has also been COPIED TO YOUR CLIPBOARD!")
        wait(10)
        exit()
            

def gameplay():
    s('cls')
    print(maniaLogo)
    options = "> Options <"
    options = options.replace('>', f.BLUE + '>' + f.RESET)
    options = options.replace('<', f.BLUE + '<' + f.RESET)
    gameOptions = [
        'Hangman',
        'Guess The Number',
        'Password Generator'
    ]
    print(options)
    for i in range(len(gameOptions)):
        print(f.LIGHTMAGENTA_EX + str(i + 1) + ". " + f.RESET + gameOptions[i])
    choice = input(f.LIGHTCYAN_EX + 'Enter your choice: ' + f.RESET)
    if(choice == "1"):
        main()
        hangman()
    elif(choice == "2"):
        guess_the_number()
    elif(choice == "3"):
        generator()


def main():
    global count
    global display
    global word
    global final_word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants","cat","dog","random","line","backing","save","bargain",
                   "feburary","month","year","amongus","chickennugget","check","get trolled"]
    word = random.choice(words_to_guess)
    final_word = word
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    

# A loop to re-execute the game when the first round ends:

def play_loop():
    global play_game
    play_game = input(f.LIGHTGREEN_EX + "Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input(f.LIGHTGREEN_EX + "Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
        hangman()
    elif play_game == "n":
        s('cls')
        print(f.RED + "Thanks For Playing! We expect you back again!")
        wait(1)
        exit()

def hangman():
    global count
    global display
    global word
    global final_word
    global final_word
    global already_guessed
    global play_game
    limit = 5
    guess = input(f.CYAN + "Word: "+ f.BLUE + display + f.CYAN +" Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print(f.RED + "Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        s('cls')
        print(display + "\n")

    elif guess in already_guessed:
        print(f.RED + "Try another letter.\n")

    else:
        count += 1

        if count == 1:
            s('cls')
            print(f.LIGHTGREEN_EX + "   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f.RED +"Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            s('cls')
            print(f.LIGHTGREEN_EX + "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f.RED + "Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           s('cls')
           print(f.LIGHTGREEN_EX + "   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print(f.RED + "Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            s('cls')
            print(f.LIGHTGREEN_EX + "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f.RED + "Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            s('cls')
            print(f.LIGHTGREEN_EX + "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print(f.RED + "Oops, look's like you were hung!\n")
            print(f.GREEN + "The word was: ", final_word, "Your Last Guess:", guess)
            print(f.BLUE + f"Your {f.LIGHTCYAN_EX}correct {f.BLUE}guesses:")
            for i in already_guessed:
                print(f'{f.LIGHTBLUE_EX}{i}')
            play_loop()

    if word == '_' * length:
        print(f.LIGHTGREEN_EX + "Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

											
s('cls')

colin(autoreset=True)

print(maniaLogo)

options = "> Options <"
options = options.replace('>', f.BLUE + '>' + f.RESET)
options = options.replace('<', f.BLUE + '<' + f.RESET)

print(options)

optionsList = [
    "Play",
    "Exit"
]
for i in range(len(optionsList)):
    print(f.LIGHTMAGENTA_EX + str(i + 1) + ". " + f.RESET + optionsList[i])

choice = input(f.LIGHTCYAN_EX + 'Enter your choice: ' + f.RESET)

if (choice == "1"):
    s('cls')
    gameplay()
elif(choice == "2"):
    s('cls')
    sec = 5
    for i in range(sec):
        s('cls')
        print(f.LIGHTRED_EX + 'Goodbye!')
        print(f.LIGHTMAGENTA_EX + 'Exiting in ' + f.LIGHTBLUE_EX + str(sec) + f.LIGHTMAGENTA_EX + ".")
        wait(1)
        sec -= 10
