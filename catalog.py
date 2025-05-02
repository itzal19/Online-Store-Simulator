from tabulate import tabulate
from typing import List, Dict
from config import WAREHOUSE

def show_catalog() -> None:
    print("\nProductos disponibles:\n")
    headers = ["Código", "Producto", "Precio"]
    data = [[product["code"], product["name"], f"S/ {product['price']:.2f}"] for product in WAREHOUSE]
    print(tabulate(data, headers=headers, tablefmt="github"))
    print("\n")