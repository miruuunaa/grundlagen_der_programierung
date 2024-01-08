#Filtern Sie die Zahlen, die eine bestimmte Beziehung zwischen Zahlen haben, die in einem String angegeben wird. (z.B: “x=y*3”, “x/y=2“, …
string="x/y=2"

l=[ 42, 63, 98]

def filt(l,string): #functia primeste o lista si un sir
    for i in l: #trece prin toate elementele din lista
        string_new= string #se creaza o copie,folosită pentru a efectua înlocuiri în șir fără a modifica șirul original
        string_new = string_new.replace('y',str(i%10)) #se înlocuiesc caracterele 'y' din string_new cu ultima cifră a lui i
        string_new = string_new.replace('x',str(i//10%10)) #se înlocuiesc caracterele 'x' din string_new cu a doua cifră a lui i
        x= string_new.split('=') #se descompune șirul în două părți folosind semnul egal ca separator și se stochează cele două părți într-o listă x
        if eval(x[0]) == eval(x[1]): #se evalueaza val numerice din ambele părți,dacă cele două părți sunt egale numeric, atunci se executa programul mai departe
            print(i) #daca cele 2 parti sunt egale se afiseaza val lui i

filt(l,string)