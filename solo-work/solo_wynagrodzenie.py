
import csv
class Pracownik:
    def __init__(self, imie, nazwisko, wyn_brutto, ube_emerytalne, ube_rentowe, ube_chorobowe, ube_wypadkowe, miejsce_zamieszkania, ppk, zaliczka_podatku):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wyn_brutto = wyn_brutto
        self.ube_chorobowe = ube_chorobowe
        self.ube_emerytalne = ube_emerytalne
        self.ube_rentowe = ube_rentowe
        self.ube_wypadkowe = ube_wypadkowe
        self.miejsce_zamieszkania = miejsce_zamieszkania
        self.ppk = ppk
        self.zaliczka_podatku = zaliczka_podatku

    def __str__(self):
        pass
    def oblicznetto(self):
        return 0
    def obliczskladki(self):
        return self.ube_chorobowe*self.wyn_brutto + self.ube_rentowe*self.wyn_brutto+self.ube_emerytalne*self.wyn_brutto
    def obliczkoszty(self):
        return 0
    #def zaliczka_podatku(self):
        #return self.wyn_brutto -  - self.mie
    
    file = open(r"C:\Users\75131\example-project\data\salary.csv", "r")
    pracownicy = list(csv.reader(file, delimiter=","))
    file.close()
    for pracownik in pracownicy:
        pracownik1 = Pracownik
        print("Pracownik Kowalski: ")
        print("- pensja brutto: ")
        print("- pensja netto: ")
        print("- koszt pracodawcy: ")
        print("- koszt całkowity: ")

    print("Suma kosztów wynosi: xxx")
