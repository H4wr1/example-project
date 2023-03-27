#kwadrat

from calendar import c
import math

a = 10

obwod = a*4
pole = a*a

print("Obwówd kwadratu wynosi " + str(obwod) + ", a pole " + str(pole) + ".")

#prostokąt

a = 10
b = 5

obwod_prostokat = (a*2)+(b*2)
pole_prostokat = a*b

print("Obwód prostokątu wynosi " + str(obwod_prostokat) + ", a pole " + str(pole_prostokat) + ".")

#trapez

a = 4
b = 13
c = 9
d = 12
h = 12

obwod_trapez = a + b + c + d
pole_trapez = ((a+c)*h)/2

print("Obwód trapezu wynosi " + str(obwod_trapez) + ", a pole " + str(pole_trapez) + ".")

#koło

r = 4
pi_zmienna = math.pi
obwod_kolo = 2*pi_zmienna*r
pole_kolo = pi_zmienna*(r**2)

print("Obwód trapezu wynosi " + str(obwod_kolo) + ", a pole " + str(pole_kolo) + ".")

