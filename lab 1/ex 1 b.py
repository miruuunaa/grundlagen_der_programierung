#Gegeben sei ein Vektor von Zahlen, finden Sie die längste ansteigende zusammenhängende Teilfolge.

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

v = [1, 2, 3, 4, 5,6, 0, 3, 2, 1]
final = secventa_cu_lungime_maxima(v) # apelam functia'secv...', si copiem intr-o lista finala rezultatul functiei
print('Cea mai lunga secventa a listei ', v,' este: ', final)

 # va afisa: Cea mai lunga secventa a listei  [1, 2, 3, 4, 5, 0, 3, 2, 1]