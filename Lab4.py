#Zad. 1
lst=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
lst.append(100) or print(lst)
lst.insert(11,0) or print(lst)
lst.extend(lst) or print(lst)
lst.remove(0) or print(lst)
lst.pop(-1) or print(lst)
lst.clear() or print(lst)
lst=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(lst[0])
print(lst[1:5:])
lst.sort() or print(lst)
lst.reverse() or print(lst)
#Zad. 2
list=["Chloe","Abraham","James","Kate"]
#A.)
list.sort() or print(list)
#B.)
list.pop(-1) or print(list)
list.append("Jack")
list.append("Michael") or print(list)
#C.)
list.insert(3, "Mike") or print(list)
#D.)
print(list[-1::-1])
list.extend(list) or print(list)
#Zad. 3
#A.)
name=input()
print(f"Witaj {name}")
#B.)
age=input()
print(f"Twoj wiek to: {age}")
#C.)
ini=input()
print(ini)
#D.)
str=input()
for i in range(0,5):
    print(str)
#E.)
str1 = input("Wprowadź pierwszy łańcuch: ")
str2 = input("Wprowadź drugi łańcuch: ")
str3 = str1 + str2
print("Połączony łańcuch:", str3)
#F.)
str1 = input("Wprowadź pierwszy łańcuch: ")
str2 = input("Wprowadź drugi łańcuch: ")
half1 = str1[:len(str1)//2]
half2 = str2[len(str2)//2:]
str3 = half1 + half2
print("Połączony łańcuch:", str3)
#Zad. 4
import string
zdanie = input("Wprowadź zdanie: ")
litery = [char.lower() for char in zdanie if char.isalpha()]
litery_posortowane = tuple(sorted(litery))
print("Posortowane litery w zdaniu:", litery_posortowane)
alfabet = set(string.ascii_lowercase)
litery_w_zdaniu = set(litery)
brakujace_litery = alfabet - litery_w_zdaniu
print("Brakujące litery w zdaniu:", tuple(sorted(brakujace_litery)))
#Zad. 5
dni_tygodnia = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
print(dni_tygodnia)
#Zad. 6
owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')
liczba_bananow = owoce.count('banan')
print("Liczba wystąpień 'banan':", liczba_bananow)
#Zad. 7
moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)
moja_lista = list(moja_krotka)
moja_lista.sort()
posortowana_krotka = tuple(moja_lista)
print("Posortowana krotka:", posortowana_krotka)
#Zad. 8
stopnie = ("Szeregowy", "Kapral", "Sierżant", "Porucznik", "Kapitan", "Major", "Pułkownik")
ilość_stopnii = len(stopnie)
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie
print(ilość_stopnii)
print(Major_index)
print(Pułkownik_wstepowanie)
#Zad. 9
zakupy = {
    "Mleko": 3.50,
    "Chleb": 2.20,
    "Jajka": 4.00,
    "Masło": 5.50,
    "Ser": 7.30
}
print("Lista zakupów:", zakupy)
suma_wydatkow = sum(zakupy.values())
print("Podsumowanie wydatków:", suma_wydatkow)
