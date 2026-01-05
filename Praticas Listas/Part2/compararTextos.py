
texto1  = "O céu azul anuncia um dia de sol radiante"
texto2 =  "O sol brilha forte no céu azul"

textolista1 = texto1.split(' ')
textolista2 = texto2.split(' ')

comum = []  

for i in textolista1:
    for j in textolista2:
        if  i == '':
            continue
        elif i == j and i not in comum:
            comum.append(i)
print(comum)