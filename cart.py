from typing import List, Dict
from utils import search_product, print_shopping_cart_table, add_order_to_file

SHOPPING_CART = [

]

def add_product_to_shopping_cart(warehouse: List[Dict[str,str|int]]) -> None:
    try:
        product_code = input("\n💬 Ingrese código de producto: ").strip().upper()
        quantity = input("💬 Cantidad: ").strip()

        if not quantity.isdigit():
            raise ValueError("La cantidad debe ser un número entero positivo.")

        product_found_index = search_product(warehouse, product_code)
        if product_found_index is not None:
            already_added_index = search_product(SHOPING_CART, product_code)
            if already_added_index is None:
                product_found = warehouse[product_found_index]
                product_to_add = {"code": product_found["code"], "name": product_found["name"], "quantity": int(quantity), "price": product_found["price"]}
                SHOPING_CART.append(product_to_add)
                print(f"\n✅ El producto {product_found['code']} - {product_found['name']} ({quantity} uds.) fue agregado al carrito\n")
            else:
                print(
                """El producto ya se encuentra en el carrito de compras. ¿Deseas actualizar la cantidad?\n
                1. Sí, actualizar carrito ⚠️\n
                2. No, cancelar ❌
                """)
                choice = input("> ")
                if choice == "1":
                    SHOPING_CART[already_added_index]["quantity"] = int(quantity)
                    print("\n✔ Carrito actualizado correctamente.\n")
                elif choice == "2":
                    print("\n❌ Operación cancelada. El carrito no fue modificado.\n")
                else:
                    print("\n⚠️  Opción no válida. El carrito no fue modificado.\n")
        else:
            print("\n❌ Error: Producto no encontrado.\n")
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")

def remove_product_from_shopping_cart() -> None:
    if SHOPING_CART:
        print_shopping_cart_table(SHOPING_CART)
        product_to_delete = input("💬 Ingrese código de producto a eliminar del carrito: ").strip().upper()
        product_found_index = search_product(SHOPING_CART, product_to_delete)
        if product_found_index is not None:
            product_found = SHOPING_CART[product_found_index]
            del SHOPING_CART[product_found_index]
            print(f"\n✅ El producto {product_found['code']} - {product_found['name']} fue retirado del carrito\n")
        else:
            print("\n❌ Error: El producto no se encuentra en el carrito de compras.\n")

def clear_shopping_cart():
    pass

def show_shopping_cart():
    pass

def checkout_shopping_cart():
    pass

