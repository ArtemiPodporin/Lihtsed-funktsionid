
#10
from math import *
print("Ajateisendus")
a=float(input("Sinu valem leiab ja v�ljastab tunnid ja minutid"))
t=int(a//60)
sec=int(a/60)
print(f"ainutes{t}:sekundid {sec}" )

#9
from math import *
from random import *
print("Rulluisutajad")
print("Rulluisutaja keskmine kiirus on 29,9km/h")
a=24/60
b=a*29.9
b=round(b,2)
print(f"Vastus: {b}km")

#8
from math import *
print("K�tusekulu arvutamine")
l=float("Kasutaja sisestab tangitud k�tuse liitrid")
km=float("Kasutaja sisestab l�bitud kilomeetrid")
p=l/km*100
print(str(f"Vastus: {p}l/km"))


#7
from math import *
print("V�tsite 3 s�braga suure pitsa hinnaga 12,90� J�tate teenindajale 10% jootraha")
s=10*12,90/100
s=round(s)
d=(12.90+s)
print(f"Vastus: {d}")
p=d/3
p=round(p,1)
print (str(f"iga lollpea peab: {p}�"))

#6
from random import *
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"K�lg a={a}\nk�lg b={b}\nk�lg c={c}")
print("kolmnurga �mberm��t={a+b+c}")

#5
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print(" ^^ "'"'" ^^  ")

#4
from math import *
print("aritmeetilise keskmise suvalises")
a=int(input("Sisesta 1. arv =>"))
b=int(input("Sisesta 2. arv =>"))
c=int(input("Sisesta 3. arv =>"))
d=int(input("Sisesta 4. arv =>"))
e=int(input("Sisesta 5. arv =>"))
S=(a+b+c+d)/5
print("Keskmine on: {S}")

#3
aeg=float(input("Mitu tundi kulus s�iduks? "))
teepikkus=float(input("Mitu kilomeetrit s�itsid? "))
kiirus=aeg / teepikkus
print()
print("Sinu kiirus oli " + str(round(kiirus)) + " km/h")

#2
from math import *
print("Ristk�likukujulise maat�ki diagonaal")
N=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
M=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maat�ki diagonaal on {d} m**2")


#1
from math import *
print("Puu l�bim��du arvutamine")
C=float(input("Puu �mberm��t: "))
d=2*(C/(2*pi))
print(f"Vastus:\npuu l�bim��duga {C} �mberm��t v�edub {d}")

