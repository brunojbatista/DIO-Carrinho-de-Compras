"""
    Descrição
    Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

    Entrada
        Lista de produtos adicionados ao carrinho (cada um com nome e preço).
    Saída
        Lista dos produtos adicionados e o total da compra.

    Exemplos
        A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

    Entrada	        Saída
    2               Pão: R$3.50
    Pão 3.50        Leite: R$4.00
    Leite 4.00      Total: R$7.50

    3               Arroz: R$2.50
    Arroz 2.50      Brigadeiro: R$3.00
    Brigadeiro 3.00 Sorvete: R$14.50
    Sorvete 14.50	Total: R$20.00

    3               Maçã: R$2.00
    Maçã 2.00       Pera: R$3.50
    Pera 3.50       Biscoito: R$5.50
    Biscoito 5.50	Total: R$11.00
"""

import re
from typing import List
from decimal import ROUND_HALF_UP, Decimal

DEFAULT_DECIMAL_PLACES = 2

def round_decimal(value: Decimal, decimal_places: int) -> Decimal:
    fator = Decimal('1.' + ('0' * decimal_places))
    return value.quantize(fator, rounding=ROUND_HALF_UP)

class Product():
    def __init__(self, name: str, price: Decimal):
        self.name: str = name
        self.price: Decimal = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def get_name(self, ) -> str:
        """
            Pega o nome do produto

        Returns:
            str: O nome do produto
        """ 
        return self.name
    
    def get_price(self, ) -> Decimal:
        """
            Pega o valor do produto

        Returns:
            Decimal: Retornar o decimal que representa o valor
        """
        return self.price
    
    def __str__(self):
        """
            Printa o objeto de produto
        """
        return f"{self.name}: R${round_decimal(self.price, DEFAULT_DECIMAL_PLACES)}"

class ShoppingCart():
    def __init__(self):
        self.cart: List[Product] = []

    def add_product(self, product: Product):
        """
            Adicionar um produco

        Args:
            product (Product): Produto a ser inserido
        """
        self.cart.append(product)

    def __str__(self):
        """
            Printa o objeto de carrinho de compras
        """
        text: str = ""
        total: Decimal = Decimal('0')
        for product in self.cart:
            total += product.get_price()
            text += str(product) + "\n"
        text += f"Total: R${round_decimal(total, DEFAULT_DECIMAL_PLACES)}"
        return text


# Entrada do número de itens
n = int(input().strip())

cart: ShoppingCart = ShoppingCart()
for i in range(n):
    row = input().strip()
    # Encontra a última ocorrência de espaço para separar nome e preço
    input_strings = re.split(r"\s+", row)

    product_name: str = input_strings[0]
    product_value: Decimal = Decimal(input_strings[1])
    product: Product = Product(product_name, product_value)

    cart.add_product(product)

print(cart)

