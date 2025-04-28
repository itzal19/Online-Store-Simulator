from catalog import show_catalog
from menu import show_menu
from cart import show_shopping_cart,add_product_to_shopping_cart, remove_product_from_shopping_cart, clear_shopping_cart, checkout_shopping_cart

WAREHOUSE = [
    {"code": "E001", "name": "Licuadora", "price": 340},
    {"code": "E002", "name": "Hervidor", "price": 320},
    {"code": "E003", "name": "Plancha", "price": 330},
    {"code": "E004", "name": "Freidora", "price": 500},
    {"code": "E005", "name": "Microondas", "price": 450},
    {"code": "E006", "name": "Cafetera", "price": 360},
    {"code": "E007", "name": "Refrigerador", "price": 820},
    {"code": "E008", "name": "Ventilador", "price": 310},
    {"code": "E009", "name": "Aspiradora", "price": 590},
    {"code": "E010", "name": "Televisor", "price": 780}
]

#SHOPING_CART = []

print("\nBienvenido a la tienda virtual 🛍️\n")
while True:
    show_menu()
    opcion = input("\n> ")
    try:
        if not opcion.isdigit() or not (1 <= int(opcion) <= 7):
            raise ValueError("Se debe ingresar un número del 1 al 7.")
        match opcion:
            case "1":
                show_catalog(WAREHOUSE)
            case "2":
                add_product_to_shopping_cart(WAREHOUSE)
            case "3":
                remove_product_from_shopping_cart()
            case "4":
                clear_shopping_cart()
            case "5":
                show_shopping_cart()    
            case "6":
                checkout_shopping_cart()
            case "7":
                print("\nGracias por visitar la tienda virtual. ¡Hasta pronto! 👋\n")
                break
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")