#Zad. 1A
print(type(1+2))#<class 'int'>
print(type(1+4.5))#<class 'float'>
print(type(3/2))#<class 'float'>
print(type(4/2))#<class 'float'>
print(type(3//2))#<class 'int'>
print(type(-3//2))#<class 'int'>
print(type(11%2))#<class 'int'>
print(type(2**10))#<class 'int'>
print(type(8**(1/3)))#<class 'float'>

#B
print(int(3.0))#3
print(float(3))#3.0
print(float("3"))#3.0
print(str(12.4))#12.4
print(bool(0))#False

#Zad. 2
uczelnia = ("Studiuje na WSIiZ")
print(uczelnia)

#Zad. 3
imie = "Jan"
wiek = 20
wzrost = 178
print(f"Nazyvam sie {imie} i mam {wiek} lat.Moj wzrost to {wzrost}")#Nazyvam sie Jan i mam 20 lat.Moj wzrost to 178

#Zad. 4
cena = float(39.99)
rabat = 0.2
koncowacena = float(cena*(1-rabat))
print(f"{koncowacena:.2f}")

#Zad. 5