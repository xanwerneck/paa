#-*- coding: utf-8 -*-
#
#K(w,j) = \max \{ K(w-w_{j}, j-1) + v_{j}, K(w, j-1)  \} .
#O algoritmo consiste em preencher uma tabela bidimensional, com 
# W+1 linhas e n+1 colunas. 
#Apesar da tabela agora ser muito maior que no caso ilimitado, 
#o tempo de execução será o mesmo, pois cada chamada leva um tempo fixo de 
# O(n) e W chamadas são feitas, então 
#o tempo total será de O(nW).

#### REFERENCES ####
# 1 - https://pt.wikipedia.org/wiki/Problema_da_mochila
# 2 - https://rjlipton.wordpress.com/2009/02/13/polynomial-vs-exponential-time/


def integer_knap(instances, W, n):
  Solution = [[0 for x in range(n)] for y in range(W)] 
  

  # Solution[w][j] = max{Solution[w-wj][j-1] + vj , Solution[w][j-1]}
  # Solution[w-wj][j-1] + vj => Com o item j => melhor = Resultado anterior + j
  # Solution[w][j-1] => Sem o item j => melhor = Resultado anterior

  for j in range(n): # number of itens
    for w in range(W): # max weight
      if instances[j][1] > (w+1):
        Solution[w][j] = Solution[w][j-1]
      else:
        Solution[w][j] = max(Solution[w][j-1],  Solution[ w - instances[j][1] ][j-1]  + instances[j][0] )

  print Solution[W-1][n-1]

#### TEST CASE ####
# a[0] = (value = 10 / weight = 5)
a = [(10,5),(4,4),(4,3),(2,1)]
integer_knap(a, 10, 4)