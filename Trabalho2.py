from pulp import *
from random import randrange, uniform
import math

#Funcao para verificar se matriz(nas linhas e colunas) satifaz as restricoes
def verificaLinhasColunas(matriz):
    for i in range(0,len(matriz),1):
        total_linha =0
        total_coluna = 0
        for j in range(0,len(matriz),1):
            total_linha += matriz[i][j]
            total_coluna += matriz[j][i]
        #print(total_linha)
       #print(total_coluna)
        if(total_linha > 1 or total_coluna > 1):

            return False
    return True
            

#Funcao para verificar se matriz(diagonais) satifaz as restricoes
def VerificaDiagonais(matriz):    
    #Pegando esquerda para direita
    i = 0
    j = 0
    q = 0
    total = 0
    while(True):
        total += matriz[i][j]
        if(total > 1):
            return False
        if(q == len(matriz)-1):
            break
        
       
        if(i == len(matriz)-1 or j == len(matriz)-1):
            q += 1
            i = q
            j = 0
            total = 0
        else:     
            i += 1
            j += 1
   
    i = 0
    j = 1
    q = 0
    total = 0
    while(True):
        total += matriz[i][j]
        if(total > 1):
            return False
        if(q == len(matriz)-2):
            break
        
        if(i == len(matriz)-1 or j == len(matriz)-1):
            q += 1
            i = 0
            j = j - q
            total = 0
        else:     
            i += 1
            j += 1
    
    #Pegando da direita para a esquerda
    i = 0
    j = len(matriz) - 1
    q = 0
    total = 0
    while(True):
        total += matriz[i][j]
        if(total > 1):
            return False
        if(q == len(matriz)-1):
            break
        
        if(i == len(matriz)-1 or j == 0):
            q += 1
            i = q
            j = len(matriz) - 1
            total = 0
        else:     
            i += 1
            j -= 1

    i = 0
    j = len(matriz) - 2
    q = 0
    total = 0
    while(True):
        total += matriz[i][j]
        if(total > 1):
            return False
        if(q == len(matriz)-2):
            break
        
        if(i == len(matriz)-1 or j == 0):
            q += 1
            i = 0
            j = (len(matriz) - 2) - q
            total = 0
        else:     
            i += 1
            j -= 1
   
    return True
        
def quantidadeDama(matriz):
    q = 0
    n = len(matriz)
    for i in range(0,n,1):
        for j in range(0,n,1):
            q+= matriz[i][j]
    return q
   
def main():
    n = int(input("Digite o tamando do n: "))
    matriz = []
    for i in range(0,n,1):
        linha = [0]*n
        matriz.append(linha)   
            
    Tmin = 0
    Tmax = 300
    T = 0
    k = 3
    Qtd_Damas = 0
    while(T>=Tmin and T < Tmax):
        qtd_atual = quantidadeDama(matriz)
        i = randrange(0,n)
        j = randrange(0,n)
        matriz[i][j] = 1

        #Verificando se infrige as restricoes
        if(not(verificaLinhasColunas(matriz) and VerificaDiagonais(matriz))):
            matriz[i][j] = 0
        qtd_vizinho = quantidadeDama(matriz)

        #Verificando se solucao melhorou se nao retorna para o anterior
        if(qtd_atual > qtd_vizinho):
            if(not(math.exp(T/k) >= uniform(0,1))): #tentando passar por maximos locais
                matriz[i][j] = 0
        
        T+=1
        #print(T)
        #print(matriz)
    
    Qtd_Damas = quantidadeDama(matriz)      
    print("Quantidade de damas: ",Qtd_Damas)
    

if __name__ == '__main__':
    main()
