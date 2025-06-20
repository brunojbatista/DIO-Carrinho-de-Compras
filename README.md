# 🛒 Sistema de Carrinho de Compras em Python

Este projeto implementa um sistema simples de carrinho de compras em Python. O sistema permite adicionar produtos com nome e preço, e exibe uma lista formatada dos itens com o valor total da compra.

---

## 📌 Descrição

O usuário informa quantos produtos deseja adicionar. Para cada produto, fornece o nome e o valor. O sistema, então, exibe a lista de itens com os respectivos preços e calcula o total geral da compra.

---

## ✅ Funcionalidades

- Adição de produtos ao carrinho.
- Armazenamento de nome e preço com precisão decimal.
- Exibição de todos os produtos no carrinho.
- Cálculo automático do total da compra com arredondamento adequado.

---

## ▶️ Como Usar

1. Salve o código em um arquivo, por exemplo, `carrinho.py`.
2. Execute no terminal:

   ```bash
   python carrinho.py
   ```

3. Insira a quantidade de produtos e, em seguida, os dados de cada um:

```
Entrada:
2
Pão 3.50
Leite 4.00

Saída:
Pão: R$3.50
Leite: R$4.00
Total: R$7.50
```

---

## 💡 Exemplos

### Entrada:

```
3
Maçã 2.00
Pera 3.50
Biscoito 5.50
```

### Saída:

```
Maçã: R$2.00
Pera: R$3.50
Biscoito: R$5.50
Total: R$11.00
```

---

## ⚠️ Possíveis Erros

| Situação | Comportamento ou Erro |
|----------|------------------------|
| Valor digitado não numérico | `decimal.InvalidOperation` ou `ValueError` |
| Dados incompletos (sem preço) | IndexError ou erro de conversão |
| Espaço extra entre nome e valor | Aceito, desde que o valor esteja separado no final |
| Produtos com nomes compostos | **Não suportado** no formato atual, apenas uma palavra |

> 💡 **Dica:** Use nomes simples (sem espaços) para produtos. Exemplo: `Sorvete 10.00`, e não `Sorvete de Chocolate 10.00`.

---

## 📦 Estrutura das Classes

### `Product`

- Armazena nome e preço do produto.
- Usa `Decimal` para precisão em valores monetários.
- Exibe o produto formatado: `Nome: R$preço`.

### `ShoppingCart`

- Armazena produtos adicionados.
- Calcula e imprime o total da compra.

---

## ✏️ Melhorias Sugeridas

- Suporte a nomes de produto com múltiplas palavras.
- Validação de entrada para evitar erros.
- Interface gráfica ou web.
- Persistência dos dados em arquivo ou banco de dados.

---

## 📄 Licença

Este projeto é livre para uso educacional e pode ser adaptado para outros fins.