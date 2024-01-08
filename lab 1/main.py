'''
#1. a
n = int(input("Enter a number: "))

for i in range(2, n + 1): #parcurge numerele de la 2 la numărul introdus n.
    is_prime = 1 #se presupune ca nr curent i este prim
    for d in range(2, i // 2 + 1): #verifica divizorii lui i de la 2 pana la jumate
        if i % d == 0: #se verifica dace e divizibil
            is_prime = 0 #daca i este divizibil cu d , atunci is_prime se face 0 , i nu este prim
            break  # se opreste daca gaseste un divizor
    if is_prime == 1: #se verifica daca is_prime are valoarea 1,atunci i este prim
        print(i, end=" ") #se afiseaza urmat de un spatiu

#trece la următorul număr,se repetă instructiunile până când au fost verificate toate numerele de la 2 la n.
#dupa ce programul se încheie,vor fi afișate toate numerele prime de la 2 la n.

#1. b

def secventa_cu_lungime_maxima(v):
     if not v: #se  verifica daca lista este goala
         return[] #o returneaza goala

     lung_act = 1 #cel putin un element in lungimea curenta
     lung_max = 1 #cel putin un element in lungimea maxima
     secv_act = [v[0]] #contine primul element din lista\vector v
     secv_max = [v[0]] #contine primul element din lista\vector v

     for i in range (1, len(v)): #se parcurge lisat incepand cu al doilea element
         if v[i-1] <= v[i]: #se verifică dacă elementul curent v[i] este mai mare sau egal cu elementul precedent
             lung_act += 1 #daca este mai mare ,atunci secventa continua sa creasca
             secv_act.append(v[i]) #elementul curent se adauga
         else:
             if lung_max < lung_act: # daca nu este mai mare atunci se incheie secventa,atunci se verifica..
                 lung_max = lung_act #daca da, atunci secventa este actualizata cu valoarea curenta
                 secv_max = secv_act #daca da, atunci secventa este actualizata cu valoarea curenta
             lung_act = 1 #se reseteaza pentru a incepe o noua sec
             secv_act = [v[i]] #reluam secventa actuala de la capat
     if lung_max < lung_act: #inca o verificare sa se vada daca secv_max este cea lunga
         secv_max = secv_act #se actualizeaza cu valoarea curenta
     return secv_max #contine cea mai lungă secv continua de elemente

v = [1, 2, 3, 4, 5, 0, 3, 2, 1]
final = secventa_cu_lungime_maxima(v) # apelam functia'secv...', si copiem intr-o lista finala rezultatul functiei
print('Cea mai lunga secventa a listei ', v,' este: ', final)

 # va afisa: Cea mai lunga secventa a listei  [1, 2, 3, 4, 5, 0, 3, 2, 1]

'''

#3 a.

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
