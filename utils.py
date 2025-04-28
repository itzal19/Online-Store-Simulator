from tabulate import tabulate
from typing import List, Optional, Dict
from datetime import datetime

def print_shopping_cart_table(cart: List[Dict[str,str|int]]) -> int:
    total = 0
    headers = ["Código", "Producto", "Cantidad", "Precio", "Subtotal"]
    data = []
    for product in cart:
        subtotal = product["quantity"] * product["price"]
        product_in_cart = [product["code"], product["name"], product["quantity"], product["price"], subtotal]
        data.append(product_in_cart)
        total += subtotal    
    print("\n")
    print(tabulate(data, headers=headers, tablefmt="github"))
    print("\n")
    return total

def search_product(products: List[Dict[str,str|int]], code: str) -> Optional[int]:
    for index, product in enumerate(products):
        if product["code"] == code:
            return index
    return None

def add_order_to_file(cart: List[Dict[str,str|int]]) -> None:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = 0
    headers = ["Código", "Producto", "Cantidad", "Precio", "Subtotal"]
    data = []
    for product in cart:
        subtotal = product["quantity"] * product["price"]
        product_in_cart = [product["code"], product["name"], product["quantity"], product["price"], subtotal]
        data.append(product_in_cart)
        total += subtotal  
    tabla = tabulate(data, headers=headers, tablefmt="github")

    with open("order_summary.txt", 'w', encoding='utf-8') as file:
        file.write(f"Resumen de compra\nFecha y Hora: {date_time}\n\n")
        file.write(tabla)
        file.write(f"\n\nTotal a pagar: S/ {total:.2f}\n")