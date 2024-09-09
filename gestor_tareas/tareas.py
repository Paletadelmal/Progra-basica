from gestor import AgreTar, ElimTar, ModTar, MostTar

def main():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Modificar Tarea")
        print("4. Mostrar Tareas")
        print("5. Salir")
        opcion = input("Ingresa la opción: ")

        if opcion == '1':
            AgreTar()
        elif opcion == '2':
            ElimTar()
        elif opcion == '3':
            ModTar()
        elif opcion == '4':
            MostTar()
        elif opcion == '5':
            break
        else:
            print("la opcion no esta en el menu. Por favor, vuelva a intentar.")

if __name__ == "__main__":
    main()