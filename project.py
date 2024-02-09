import time
import random
import sys
import re
import os
import traceback
import glob
from tabulate import tabulate


def get_word():
    file = open("words_alpha.txt", "r")
    words = file.read().splitlines()
    word = random.choice(words)
    return word


def test():

    stack = traceback.extract_stack()

    correct = 0
    incorrect = 0
    total = 0
    print("Re-type every word that comes up within the given time")
    print("Starting")
    t_end = time.time() + 30
    while time.time() <= t_end:

        #prints time left

        print("Time left:",end = "")
        print(int(t_end - time.time()))
        print()

        word = get_word()
        print(word)
        print("Enter: ",end= "")
        guess = input("")
        total += 1
        if word == guess:
            correct += 1
        else:
            incorrect += 1
        print()
    print("Time's up")
    wpm = calc_wpm(correct,incorrect,total)

    #if fucnction is called from homepage returns wpm to be written to file

    for frame in stack:
        if frame.name == "homepage":
            return wpm


def calc_wpm(correct,incorrect,total):

    #formula
    # WPM adjusted = Correct words x 100/time (in min) x accuracy %

    #calculating accuracy %
    print(f"Raw WPM: {total}")
    print(f"No. of mistakes: {incorrect}")
    accuracy = (correct/total) * 100
    print(f"Accuracy = {accuracy}% ")
    #WPM = (correct * 100)/(.5 * accuracy)
    WPM = total - incorrect
    print("adjusted WPM: ",end = "")
    print(int(WPM))
    return int(WPM)


def main():
    ch = input("Do you want to login, signup, test or check the scoreboard? ")
    if ch.startswith('l') or ch.startswith('L'):
        login()
    elif ch.startswith('sc') or ch.startswith('Sc'):
        scoreboard()
    elif ch.startswith('s') or ch.startswith('S'):
        signup()
    elif ch.startswith('t') or ch.startswith('T'):
        test()


def signup():
    user_name = input("Make a username: ")

    #validating username
    if re.match(r'.{4,}',user_name):
        pass
    else:
        signup()

    #checking if a user with that name already exists
    try:
        # Try to create a file
        File = open(f"{user_name}.txt", "x")
    except FileExistsError:
        c = input("User already exists.Would you like to login or retry signup?")
        if c.startswith("l") or c.startswith("L"):
            login()
        else:
            signup()

    password = input("Make a password: ")

    #validating password
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$',password):
        pass
    else:
        print("Password must contain")
        print(" At least one lowercase letter.")
        print("At least one uppercase letter.")
        print("At least one digit")
        print("Minimum 8 characters in total.")
        os.remove(f"{user_name}.txt")
        signup()

    info = f"User Name: {user_name} \nPassword: {password}"
    File.write(info)
    user_name = f"{user_name}.txt"
    homepage(user_name)


def login():
    name = input("Enter your user name: ")
    user_name = f"{name}.txt"

    #validating user exists
    if os.path.exists(user_name):
        pass
    else:
        print("User name does not exist.")
        c = input("Would you like to make an account or try logging in again(signup/retry)? ")
        if c.startswith("r") or c.startswith("r"):
            login()
        else:
            signup()

    #validating password
    try:
        with open(user_name, 'r') as file:
            for line in file:
                if "Password:" in line:
                    # Assuming the string you want is the part after the target word
                    index = line.index("Password:") + len("Password:")
                    pas = line[index:].strip()
    except FileNotFoundError:
        print(f"User not found")

    c = 0
    while True:
        att = input("Enter your password: ")
        if att == pas:
            homepage(user_name)
        c += 1
        if c == 3:
            break

def homepage(name):
    names = f"{name}.txt"
    #decide what homepage will do so far
    while True:
        choice = input("Run test, see your scores,the scoreboard,delete your account, or exit(test/scores/scoreboard/delete/exit)? ")
        if choice.startswith('t') or choice.startswith('T'):
            wpm = test()
            with open(f"{name}.txt",'a') as file:
                w = f"{str(wpm)} \n"
                file.write(w)
                file.close()
        if choice.startswith('E') or choice.startswith('e'):
            sys.exit(1)
        if choice.startswith('d') or choice.startswith('D'):
            os.remove(name)
            os.remove(names)
            sys.exit(1)
        if choice == "scores":
            with open(names, 'r') as file:
                # Read each line, convert to integer, and store in an array
                scores = [int(line.strip()) for line in file]
                scores.sort()
            print(scores)
        if choice == "scoreboard":
            scoreboard()

def scoreboard():

    directory_path = '.'

    # Use glob to find all files ending with .txt in the specified directory
    txt_files = glob.glob(f'{directory_path}/*.txt.txt')

    boards = []
    for file_path in txt_files:
        names = re.findall(r'\b\w+\b', file_path)
        #print(names[0])
        scores = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                scores = int(lines[-1])
                #print(scores)
        board = {'Name': names[0], 'Score':scores}
        boards.append(board)
    #print(boards)
    b = sorted(boards, key=lambda x: x['Score'], reverse=True)
    print(tabulate(b,headers="keys"))

if __name__ == "__main__":
    main()
