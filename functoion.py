#1번
code = "*"

print(code * 100)
print()
print("* Welcome to Coding World *")
print()
print(code * 100)


#2번
import random

word = ["chan", "man", "hansome", "big"]
Word = random.choice(word)
if Word is "chan":
    firstword = "c"
    if Word is "man":
        firstword = "m"
        if Word is "hansome":
            firstword = "h"
            if Word is "big":
                firstword = "b"

print("You can  find in chan, man, hansome, big.")
print("it's ", len(Word), "spels.")
print("Do you have a code?\nSay Yes or No")
if input("Yes"):
    print("What is the code?")
    if input("chan"):
        print(firstword, "is word's first word.")
    elif input(not "chan"):
        exit("Bye ~~ ^ㅡ^")
elif input("No"):
    print("What is the word?")
    if input(Word):
            exit("That's true!")
    if input(not Word):
        exit("Noooo!!!!!!")