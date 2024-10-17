import random
import math

# A) Sprawdź w interpreterze typ wyników określonych działań - type( x ) i wyjaśnij, co
# oznaczają poszczególne operatory?
print(type(1 + 2)) #<class 'int'>
print(type(1 + 4.5)) #<class 'float'>
print(type(3 / 2)) #<class 'float'>
print(type(4 / 2)) #<class 'float'>
print(type(3 // 2)) #<class 'int'>
print(type(-3 // 2)) #<class 'int'>
print(type(11 % 2)) #<class 'int'>
print(type(2 ** 10)) #<class 'int'>
print(type(8 ** (1/3))) #<class 'float'>

# B) Sprawdź i wyjaśnij działanie następujących instrukcji:
print('------------------------ \n')

print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))


print("------------------")
#Zad. 2:
#Do zmiennej o nazwie uczelnia przypisz zdanie Studiuję na WSIiZ, Następnie korzystając z
#funkcji print() wydrukuj ten tekst do konsoli.
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)


#Zad. 3:
#Podane są poniższe zmienne:
imię = "Jan"
wiek = 30
wzrost = 175

print(f"Nazywam się {imię} i mam {wiek} lat.\nMój wzrost to {wzrost} cm")

#Zad. 4:
#Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat przypisz
#wartość 0.2 (rabat 20%). Następnie policz cenę tego produktu po zastosowaniu podanego
#rabatu. Wynik wydrukuj do konsoli. Zwróć uwagę na odpowiednie formatowanie tekstu w
#funkcji print() tak, aby końcowa cena produktu została wyświetlona tylko do drugiego
#miejsca po przecinku.

Cena = 39.99
Rabat = 0.2
discountedPrice = Cena * (1 - Rabat)
print(f"Price with discount: {discountedPrice:.2f} PLN")


#Zad. 5:
#Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
#oraz wyświetla wyniki na ekranie.
length = float(input("Insert the length of rectangle: "))
width = float(input("Insert the width of rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area of rectangle: {area}")
print(f"perimeter of rectangle: {perimeter}")

#Zad. 6:
#Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
#spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o
#szacowanych kosztach podróży (cena paliwa 6.5 zł/l).
#A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo
#(liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr.
#B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.

distance = random.randint(50, 500) 
average_fuel_consumption = float(input("Insert average fuel consumption (L/100 км): "))
fuel_price = float(input("Insert the fuel price for 1 liter (zl): "))

fuel_used = (distance / 100) * average_fuel_consumption  
trip_cost = fuel_used * fuel_price  

print(f"Distance: {distance} км")
print(f"Average fuel consumption: {average_fuel_consumption:.2f} L/100 км")
print(f"Fuel used: {fuel_used:.2f} л")
print(f"Trip cost: {trip_cost:.2f} zł")

#Zad. 7:
#Narysuj schemat blokowy algorytmu i napisz program rozwiązywania rownania
#liniowego ax + b = 0 , gdzie a i b są wspołczynnikami podawanymi przez uzytkownika

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))

if a == 0:
    if b == 0:
        print("Equation has infinitely many solutions")
    else:
        print("Equation has no solution")
else:
    x = -b / a
    print(f"Solution of equation: x = {x}")

#Zad. 8:
#Narysuj schemat blokowy algorytmu i napisz program rozwiązywania rownania
#kwadratowego ax2 + bx + c = 0, gdzie a, b i c są wspołczynnikami podawanymi przez
#uzytkownika.

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Equation has two roots: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"Equation has one root: x = {x}")
else:
    print("Equation has no roots")


#Zad. 9:
#Napisz kalkulator, który wyświetli wyniki dodawania, odejmowania, mnożenia, dzielenia i
#potęgowania 2 liczb podanych przez użytkownika.

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 != 0 else "Cannot divide by zero"
power = number1 ** number2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Power: {power}")
