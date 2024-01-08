# Schreiben Sie die Anzahl von symmetrischen Paaren (xy) und (yx).
numbers = [55, 66, 77, 55, 88, 66,77,56,65]
def perechi(numbers):
    count=0 #numar perechile
    for i in range (0,len(numbers)-1): #parcurge toate nr din lista
        for j in range(i+1,len(numbers)): #pentru fiecare nr parcurg cu al doilea for si caut simetricul lui in lista
            if numbers[i]%10 == numbers[j]//10%10: #daca ultima cifra a lui i e egala cu prima cifra a lui j
                if numbers[i]//10%10==numbers[j]%10:  #daca prima cifra a lui i e egala cu ultima cifra a lui j
                    count +=1 #cand gaseste o pereche simetrica creste
    return count
print(perechi(numbers))


