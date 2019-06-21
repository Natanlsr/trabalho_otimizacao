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
   
    return diagonais
        
    
        
        
        
            
        
    

def main():
    n = int(input("Digite o tamando do n: "))
    matriz = [0] * n
    matriz = [matriz] * n
    linhas,colunas = pegaLinhasEColunas(matriz)
    print(linhas)
    #print(colunas)
    diagonais = pegaDiagonais(matriz)
    #print(diagonais)
    #montando variaveis
    di = []
    dicionario = {}
    for i in range(0,len(matriz),1):
        for j in range(0,len(matriz),1):
           di.append('M'+ str(i)+ '_' +str(j))
           dicionario['M'+ str(i)+ '_' +str(j)] = LpVariable('M'+ str(i)+ '_' +str(j),0,1,cat='Integer')
    #print(dicionario)

    #Criando o solver
    prob = LpProblem("Problema das Damas", LpMaximize)

    #Funcao objetivo
    soma= []
    for i in di:
        soma += dicionario[i]
    #print(soma)
    prob += soma


   #Restricoes

    #Para as linhas:
    
    for l in linhas:
        re_linhas = []
        for pos in range(0,len(l),1):
                re_linhas += dicionario[l[pos]]
        prob += re_linhas <= 1
   # print(re_linhas)
    #Para as colunas   
    
    for l in colunas:
        re_colunas = []
        for pos in range(0,len(l),1):
                re_colunas += dicionario[l[pos]]
        prob += re_colunas <= 1

    #print(diagonais)
    #Para as diagonais
    
    for l in diagonais:
        re_diagonais = []
        for pos in range(0,len(l),1):
                #print(dicionario[l[pos]])
                re_diagonais += dicionario[l[pos]]
        prob += re_diagonais <= 1
    

    print(prob)
    prob.solve()
    print("Status:", LpStatus[prob.status])
    total = 0
    for v in prob.variables():
        total +=  v.varValue
        print(v.name, "=", v.varValue)
    print("Total de Damas = ", total)
    

if __name__ == '__main__':
    main()
