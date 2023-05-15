from calendar import c

class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"
    def __int__(self):
        return 5
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)
class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
    
    def obwod(self):
        return self.a + self.b + self.c
    
    def pole(self):
        return (self.a*self.h_a)/2

class Romb:
    def __init__(self, a, h_a):
        self.a = a
        self.h_a = h_a
    
    def obwod(self):
        return 4*self.a 
    
    def pole(self):
        return (self.a*self.h_a)

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)

#print(trojkat_rownoboczny.obwod())
#print(trojkat_rownoboczny.pole())

romb_1 = Romb(10, 10)

#print(romb_1.obwod())
#print(romb_1.pole())

student_Mikolaj = Student("Mikołaj", "Hawryluk", 120040)
student_Mikolaj.dodaj_ocene(4.5)
print(student_Mikolaj.zwroc_srednia())

class Mieszkanie:
    def __init__(self, powierzchnia, wlasciciel, wartosc, typmieszkania, iloscpokoi, adres, czynasprzedaz, czyumeblowane):
        self.powierzchnia = powierzchnia
        self.wartosc = wartosc
        self.adres = adres
        self.czynasprzedaz = czynasprzedaz
        self.wlasciciel= wlasciciel
        self.typmieszkania = typmieszkania
        self.iloscpokoi = iloscpokoi
        self.czyumeblowane = czyumeblowane
    def __str__(self):
        return self.adres
    def wartosc_za_metr_kwadratowy(self):
        return self.wartosc/self.powierzchnia
    def oferta_sprzedazy(self):
        if (self.czynasprzedaz == True):
            return f"{self.typmieszkania}\n{self.powierzchnia}\n{self.adres}\nCena: {self.wartosc} zł\nDane właściciela: {self.wlasciciel}"
        else:
            return "Wystapil wyjątek: Mieszkanie nie jest na sprzedaż"
mieszkanie_1 = Mieszkanie(100, "Mikołaj Hawryluk", 100000, "Dom jednorodzinny", 5, "ul. Warszawska 349, 61-060 Poznań", True, False)
print(mieszkanie_1)
print(mieszkanie_1.wartosc_za_metr_kwadratowy())
print(mieszkanie_1.oferta_sprzedazy())