def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir por cero"

def main():
    while True:
        print("\nCalculadora Básica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "5":
            print("Adiós!")
            break

        elif opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                print(f"El resultado de la suma es: {suma(num1, num2)}")
            elif opcion == "2":
                print(f"El resultado de la resta es: {resta(num1, num2)}")
            elif opcion == "3":
                print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
            elif opcion == "4":
                print(f"El resultado de la división es: {dividir(num1, num2)}")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
    
