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

# fun solve_sudoku4x4 board
#   is completed?
#       y -> True
#       n -> row, column = row, column of the next empty cell
#            for number = 1 to 4
#                is number valid?
#                   y -> board[row, column] = number
#                        is solve_sudoku4x4(board) True?
#                            y -> True
#                        board[row, column] = 0
#             endfor
#             -> False
#          
def solve_sudoku4x4(board):
    if is_complete(board):
        return True

    row, col = find_next_empty_cell(board)
    for num in range(1, 5):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku4x4(board):
                return True
            board[row][col] = 0

    return False

def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True

def find_next_empty_cell(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid(board, row, col, num):
    # wiersz
    if num in board[row]:
        return False

    # kolumna
    if num in [board[i][col] for i in range(4)]:
        return False

    # 2na2 siatka
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False

    return True

puzzle_1 = [
    [3, 0, 2, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 4]
]

if solve_sudoku4x4(puzzle_1):
    print("Rozwiązanie:")
    for row in puzzle_1:
        print(row)
else:
    print("Nie ma rozwiązania")
