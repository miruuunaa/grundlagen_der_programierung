from action_keys import *
def draw_automatic():
    word = input("Enter your word=")
    for letter in word:
        if letter in'0123456789':
            caracter_special()
        else:
            al[letter]()