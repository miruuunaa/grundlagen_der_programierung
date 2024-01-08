# Finden Sie den kleinsten gemeinsamen Vielfachen zwischen Index from und to, welche gegeben sind
def cmmdc(a,b): #cmmdc ,algoritmul lui euclid
    while (a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def cmmmc(a,b): # functia returnează cel mai mic multiplu a lui a si b
    return a * b // cmmdc(a,b) #functia returneaza cel mai mare div comun a lui a si b

def finden(l,fom,to): #functia are:o listă l și două indexuri, fom și to
    return cmmmc(l[fom],l[to]) #returnează cmmmc al elementelor din lista l de la indexul fom la indexul to, se face apelând funcția cmmmc cu valorile din lista l corespunzătoare indexurilor specificate
print(finden([12,24,48,5,6,3],0,2))