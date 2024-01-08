#Schreiben Sie eine Funktion, welche das pascalsche Dreieck auf dem Bildschirm ausgibt.

n = int(input(" Introduceti nr de coloane: ")) #nr de coloane pt triunghiul pascal (il stocheaza in var n)
list1 = [] #se initializeaza o lista goala care contine triunghiul
for i in range(n): #parcurge fiecare rând din triunghi, de la 0 la penultima coloana, fiecare rând este reprezentat de var i.
    temp = [] #lista goala temporara pt fiecare rand
    for j in range(i+1): #parcurge fiecare element de pe rândul curent, de la 0 la i,elementele rândului sunt reprezentate de var j.
        if j == 0 or j == i:
            temp.append(1) #se adauga valoarea 1 in lista
        else:
            temp.append(list1[i-1][j-1] + list1[i-1][j]) #se adauga valoarea care este suma celor două elemente situate deasupra lui j în rândul anterior
    list1.append(temp) #se adauga la lista principala


for i in range(n): #parcurge fiecare rand
    for j in range(n-i-1):
        print(format(" ",  "<2"), end="") #inaintea fiecarui rand se afiseaza spatii aliniate
    for j in range(i+1): # parcurge fiecare element de pe rând și le afișează formatate,să ocupe 4 caractere
        print(format(list1[i][j], "<4"), end="") #la sfârșitul fiecărui rând, se afișează o linie goală pentru a trece la următorul rând
    print()
