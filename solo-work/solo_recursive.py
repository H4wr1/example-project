# fun sum l
#   is empty?
#       y -> 0
#       n -> l(0)+sum(reszta)
def sum_of_list(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0] + sum_of_list(lista[1:]) 
lista1 = [1, 3, 4, 2, 5]
print("Suma elementów listy {}: {}".format(lista1, sum_of_list(lista1)))

# fun factorial n
#   is 1?
#       y -> n
#       n -> n*factorial(n-1)
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)
factorial1 = 4
print("Silnia dla liczby {}: {}".format(factorial1, factorial(factorial1)))

# fun find_max l
#   is 1?
#       y->l(0)
#       n -> is l(0)>find_max(reszta)?
#               y->l(0)
#               n-> l(reszta)  
def find_max(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], find_max(lista[1:]))
    
lista2 = [1, 3, 4, 2, 5]
print("Maksymalna wartość dla listy {}: {}".format(lista2,find_max(lista2)))

# fun fibonacci n
#   is smaller or equal to 1?
#       y->n
#       n -> fibonacci(n-1)+fibonacci(n-2)
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

fibo1 = 8
print("Ciąg fibonacciego, pierwsze {} liczb:".format(fibo1))
for i in range(fibo1):
    print(fibonacci(i))
# fun rozw_suodku4x4 board
#   is solved?
#       y->True
#       n -> 
def rozwiaz_sudoku4x4(plansza):
    if czy_rozwiazane(plansza):
        return True

    wiersz, kolumna = nastepna_pusta_komorka(plansza)
    for liczba in range(1, 5):
        if czy_prawidlowa(plansza, wiersz, kolumna, liczba):
            plansza[wiersz][kolumna] = liczba
            if rozwiaz_sudoku4x4(plansza):
                return True
            plansza[wiersz][kolumna] = 0

    return False

def czy_rozwiazane(plansza):
    for wiersz in plansza:
        if 0 in wiersz:
            return False
    return True

def nastepna_pusta_komorka(plansza):
    for wiersz in range(4):
        for kolumna in range(4):
            if plansza[wiersz][kolumna] == 0:
                return wiersz, kolumna
    return None, None

def czy_prawidlowa(plansza, wiersz, kolumna, liczba):
    # Check row
    if liczba in plansza[wiersz]:
        return False

    # Check column
    if liczba in [plansza[i][kolumna] for i in range(4)]:
        return False

    # Check 2x2 grid
    start_row = (wiersz // 2) * 2
    start_col = (kolumna // 2) * 2
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if plansza[i][j] == liczba:
                return False

    return True

plansza = [
    [0, 1, 0, 0],
    [3, 0, 0, 1],
    [4, 0, 0, 2],
    [0, 0, 4, 0]
]

if rozwiaz_sudoku4x4(plansza):
    print("Rozwiązanie:")
    for wiersz in plansza:
        print(wiersz)
else:
    print("Nie ma rozwiązania")
