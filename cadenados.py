def escribir_centrado(texto):
    anchura = 80  # anchura de la pantalla (89 - 9 para dejar margen)
    longitud = len(texto)
    espacios = " " * ((anchura - longitud) // 2)
    print(espacios + texto)
    print(espacios + "=" * longitud)

escribir_centrado("Hola Mundo")    