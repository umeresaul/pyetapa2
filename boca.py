import tkinter as tk

def crear_ventana():
    # Crear la ventana principal
    ventana = tk.Tk() 
    ventana.title("ejemplo")

    # Configurar el tamaño de la ventana
    ventana.geometry("800x600")

    # Crear un canvas para dibujar la franja amarilla
    canvas = tk.Canvas(ventana, width=800, height=600)
    canvas.pack()

    # Dibujar la franja amarilla
    canvas.create_rectangle(100, 250, 700, 350, fill="yellow")

    # Crear un texto dentro de la franja amarilla
    texto = canvas.create_text(400, 300, text="leonel kpo", font=("Arial", 48), fill="blue")

    # Subrayar el texto
    canvas.create_line(400-100, 320, 400+100, 320, fill="black")

    # Cambiar el color de fondo de la ventana a azul
    ventana.configure(background="blue")

    # Iniciar el bucle principal de la ventana
    ventana.mainloop()

# Preguntar al usuario que ingrese "leonel"
nombre = input("Ingrese 'leonel': ")

if nombre == "leonel":
    crear_ventana()
else:
    print("Nombre incorrecto")