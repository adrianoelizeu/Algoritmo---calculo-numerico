""" sistema 
 |-3x  + 2x - 3x = b 
 |a21x + 3x - x  = 4
 |-x   + 5x - a33x = 2
 
 algoritmo que receba os valores b, a21, a33 que resolva o sistema e diga se é possivel o criterio da matiz dioagonamente dominante"""

def verifica_diagonal(A):
    n=len(A)
    for i in range(n):
        if A[i][i]==0:
            return False
    return True   

#Metado de Gauss - Seidel
def gauss_jacobi(A,b):
    n = len(A)
    aproximacao=[0 for i in range(n)]
    erro = 0.00000000001
    iteracoes = 10000
    teste = [0 for i in range(n)]
    if verifica_diagonal(A):
        for k in range(iteracoes):
            for i in range(n):
                soma=0
                for j in range(n):
                    if i==j:
                        continue
                    else:
                        soma = soma+A[i][j]*aproximacao[j]
                teste[i]=(b[i]-soma)/A[i][i]
            erros=[0 for i in range(n)]
            for i in range(n):
                erros[i]= abs(teste[i]-aproximacao[i])
            if(max(erros)/max(teste)<erro):
                return aproximacao
            for i in range(n):
                aproximacao[i] = teste[i]
    else:
        print("Pela definição do algoritmo ele exige que só se tenha elementos não nulos na diagonal principal portanto esse sistema não pode ser resolvido")

b1=3
a21=2
a33=12

A=[[-3,2,-3],[a21,3,-1],[-1,5,-a33]]
b=[b1,4,2]

#GAUSS SEIDEL
print("METADO DE GAUSS-SEIDEL")
print(gauss_jacobi(A,b))

def gauss_seidel(A,b):
    n = len(A)
    aproximacao=[0 for i in range(n)]
    erro = 0.00000000001
    iteracoes = 10000