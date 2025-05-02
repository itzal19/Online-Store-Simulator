from catalog import show_catalog
from cart import show_shopping_cart,add_product_to_shopping_cart, remove_product_from_shopping_cart, clear_shopping_cart, checkout_shopping_cart
import os

def add_options():
    print("¿Qué deseas hacer ahora?\n") 
    print("1. Salir de la tienda 👋    2. Ir al menú 🏠\n")
    opcion = input("> ")
    if opcion == "1":
        print("\nGracias por visitar la tienda virtual. ¡Hasta pronto! 👋\n")
    elif opcion == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
    else:
        print("\n⚠️  Opción no válida. Vuelve a intentarlo.\n")
        add_options()


def show_menu() -> None:
    print(
    """¿Qué deseas hacer?

    1. Ver catálogo
    2. Agregar producto al carrito
    3. Eliminar producto del carrito
    4. Vaciar carrito
    5. Mostrar carrito
    6. Finalizar compra
    7. Salir"""
    )

    opcion = input("\n> ")
    try:
        if not opcion.isdigit() or not (1 <= int(opcion) <= 7):
            raise ValueError("Se debe ingresar un número del 1 al 7.")
        match opcion:
            case "1":
                show_catalog()
                add_options()
            case "2":
                add_product_to_shopping_cart()
                add_options()
            case "3":
                remove_product_from_shopping_cart()
                add_options()
            case "4":
                clear_shopping_cart()
                add_options()
            case "5":
                show_shopping_cart()
                add_options()    
            case "6":
                checkout_shopping_cart()
                add_options()
            case "7":
                print("\nGracias por visitar la tienda virtual. ¡Hasta pronto! 👋\n")
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")