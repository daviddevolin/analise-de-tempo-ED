import random
from time import time

def insertion_sort(v,n):
    k = 0
    j = 0
    
    for i in range (1,n):
        k = v[i]
        j = i-1
        while j >= 0 and v[j] > k:
            v[j+1] = v[j]
            j = j - 1
        v[j+1] = k
    return v
     
def randVet(x):
    v = []
    for i in range(x):
        v.append(random.randint(0,100))
    return v

def medirTempo(v):
  v.sort()
  v.reverse()
  s = time()
  insertion_sort(v, len(v))
  return time() - s
  


def main():
  for i in range(100, 1001,100):
    #10 vetores q começa com tamnho 100 e aumeta de 100 ao tamnho anterior a cada repetição
    soma = 0
    #soma do tempo dos 100vetores
    for j in range(0,10):
      v = randVet(i)
      e = medirTempo(v)
      soma += e
    media = soma/10
    print(f"{i} {media}")
    
        
main()

