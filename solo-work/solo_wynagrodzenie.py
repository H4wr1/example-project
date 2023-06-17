
import csv
import math
class Pracownik:
    fundusz_praca = (2.45/100)
    fundusz_gsb = (0.10/100)
    ube_emerytalne = (9.76/100)
    ube_rentowe = (1.5/100)
    ube_rentowe_pracodawca = (6.5/100)
    ube_wypadkowe = (1.67/100)
    ube_chorobowe = (2.45/100)
    ube_zdrowotne = (9/100)
    koszty_uzysk_przych = 250
    zaliczka_podatek = (12/100)
    pomniejsz_zaliczka = 300
    def __init__(self, imie, nazwisko, wiek, wyn_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wyn_brutto = wyn_brutto
        
        
    def __str__(self):
        pass
    
    def obliczskladki(self):
        return self.wyn_brutto*Pracownik.ube_chorobowe + Pracownik.ube_rentowe*self.wyn_brutto + Pracownik.ube_emerytalne*self.wyn_brutto
    def obliczskladkazdrowotna(self):
        return (self.wyn_brutto - self.obliczskladki())*Pracownik.ube_zdrowotne
    def podstawapodatku(self):
        return self.wyn_brutto - self.obliczskladki() - Pracownik.koszty_uzysk_przych
    def zaliczkapodatku(self):
        return round(self.podstawapodatku()*Pracownik.zaliczka_podatek)-self.pomniejsz_zaliczka
    def oblicznetto(self):
        #self.wyn_netto = self.wyn_brutto - self.obliczskladki() - self.obliczskladkazdrowotna() - self.zaliczkapodatku()
        if self.wiek <= 26:

            return self.wyn_brutto - self.obliczskladki() - self.obliczskladkazdrowotna() 
        else:
            return self.wyn_brutto - self.obliczskladki() - self.obliczskladkazdrowotna() - self.zaliczkapodatku()
    def kosztpracodawcy(self):
        #self.wyn_netto = self.wyn_brutto - self.obliczskladki() - self.obliczskladkazdrowotna() - self.zaliczkapodatku()
        return self.wyn_brutto*Pracownik.ube_emerytalne + self.wyn_brutto*Pracownik.ube_rentowe_pracodawca + Pracownik.ube_wypadkowe*self.wyn_brutto + self.wyn_brutto*Pracownik.fundusz_praca + self.wyn_brutto*Pracownik.fundusz_gsb
    def razemkosztpracodawcy(self):
        return self.wyn_brutto+self.kosztpracodawcy()
    
    
#Pracownik1 = Pracownik("Mikolaj", "Hawryluk", 27, 3490)

#print(Pracownik1.razemkosztpracodawcy())
pracownicy = []
with open('data/salary.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 
    for row in csv_reader:
        imie, nazwisko, wyn_brutto, wiek = row
        pracownik = Pracownik(imie, nazwisko, int(wiek), int(wyn_brutto))
        pracownicy.append(pracownik)

print("Wynagrodzenia netto:")
for pracownik in pracownicy:
    print(f"{pracownik.imie} {pracownik.nazwisko}: {pracownik.oblicznetto()}")  
print()  
print("Razem koszty pracodawcy:")
for pracownik in pracownicy:
    print(f"{pracownik.imie} {pracownik.nazwisko}: {pracownik.razemkosztpracodawcy()}")    