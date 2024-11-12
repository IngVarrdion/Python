#Zad. 1
def quadr(x):
    x=x**2
    print(x)
x=float(input("Enter a number:\n"))
quadr(x)
#Zad. 2
def flip(a):
    a=a[::-1]
    print(a)
a=str(input("Enter your string:\n"))
flip(a)
#Zad. 3
def Greeting(name,lang):
    if lang == "Polish":
        print(f"Cześć, {name}")
    elif lang == "English":
        print(f"Hello, {name}")
    elif lang == "German":
        print(f"Guten Morgen, {name}")
    else:
        print(f"Witaj, {name}")

name=str(input("Enter your name:\n"))
lang=str(input("Enter your native language: \n"))
Greeting(name, lang)
#Zad. 4
def mid(lst):
    if len(lst) == 0:
        print("List is empty!")
    else:
        print(sum(lst) / len(lst))
lst = [10, 20, 30, 40, 50]
mid(lst)
#Zad. 5
def BMI(mass, height):
    bmi=mass/(height**2)
    if bmi <=18.5:
        print("Niedowaga")
    elif bmi>18.5 & bmi<25:
        print("Pozadana masa ciala")
    elif bmi>=25 & bmi<30:
        print("Nadwaga")
    elif bmi>=30 & bmi<35:
        print("Otyslosc I stopnia")
    elif bmi>=35 & bmi<40:
        print("Otyslosc II stopnia")
    elif bmi>=40:
        print("Otyslosc III stopnia")
mass=int(input("Please, enter your mass:\n"))
height=int(input("Please, enter your height:\n"))
BMI(mass, height)
#Zad. 6
import math
def tri(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki trójkąta muszą być dodatnie.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Boki nie spełniają nierówności trójkąta.")
        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return pole
    except ValueError as ve:
        return f"Błąd: {ve}"
    except Exception as e:
        return f"Nieoczekiwany błąd: {e}"
a = input("a:\n")
b = input("b:\n")
c = input("c:\n")
pole = tri(a, b, c)
print(f"Pole trójkąta o bokach {a}, {b}, {c} wynosi: {pole}")
#Zad. 7
def potega(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * potega(a, n - 1)
    else:
        return 1 / potega(a, -n)
a = float(input("Podaj liczbę a: "))
n = int(input("Podaj wykładnik n: "))
wynik = potega(a, n)
print(f"{a} do potęgi {n} wynosi: {wynik}")
#Zad. 8
#A.)
def var(*args):
    for arg in args:
        print(arg)
var(1, 2, 3, "hello", True)
#B.)
def maximal(*args):
    if args:
        return max(args)
    else:
        return None
max1 = maximal(1, 5, 3, 9, 2)
print("Maksymalna wartość:", max1)
#Zad. 9
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
print(f"{n}-ty wyraz ciągu Fibonacciego to:", fibonacci(n))

n = 5
print(f"{n}-ty wyraz ciągu Fibonacciego to:", fibonacci(n))
#Zad. 10
def wspolne_wartosci(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)
    wspolne = set1 & set2
    return list(wspolne)
seq1 = [1, 2, 3, 4, 5]
seq2 = [3, 4, 5, 6, 7]
wspolne = wspolne_wartosci(seq1, seq2)
print("Wspólne wartości:", wspolne)
