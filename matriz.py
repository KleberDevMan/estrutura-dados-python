a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

b = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 15]]

# vai guardar o resultado
matriz_resultado = []

# Supondo que as duas matrizes possuem o mesmo tamanho
quant_linhas = len(a)  # Conta quantas linhas existem
quant_colunas = len(b[0])  # Conta quantos elementos têm em uma linha

for i in range(quant_linhas):

        # Cria uma nova linha na matriz_resultado
        matriz_resultado.append([])

        for j in range(quant_colunas):

                # Compara os elementos que possuem o mesmo índice
                ganhador = a[i][j] if (a[i][j] > b[i][j]) else b[i][j]

                matriz_resultado[i].append(ganhador)

print('Matriz resultado: ', matriz_resultado)

