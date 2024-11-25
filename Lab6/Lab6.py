#Zad. 1
import keyword
import random
import time
from modules import geometria as g
print("Zadanie I")
print(g.obwod_kola(16))
print(g.pole_kola(16))
#Zad. 2
# pogoda.py
#Zad. 3
# cwiczenia.py
#Zad. 4
print("Zadanie IV")
print(f"Szczesliwa liczba to jest {random.randint(1,100)}")
rocznik=[2000,2001,2002,2003]
print(random.choice(rocznik))
#Zad. 5
print("Zadanie V")
k = list(range(1, 50))
print("Lista kul", k)
print("Wylosowane kule", sorted(random.sample(k, 6)))
#Zad. 6
print("Zadanie VI")
czas=int(input("Proszem wpisac sekundy\n"))
while czas>0:
    print(f"Pozostalo {czas} sekund")
    time.sleep(1)
    czas-=1
    if czas==0:
        print("Czas minal!")
#Zad. 7
print("Zadanie VII")
from datetime import datetime
lld = datetime(2024, 11, 19)
ed = datetime(2024, 12, 17)
cd = datetime.now()
dsll = (cd - lld).days
due = (ed - cd).days
mn = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
print(f"Days since the last laboratory: {dsll} days")
print(f"Days until the exam: {due} days ({mn[ed.month]})")
#Zad. 8
print("Zadanie VIII")
words=["for","print","break","bad"]
for i in range(0,len(words)):
    if keyword.iskeyword(words[i])==0:
        print(f"{words[i]} nie jest keywordem")
    else:
        print(f"{words[i]} jest keywordem")
#Zad. 9
import math
print("Zadanie IX")
print(dir(math))
#Zad.10
print("Zadanie X")
s = int(input("Enter the start of range"))
e = int(input("Enter the end of range:"))
tl = []
for i in range(10):
    tl.append(random.randint(s,e))
n = tuple(tl)
print("Generated tuple:", n)
p = 1
for num in n:
    p *= num
gm = p ** (1 / len(n))
print("geometric_mean:", gm)
