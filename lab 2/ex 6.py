#Finden Sie die längste zusammenhängende Domino Teilfolge. Eine Domino Teilfolge ist definiert als x1y1, x2y2, wo y1=x2. (z.B: 89, 95, 54)
l=[12,23,34,45,67]
def domino(l):
    lun = 1 #se initializeaza var lun cu 1,aceasta va fi folosită pentru a ține evidența lung curente a sec "domino" (adică elementele consecutive care se potrivesc)
    lunmax = 1 #va fi folosită pentru a ține evidența celei mai lungi sec "domino" găsite până acum
    indice = 0 #va fi folosită pentru a ține evidența indexului în listă al primului el al celei mai lungi sec "domino" găsite până acum

    #parcurge lista l până la penultimul element,compara fiecare el cu următorul el din listă

    for idx in range(0, len(l)-1): #idx variază de la 0 la len(l)-2
        if lun > lunmax: #compară lung curentă a sec cu cea mai lungă sec găsită până acum lunmax
            lunmax = lun #dacă lung curentă este mai mare decât cea mai lungă sec găsită, atunci se actualizează lunmax la lun
            indice = idx #indice este actualizat cu val indexului curent
        if l[idx] % 10 == l[idx+1]//10 % 10: #verifică dacă nr consecutive din listă se potrivesc jocului de domino,această verificare se face comparând ultima cifră a unui nr cu prima cifră a nr următor
            lun +=1 #dacă sunt la fel, lung sec consecutive (lun) este incrementată cu 1
        else:
            lun=1 #altfel, sec se întrerupe și lun este resetată la 1
    for i in range(indice - lunmax + 1, indice + 1): ##al doilea for se folosește pentru a afișa sec max găsită,acesta pornește de la indice - lunmax + 1 (începutul sec) și merge până la indice + 1 (sfârșitul sec)
        print(l[i]) #afișează elementele corespunzătoare din listă
domino(l) #am apelat functia


#lun=lungimea curenta
#lunmax=cea mai lunga secventa gasita