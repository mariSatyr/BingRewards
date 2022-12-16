#bing search
import sys 
import os 
import string
import random
import time
import pyautogui

lowercase_letters = string.ascii_lowercase #A constant containing lowercase letters
uppercase_letters = string.ascii_uppercase #A constant containing uppercase letters
letters = string.ascii_letters #A contstant containing all uppercase and lowercase letters
def mixedcase_word(): #The function responsible for generating #random words which are in uppercase
    word = '' #The variable which will hold the random word
    random_word_length = random.randint(1,10) #The random length of the word
    while len(word) != random_word_length: #While loop
        word += random.choice(letters)
    return word
pyautogui.press("win")
pyautogui.write(mixedcase_word())
pyautogui.press('enter')
pyautogui.press('enter')

randomtime = random.randint(10, 20);

time.sleep(randomtime)
turns = 0
while turns < 60:
    pyautogui.press("win")
    pyautogui.write(mixedcase_word())
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(randomtime)
    turns=turns+1
