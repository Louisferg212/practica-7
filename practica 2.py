#modulo de lista bidimensional
import random as rd
matriz=[]

for x in range(5):
    l=[]
    for y in range(5):
        l.append(rd.randint(1,9))
    matriz.append(l)
print(matriz)
# subprogramas
#subpromrada de suma de cada una de las filas y el total de la matriz
def sumafilas():
    sumaFila0 = 0
    sumaFila1 = 0
    sumaFila2 = 0
    sumaFila3 = 0
    sumaFila4 = 0
    sumaColumna0=0
    sumaColumna1 = 0
    sumaColumna2 = 0
    sumaColumna3 = 0
    sumaColumna4 = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if (x == 0):
                sumaFila0 = sumaFila0 + matriz[x][y]
            elif (x == 1):
                sumaFila1 += matriz[x][y]
            elif (x == 2):
                sumaFila2 += matriz[x][y]
            elif (y == 0):
                sumaColumna0 += matriz[x][y]
            elif (y == 1):
                sumaColumna1 += matriz[x][y]
            elif (y == 2):
                sumaColumna2 += matriz[x][y]
    print("\nSuma de la primera fila:", sumaFila0)
    print("\nSuma de la segunda fila:", sumaFila1)
    print("\nSuma de la tercera fila:", sumaFila2)
    print("\nSuma de la cuarta fila:", sumaFila3)
    print("\nSuma de la quinta fila:", sumaFila4)

    #el total de la matriz
    totalMatriz=sumaFila0+sumaFila2+sumaFila3+sumaFila4+sumaColumna0+sumaColumna2+sumaColumna3+sumaColumna4
    print("La suma del total de la matriz",totalMatriz)

def promedio(p):
    p=totalMatriz/8
    return p
def matrizpares():
    for x in range(5):
        for y in range(5):
            if x % 2==0:
                print(x)

def filatres():
    sumaFila2 = 0
    elif (x == 2):
    multiplicacionFila2 = matriz[x][y]*2
    print("La modificacion de la matriz en la fila 3 multiplicando los numeros por 2 es",multiplicacionFila2)

def main():
    sumafilas()
    promedio()
    matrizpares()
    filatres()



main()

