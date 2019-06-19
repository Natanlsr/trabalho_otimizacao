from pulp import *

#Funcao para pegar todas linhas e colunas da matriz
def pegaLinhasEColunas(matriz):
    mat = []
    col = []
    for i in range(0,len(matriz),1):
        linhas = [];
        l =[]
        for j in range(0,len(matriz),1):
            linhas.append('M'+ str(i)+ '_' +str(j))
            l.append('M'+str(j) + '_' +str(i))
        mat.append(linhas)
        col.append(l)
    return mat,col
            

#Funcao para pegar todas diagonais da matriz
def pegaDiagonais(matriz):
    diagonais = []
    
    #Pegando esquerda para direita
    i = 0
    j = 0
    q = 0
    d = []
    
    while(True):
        if(q == len(matriz)-1):
            break
        d.append('M'+str(i) +'_' + str(j))
       
        if(i == len(matriz)-1 or j == len(matriz)-1):
            q += 1
            diagonais.append(d)
            d = []
            i = q
            j = 0
        else:     
            i += 1
            j += 1
   
    i = 0
    j = 1
    q = 0
    d = []
    while(True):
        if(q == len(matriz)-2):
            break
        d.append('M'+str(i) +'_' + str(j))
       
        if(i == len(matriz)-1 or j == len(matriz)-1):
            print(i,j)
            q += 1
            diagonais.append(d)
            d = []
            i = 0
            j = j - q
        else:     
            i += 1
            j += 1
    
    #Pegando da direita para a esquerda
    i = 0
    j = len(matriz) - 1
    q = 0
    d = []
    
    while(True):
        if(q == len(matriz)-1):
            break
        d.append('M'+str(i) +'_' + str(j))
       
        if(i == len(matriz)-1 or j == 0):
            q += 1
            diagonais.append(d)
            d = []
            i = q
            j = len(matriz) - 1
        else:     
            i += 1
            j -= 1

    i = 0
    j = len(matriz) - 2
    q = 0
    d = []

    while(True):
        if(q == len(matriz)-2):
            break
        d.append('M'+str(i) +'_' + str(j))
       
        if(i == len(matriz)-1 or j == 0):
            print(i,j)
            q += 1
            diagonais.append(d)
            d = []
            i = 0
            j = (len(matriz) - 2) - q
        else:     
            i += 1
            j -= 1
   
    print(diagonais)
        
    
        
        
        
            
        
    

def main():
    n = int(input("Digite o tamando do n: "))
    matriz = [0] * n
    matriz = [matriz] * n
    linhas,colunas = pegaLinhasEColunas(matriz)
    pegaDiagonais(matriz)
    #Modelagem usando pulp

if __name__ == '__main__':
    main()
