diccionario = {}
texto = input("ingresar testo: ")
for i in texto:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1

print(diccionario)