#Zad. 1
import keyword
import random
import time
import geometria as g
print("Zadanie I")
print(g.obwod_kola(16))
print(g.pole_kola(16))
#Zad. 4
print("Zadanie IV")
print(f"Szczesliwa liczba to jest {random.randint(1,100)}")
rocznik=[2000,2001,2002,2003]
print(random.choice(rocznik))
#Zad. 5
print("Zadanie V")
rn=random.sample(range(1,50),6)
print(rn)
#Zad. 6
print("Zadanie VI")
czas=int(input("Proszem wpisac sekundy\n"))
while czas>0:
    print(f"Pozostalo {czas} sekund")
    time.sleep(1)
    czas-=1
    if czas==0:
        print("Czas minal!")
#Zad. 8
print("Zadanie VIII")
print(keyword.iskeyword("for"))
print(keyword.iskeyword("print"))
print(keyword.iskeyword("break"))
print(keyword.iskeyword("done"))
print(keyword.iskeyword("bad"))
#Zad. 9
print("Zadanie IX")
import math
print(dir(math))
