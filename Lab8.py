import numpy as n
import matplotlib.pyplot as p
#Zad. 1
kategorie =['Zywnosc', 'Odziez', 'Meble', 'Materialy pismienne']
wartosci = [100000, 20000, 10500, 20500]
p.bar(kategorie, wartosci)
p.show()
#Zad. 2
udzial=[]
for i in range(len(kategorie)):
    udzial.append((wartosci[i]/sum(wartosci))*100)
p.pie(udzial,labels=kategorie,autopct='%1.f%%',startangle=90,colors=['skyblue','lightgreen','lightcoral','gold'])
p.title('Procentowy udzial roznych kategorii')
p.show()
#Zad. 3
x=[1,2,3,4,5,6,7,8,9,10]
y=[9,18,24,30,35,38,42,44,45,46]
p.scatter(x,y)
p.show()
#Zad. 4
print("IV")
weights_list = [2**i for i in range(7, -1, -1)]  # [128, 64, 32, 16, 8, 4, 2, 1]
Weights = n.array(weights_list)
bin_count = n.random.randint(0, 2, 8)
def bin_value(weights, bin_count):
    return n.dot(weights, bin_count)
print("Weights:", Weights)
print("bin_count:", bin_count)
decimal_value = bin_value(Weights, bin_count)
print("Decimal value:", decimal_value)
#Zad. 5
print("V")
matrix = n.random.randint(0, 100, size=(5, 5))
max_value = matrix.max()
min_value = matrix.min()
max_in_rows = matrix.max(axis=1)
max_in_columns = matrix.max(axis=0)
sum_in_rows = matrix.sum(axis=1)
print(matrix)
print(max_value)
print(min_value)
print(max_in_rows)
print( max_in_columns)
print(sum_in_rows)
#Zad. 6
print("VI")
m=[
    [0,0,0],
    [1,1,0],
    [1,1,0]
]
print(m)
m=[
    [0,0,1],
    [0,0,1],
    [0,0,1]
]
print(m)
m1=[
    [1,1,1],
    [1,1,1],
    [0,0,0]
]
print(m)
m=[
    [1,0,0],
    [1,0,0],
    [0,0,0]
]
print(m)
m=[
    [1,0,1],
    [1,0,1],
    [0,0,0]
]
print(m)
#Zad. 7
import math
print("VII")
m=[
    [0,1,0],
    [1,0,1],
    [0,1,0]
]
def rev(m):
    for i in range((len(m))**2):
        r=i%len(m)
        c=math.floor(i/len(m))
        if m[r][c]==0:
          m[r][c]=1
        else:
           m[r][c]=0
        if i==2 or i==5:
           c+=1
    return m
print(rev(m))
#Zad. 8
print("VIII")
m = n.random.randint(0, 100, size=(5, 5))
print("Macierz 5x5:")
print(matrix)
greater_than_20 = matrix[matrix > 20]
count_greater_than_20 = greater_than_20.size
mean_value = matrix.mean()
print("\nElementy wieksze niż 20:", greater_than_20)
print("Liczba elementow wiekszych niz 20:", count_greater_than_20)
print("Srednia wartosc dla calej tablicy:", mean_value)
