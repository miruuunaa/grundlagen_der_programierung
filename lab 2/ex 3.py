#  Generieren Sie die größte mögliche Zahl, die aus der Konkatenation der Elemente der Liste gebildet ist.
def mare(l): #se defineste functia si primeste o lista l
    numar = 0 #se initializaeza o var numită nr cu val 0 ,va fi utilizată pentru a stoca nr format din elementele listei
    indice = 0 # se initializeaza o var indice cu val 0, va fi folosită pentru a ține evidența poziției elementului maxim în listă
    while len(l) != 0: #se executa atata timp cat lista l este goala
        max = 0 #se initializeaza o var ,pentru a stoca val max găsită în listă
        for idx in range(0,len(l)): #trece prin toate elementele listei l, utilizând var idx pentru a ține evidența indexului elementului curent
            if l[idx] > max: #se verifica daca el curent este mai mare decat val maxima
                max = l[idx] #daca este mai mare atunci se actualizeaza val maxima
                indice = idx #pentru a ține evidența indexului elementului max în listă
        numar = numar * 100 + max #după ce am găsit max în listă, adăugăm val max la nr,prin înmulțirea lui nr cu 100 și adăugarea max,se creaza un nr mai mare care combină el din listă în ordinea lor
        l.pop(indice)#se elimina el max din listă folosind funcția pop
    return numar #returnează val numar, care reprezintă nr mare format prin combinarea elr din lista l
print(mare([12,78,93]))