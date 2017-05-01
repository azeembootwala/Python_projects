"""
This python file generates a string/names using random constraints and length
"""

import random
import string
vowels = "aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
letters=vowels+consonents

first_letter = input("Enter any letter , chose v for volwels, c for consonents,& l for anyletter:- ")
second_letter = input("Enter any letter , chose v for volwels, c for consonents,& l for anyletter:- ")
third_letter = input("Enter any letter , chose v for volwels, c for consonents,& l for anyletter:-")
def key_gen(first_letter,second_letter,third_letter):
    if first_letter=="v":
        one=random.choice(vowels)
    elif first_letter=="c":
        one=random.choice(consonents)
    else:
        one=random.choice(letters)
    if second_letter=="v":
        two=random.choice(vowels)
    elif second_letter=="c":
        two=random.choice(consonents)
    else:
        two=random.choice(letters)
    if third_letter=="v":
        three=random.choice(vowels)
    elif third_letter=="c":
        three=random.choice(consonents)
    else:
        three=random.choice(letters)
    result =one+two+three
    return result

print(key_gen(first_letter,second_letter,third_letter))
