import random
from time import time

def partition( a,s, e):  
    pivot, ptr = a[(s+e)//2], s
    for i in range(s, e):
      if a[i] < pivot:
        a[i], a[ptr] = a[ptr], a[i]
        ptr += 1
    a[ptr], a[e] = a[e], a[ptr]
    return ptr

def quick_sort(a,s,e):
  if s<e:
    #a[e//2], a[e] = a[e] , a[e//2] 
    p= partition(a,s,e)
    quick_sort(a,s,p-1)
    quick_sort(a,p+1,e)
  return 
  


 
def randVet(x):
    v = []
    return list(range(x))

def medirTempo(v):
  v.sort()
  s = time()
  quick_sort(v,0, len(v)-1)
  return time() - s



def main():
  for i in range(100, 1001,100):
    #10 vetores q começa com tamnho 100 e aumeta de 100 ao tamnho anterior a cada repetição
    soma = 0
    #soma do tempo dos 10vetores
    for j in range(0,10):
      v = randVet(i)
      e=medirTempo(v) 
      soma+=e
    media = soma/10
    print(f"{i} {media}")

main()
