"""
Guess the number and win the prize!

"""

magicNumber = 4

def get_number():
    myNumber = input("Enter your number=")
    return myNumber

def check_number():
    if (get_number() == magicNumber):
        print magicNumber
    else:
        check_number()

check_number()