

#addition
def add(x,y):
    return x + y

#soustraction
def sous(x,y):
    return x - y

#multiplication
def mult(x,y):
    return x * y

#division
def div(x,y):
    return x / y

result = 0

print("""Choix option \n
      1- Addition \n
      2- Soustraction \n
      3- Multiplication \n
      4- Division \n""")

while True :
    choix = input("Entrer votre choix (1,2,3,4):")

    if choix in ("1","2","3","4"):
        num1 = float(input("Entrer votre premier nombre, si vous voulez conserver le resultat tapez 00.0:"))
        if num1 == 00.0:
            num1=result
        num2 = float(input("Entrer votre deuxieme nombre :"))

        if choix == "1" :
            print( num1 , "+",num2, "=",add(num1, num2))
            result = add(num1, num2)

        if choix == "2" :
            print( num1 , "-",num2, "=",sous(num1, num2))
            result = sous(num1, num2)

        if choix == "3" :
            print( num1 , "*",num2, "=",mult(num1, num2))
            result = mult(num1, num2)

        if choix == "4" :
            print( num1 , "/",num2, "=",div(num1, num2))
            result = div(num1, num2)
        
        next_calcul = input("Voulez-vous faire un autre calcul ? (Oui/Non) : ")
        if next_calcul == "Non" :
            break
        if next_calcul == "non" :
            break
