import random

def spiele_schere_stein_papier():
    symbole = ['Schere', 'Stein', 'Papier']
    gewinne_benutzer = 0
    gewinne_computer = 0

    while gewinne_benutzer < 2 and gewinne_computer < 2:
        computer_wahl = random.choice(symbole)
        benutzer_wahl = input("Wählen Sie Schere, Stein oder Papier: ")

        if benutzer_wahl in symbole:
            print(f"Computer wählt: {computer_wahl}")

            if benutzer_wahl == computer_wahl:
                print("Unentschieden!")
            elif (
                    (benutzer_wahl == 'Schere' and computer_wahl == 'Papier') or
                    (benutzer_wahl == 'Stein' and computer_wahl == 'Schere') or
                    (benutzer_wahl == 'Papier' and computer_wahl == 'Stein')
            ):
                print("Sie gewinnen!")
                gewinne_benutzer += 1
            else:
                print("Computer gewinnt!")
                gewinne_computer += 1
        else:
            print("Ungültige Eingabe. Bitte wählen Sie Schere, Stein oder Papier.")

    if gewinne_benutzer > gewinne_computer:
        print("Sie haben das Spiel gewonnen!")
    elif gewinne_benutzer < gewinne_computer:
        print("Computer hat das Spiel gewonnen!")
    else:
        print("Das Spiel endet unentschieden!")


if __name__ == "__main__":
    spiele_schere_stein_papier()