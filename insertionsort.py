import time
import random

def inse_so(li,tam):
    t1 = time.clock()
    for j in range(tam):
        vl = li[j]
        i=j-1
        while i>=0 and li[i] > vl:
            li[i+1]=li[i]
            i=i-1
        li[i+1]=vl
     
        
    print li
    print time.clock()-t1
    
   
    

def inicio():
    tam = input ("ingrese\n")
    li = []

    for i in range(tam):
        li.append(random.randint(0,(tam)))

    print li

    print ("Lista Ordenada: ")
    inse_so(li,tam)
    


inicio()
