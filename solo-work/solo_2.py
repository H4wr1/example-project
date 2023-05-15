from calendar import c


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

print(trojkat_rownoboczny.obwod())
print(trojkat_rownoboczny.pole())

romb_1 = Romb(10, 10)

print(romb_1.obwod())
print(romb_1.pole())