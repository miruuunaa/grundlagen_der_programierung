#Enfernen Sie die Zahlen die sich wiederholen

numbers=[10,2,3,4,5,7,7,8,2,10]
unique=[] #initializam o lista noua
for number in numbers: #cautam nr
    if number not in unique:  #daca nu avem nr in lista noastra
        unique.append(number)  #adaugam in lista noua
print(unique)