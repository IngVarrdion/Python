#Zad.1
f=100
ft=10
t=0
while f>0:
    print(f"\nFuel:{f}\nFuel per second:{ft}\nTime:{t}\n")
    f-=ft
    t+=1
print(f"Fuel:{f}\nFuel per second:{ft}\nTime:{t}")
print("Koniec lotu")

#Zad.2

#Zad.3
a=0
bloki=1
lokali=1
Streets=["Jagodowa","Lipowa","Kwiatowa","Kasztanowa","Polna"]
while a>=0:
    if lokali<=10:
        print(f"{Streets[a]},{bloki},{lokali}")
        lokali+=1
    if bloki==5 and lokali==11:
        a+=1
        bloki=1
        lokali=1
    if lokali==11:
        bloki+=1
        lokali=1
    if a==4 and lokali==10 and bloki==5:
        a=-1
        print(f"{Streets[a]},{bloki},{lokali}")

#Zad.4
x=input("Liczbe gosci:\n")
n=input("Liczbe dan:\n")

#Zad.5
for i in range(80, -1, -4):
    print(i)

#Zad.6
o=0
while o==0:
    l = int(input("Dowolna liczbe:\n"))
    if l<0:
        o=1

#Zad.7
#A.)

#B.)

#Zad.8
txt="Python jest super"
print(txt[0])
print(txt[-1])
print(txt[0::2])
print(txt[1::3])
print(txt[10::])
print(txt[-1:0:-1])

#Zad.9
name="Ihor"
print(f"Hello{name}")
age=17
print(f"Your age:{age}")
