from PetManager import PetManager

def show_credits():
    print("Curso:  LENGUAJES FORMALES Y DE PROGRAMACION")
    print("Sección: B-")
    print("Carnet: 202200387")
    input("Presiona Enter para continuar...")

def main():
    while True:
        show_credits()
        pet_manager = PetManager()
        pet_manager_menu(pet_manager)
        
        choice = input("¿Quieres regresar al Menú Principal? (Sí/No): ").lower()
        if choice != 'si':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

def pet_manager_menu(pet_manager):
    while True:
        print("\nMenú PetManager:")
        print("1. Crear Gato")
        print("2. Dar de Comer")
        print("3. Jugar")
        print("4. Resumen de Mascota")
        print("5. Resumen Global")
        print("6. Cargar Archivo")
        print("7. Salir")

        choice = input("Ingrese el número de la opción deseada: ")

        if choice == "1":
            pet_name = input("Ingrese el nombre del gato: ")
            pet_manager.create_pet(pet_name)
        elif choice == "2":
            pet_name = input("Ingrese el nombre del gato: ")
            mouse_weight = input("Ingrese el peso del ratón: ")
            pet_manager.eat(pet_name, int(mouse_weight))
        elif choice == "3":
            pet_name = input("Ingrese el nombre del gato: ")
            minutes = input("Ingrese la duración del juego en minutos: ")
            pet_manager.play(pet_name, int(minutes))
        elif choice == "4":
            pet_name = input("Ingrese el nombre del gato: ")
            pet_manager.print_summary(pet_name)
        elif choice == "5":
            pet_manager.print_global_summary()
        elif choice == "6":
            filename = input("Ingrese el nombre del archivo a cargar: ")
            pet_manager.load_from_file(filename)
        elif choice == "7":
            print("Saliendo del Menú PetManager")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()