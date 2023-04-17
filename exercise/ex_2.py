# Import math Library
import math

# Print the value of pi
print (math.pi)

def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole


# kwadrat, prostokat dla studenta 1
def kwadrat(bok):
    # TODO
    return 0, 0


def prostokat(bok_a, bok_b):
    # TODO
    return 0, 0

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    # TODO
    return 0, 0

def romb(bok, wysokosc):
    # TODO
    return 0, 0

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    # TODO
    return 0, 0


def kolo(promien):
    # TODO
    return 0, 0


# assert trojkat(10, 15, 16, 8) == (41, 40)
# assert kwadrat(20) == (80, 400)
# assert prostokat(12, 10) == (44, 120)
# assert rownoleglobok(6, 5, 2) == (22, 12)
# assert romb(10, 5) == (40, 50)
# assert trapez(10, 15, 7, 14, 2) == (45, 25)
# TODO na koniec (na wyraźne polecenie prowadzącego)! 
# Dla każdej figury powinny znajdować się dwa testy