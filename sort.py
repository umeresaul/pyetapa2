lista_numeros= []

while True:
    numero = input("ingrese un número o 'fin' para terminar: ")
    if numero == 'fin' :
        break
    lista_numeros.append(int(numero))

    lista_ordenada=sorted(lista_numeros)
    print(lista_ordenada)