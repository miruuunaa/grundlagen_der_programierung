#Generieren Sie alle Primzahlen, die kleiner als eine natürliche Zahl n sind.

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