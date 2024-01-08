#Verschlüsseln Sie die Elemente der Liste, indem Sie das erste Element als Schlüssel benützen und die Methode selbst wählen (+, *, XOR).
def ver(l): #se defineste functia si primeste o lista
    for idx in range(1,len(l)): #parcurge toata lista,începe de la indicele 1 (elementul al doilea al listei) și merge până la ultimul element din listă
        l[idx]= [ l[0] + l[idx]] #in fiecare iterație,el de la idx din l este modificat,se adaugă 1 la val el existent și se înlocuiește el original cu noua val,acest lucru se realizează înlocuind el la idx cu o listă ce conține noua val, rezultând [1 + l[idx]].
    return l #returnează l, care a fost modificată prin adăugarea val 1 la fiecare el
print(ver([22,23,24,25,30,34])) #l;a fiecare el din lista se adauga primul