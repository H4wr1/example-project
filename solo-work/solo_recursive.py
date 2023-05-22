# fun sum l
#   is empty?
#       y->0
#       n->l(0)+sum(reszta)
def sum_of_list(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0] + sum_of_list(lista[1:]) 
print(sum_of_list([1, 3, 4, 2, 5]))

# fun factorial n
#   is 1?
#       y->n
#       n->n*factorial(n-1)
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

print(factorial(4))

# fun find_max l
#   is 1?
#       y->l(0)
#       n->maximumof(l(0),find_max(reszta))
def find_max(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0],find_max(lista[1:]))
print(find_max([1, 3, 4, 2, 5]))