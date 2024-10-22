#Zad. 1
a = int(input("Proszem wpisac liczbu zdobytych punktow\n"))
if a>80:
    print("Student zalicza egzamin w terminie 0")
elif 50<=a<=80:
    print("Student mogą poprawić jego wynik")
else:
    print("Student muszą go poprawić")

#Zad.2
temp=int(0)
x = int(input("Proszem wpisac X\n"))
y = int(input("Proszem wpisac Y\n"))
z = int(input("Proszem wpisac Z\n"))
if x>y:
    temp = x
    x=y
    y=temp
if y>z:
    temp = y
    y = z
    z = temp
if x > y:
    temp = x
    x=y
    y=temp
print (x,y,z)

#Zad. 3
Nazwa_pliku = ("Raport_maj.xlsx")
if Nazwa_pliku.endswith(".xlsx"):
    print("Tak")
else:
    print("Nie")

#Zad. 4
gol = int(input("Proszem wpisac liczbu golow\n"))
bonus=int(0)
summ=int(0)
if gol>5:
    bonus+=5
if gol>10:
    bonus+=10
summ=summ+10*gol+bonus
print (summ)

#Zad. 5
try:
    with open("notowanie_gieldowe.txt","r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error")
try:
    with open("notowanie_gieldowe.txt","a") as file:
        file.write("\nALR, 113")
    with open("notowanie_gieldowe.txt","r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error")