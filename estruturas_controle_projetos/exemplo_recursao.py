def imprimir(max, current):
    # condição de parada
    if current < max:
        print(current)
        imprimir(max, current + 1)


imprimir(100, 1)
