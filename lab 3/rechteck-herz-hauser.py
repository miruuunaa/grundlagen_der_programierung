import turtle

#example
# t = turtle.Pen()
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.reset()
# #t.clear()
# t.backward(100)
# t.up()
# t.right(90)
# t.forward(20)
# t.left(90)
# t.down()
# t.forward(100)

#Ub1
def rechteck(a):
    for i in range(4):
        if i % 2 == 0:
            a.forward(200)
        else:
            a.forward(100)
        a.left(90)

    a.up()
    a.left(45)
    a.forward(50)
    a.down()
    a.right(45)

    for i in range(4):
        if i % 2 == 0:
            a.forward(50)
        else:
            a.forward(25)
        a.left(90)

    a.reset()
    turtle.done()


#Ub2

def herz(a):
    a.left(45)
    a.forward(150) #se rotește cu 45 de grade la stânga, apoi desenează o linie de 150 de unități pentru partea de sus a inimii
    a.circle(70, 200) #se desenează jumătate din cercul superior al inimii
    a.right(125) # se rotește la dreapta cu 125 de grade și se desenează jumătate din cercul inferior al inimii
    a.circle(70, 200)
    a.forward(150) # se desenează o linie de 150 de unități pentru partea de jos a inimii

    a.reset()
    turtle.done()


#Ub3


def hauser(a, b):
    a.up()
    a.backward(100)
    a.down()
    b.up()
    b.forward(100)
    b.down()

    for i in range(4): #Se folosesc buclele pentru a desena părțile exterioare ale caselor și detalii precum ferestrele
        for j in range(100):
            a.forward(1)
            b.forward(1)
        a.right(90)
        b.right(90)
    a.left(60)
    b.left(60)
    for i in range(2):
        for j in range(100):
            a.forward(1)
            b.forward(1)
        a.right(120)
        b.right(120)

    a.up()
    a.left(30)
    a.forward(40)
    a.left(60)
    a.down()
    b.up()
    b.left(30)
    b.forward(40)
    b.left(60)
    b.down()

    for i in range(4):
        for j in range(30):
            a.forward(1)
            b.forward(1)
        a.right(90)
        b.right(90)

    a.up()
    a.forward(45)
    a.down()
    b.up()
    b.forward(45)
    b.down()

    for i in range(4):
        if i % 2 == 0:
            for j in range(35):
                a.forward(1)
                b.forward(1)
        else:
            for j in range(30):
                a.forward(1)
                b.forward(1)
        a.right(90)
        b.right(90)

    a.reset()
    b.reset()
    turtle.done()



def menu(): #această funcție afișează un meniu simplu în consolă, care permite utilizatorului să selecteze ce figură să fie desenată
    print(
        """
        Wahlen Sie eine Zeichnung aus:
        1 - Rechteck
        2 - Herz
        3 - Hauser
        """
    )


def main():
    menu()
    a = turtle.Pen()

    opt = int(input('option = '))
    if opt == 1:
        rechteck(a)
    elif opt == 2:
        herz(a)
    else:
        b = turtle.Pen()
        hauser(a,b)


main()
