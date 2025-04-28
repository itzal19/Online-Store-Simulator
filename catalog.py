from tabulate import tabulate
from typing import List, Dict

def show_catalog(products: List[Dict[str,str|int]] ) -> None:
    headers = ["Código", "Producto", "Precio"]
    data = [[product["code"], product["name"], f"S/ {product['price']:.2f}"] for product in products]
    print("\n")
    print(tabulate(data, headers=headers, tablefmt="github"))
    print("\n")