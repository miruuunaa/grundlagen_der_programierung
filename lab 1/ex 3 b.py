#Gegeben sei ein Vektor von Zahlen, finden Sie die längste zusammenhängende Teilfolge von Primzahlen.

def is_prime(n): #se defineste prima functie cu un nr n
    if n <= 1: #n mai mic sau egal cu 1
        return False #nr nu este prim
    if n <= 3: #n mai mic sau egal cu 3
        return True #n este prim

    if n % 2 == 0 or n % 3 == 0: #verifica dac n este divizibil cu 2 sau cu 3
        return False #atunci returneaza false

    i = 5 #se initializeaza variabila i cu 5
    while i * i <= n: #se executa atat timp cat patratul lui i este mai mic sau egal cu n
        if n % i == 0 or n % (i + 2) == 0: #se verifica daca n este divizibil cu i sau cu i+2
            return False #daca este divizibil returneaza false
        i += 6 #i creste cu 6 dupa iteratie

    return True #daca nu este executata nici o conditie din while,returneaza true=nr este prim

def sec_nrprime(lista_de_numere): #se defineste o functie si primeste o lista de nr
    sec_curent = [] #se difineste o lista goala,care va stoca sec_curent de nr prime
    sec_lung = [] #se difineste o lista goala,care va stoca sec_lung de nr prime consecutive găsita până acum

    for numar in lista_de_numere: #trece prin fiecare nr din lista
        if is_prime(numar): #se verifica daca nr este prim
            sec_curent.append(numar) #daca este prim ,atunci se adauga la sec_curent
        else: #daca nu este prim
            if len(sec_curent) > len(sec_lung): #daca lung lui sec_curent este mai mare decat lung lui sec_lung
                sec_lung = sec_curent #daca sec_curent este mai mare,atunci sec_lung se actualizeaza cu sec_curent
            sec_curent = [] #se reinițializează pentru a începe o noua sec

    if len(sec_curent) > len(sec_lung): #se mai face o verificare de lungime
        sec_lung = sec_curent

    return sec_lung #se returneaza sec_lung consecutiv de numere prime găsit în lista

# Exemplu de listă de numere
lista_de_numere = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 90]

cel_mai_lung_subșir_de_numere_prime = sec_nrprime(lista_de_numere) #se apeleaza functia pt a gasi sec_lung
print("Cel mai lung subșir consecutiv de numere prime este:", cel_mai_lung_subșir_de_numere_prime) #se afiseaza rezultatul
