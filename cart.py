from utils import search_product, print_shopping_cart_table, add_order_to_file
from typing import List, Dict
from config import WAREHOUSE

SHOPPING_CART = [

]

def add_product_to_shopping_cart() -> None:
    try:
        product_code = input("\n💬 Ingrese código de producto: ").strip().upper()
        product_found_index = search_product(WAREHOUSE, product_code)
        if product_found_index is None:
            raise ValueError("Producto no encontrado en catálogo.")

        quantity = input("💬 Cantidad: ").strip()
        if not quantity.isdigit():
            raise ValueError("La cantidad debe ser un número entero positivo.")

        already_added_index = search_product(SHOPPING_CART, product_code)
        if already_added_index is None:
            product_found = WAREHOUSE[product_found_index]
            product_to_add = {"code": product_found["code"], "name": product_found["name"], "quantity": int(quantity), "price": product_found["price"]}
            SHOPPING_CART.append(product_to_add)
            print(f"\n✅ El producto {product_found['code']} - {product_found['name']} ({quantity} uds.) fue agregado al carrito\n")
        else:
            print(
            """El producto ya se encuentra en el carrito de compras. ¿Deseas actualizar la cantidad?\n
            1. Sí, actualizar carrito ⚠️\n
            2. No, cancelar ❌
            """)
            choice = input("> ")
            if choice == "1":
                SHOPPING_CART[already_added_index]["quantity"] = int(quantity)
                print("\n✔ Carrito actualizado correctamente.\n")
            elif choice == "2":
                print("\n❌ Operación cancelada. El carrito no fue modificado.\n")
            else:
                print("\n⚠️  Opción no válida. El carrito no fue modificado.\n")
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")

def remove_product_from_shopping_cart() -> None:
    if SHOPPING_CART:
        print_shopping_cart_table(SHOPPING_CART)
        product_to_delete = input("💬 Ingrese código de producto a eliminar del carrito: ").strip().upper()
        product_found_index = search_product(SHOPPING_CART, product_to_delete)
        if product_found_index is not None:
            product_found = SHOPPING_CART[product_found_index]
            del SHOPPING_CART[product_found_index]
            print(f"\n✅ El producto {product_found['code']} - {product_found['name']} fue retirado del carrito\n")
        else:
            print("\n❌ Error: El producto no se encuentra en el carrito de compras.\n")
    else:
        print("\n⚠️  Aún no has agregado productos al carrito.\n")

def clear_shopping_cart() -> None:
    if SHOPPING_CART:
        print(
        """¿Estás seguro de que deseas vaciar el carrito de compras?\n
        1. Sí, vaciar carrito ⚠️
        2. No, cancelar ❌
        """)
        choice = input("> ")
        if choice == "1":
            SHOPPING_CART.clear()
            print("\n✅ Carrito vaciado correctamente.\n")
        elif choice == "2":
            print("\n⚠️  Operación cancelada. El carrito no fue modificado.\n")
        else:
            print("\n⚠️  Opción no válida. El carrito no fue modificado.\n")
    else:
        print("\n⚠️  Aún no has agregado productos al carrito.\n")

def show_shopping_cart() -> None:
    if SHOPPING_CART:
        print("\nTu carrito de compra:")
        total = print_shopping_cart_table(SHOPPING_CART)
        print(f"Total a pagar: S/ {total:.2f}\n")
    else:
        print("\n⚠️  Aún no has agregado productos al carrito.\n")

def checkout_shopping_cart() -> None:
    if SHOPPING_CART:
        print("\nTus productos:")
        total = print_shopping_cart_table(SHOPPING_CART)
        print(f"Cuenta total: S/ {total:.2f}")
        print("\nGracias por tu compra 😊\n")
        add_order_to_file(SHOPPING_CART)
        SHOPPING_CART.clear()
    else:
        print("\n⚠️  Aún no has agregado productos al carrito.\n")
