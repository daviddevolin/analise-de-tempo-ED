import random
from time import time
def merge(A, aux, s, m, e):
    
    for k in range(s, e + 1):
        aux[k] = A[k]
    i = s
    j = m + 1
    for k in range(s, e + 1):
        if i > m:
            A[k] = aux[j]
            j += 1
        elif j > e:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1


def merge_sort(A, aux, s, e):
  if e <= s:
    return
  m = (s + e) // 2

  # Ordena a primeira metade do arranjo.
  merge_sort(A, aux, s, m)

  # Ordena a segunda metade do arranjo.
  merge_sort(A, aux, m + 1, e)

  # Combina as duas metades ordenadas anteriormente.
  merge(A, aux, s, m, e)


def randVet(x):
  v = []
  for i in range(x):
    v.append(random.randint(0,100))
  return v

def medirTempo(v):
  aux = [0] * len(v)
  s = time()
  merge_sort(v,aux,0,len(v)-1)
  return time() - s
  print(v)


def main():
  for i in range(100, 1001,100):
    #10 vetores q começa com tamnho 100 e aumeta de 100 ao tamnho anterior a cada repetição
    soma = 0
    #soma do tempo dos 10vetores
    for j in range(0,10):
      v = randVet(i)
      e = medirTempo(v)
      soma += e
    media = soma/10
    print(f"{i} {media}")

    
main()
