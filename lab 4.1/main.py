from menu import *
from action_keys import deseneaza
from auto_draw import draw_automatic
from litere_desenate import sterge2

def main():
   with open('keys_pressed.txt', 'a') as file:
       file.write("\n")
   while True:
        print(meniu())
        opt = int(input("Optiunea="))

        if opt == 1:
            draw_automatic()
        if opt == 2:
            sterge2()
            print(meniu_deseneaza_manual())
            deseneaza()
        if opt == 0:
            break

main()