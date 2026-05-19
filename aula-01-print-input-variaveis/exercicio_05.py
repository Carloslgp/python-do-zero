# Exercício 5 — Conversor de reais para dólares
# Aula 01: print(), input() e variáveis
 
# Usamos float() em vez de int() porque queremos aceitar números com casas
# decimais (a cotação do dólar quase sempre tem vírgula, como 5.20).
valor_reais = float(input("Valor em reais: "))
cotacao_dolar = float(input("Cotação do dólar: "))
 
# Dividimos o valor em reais pela cotação para descobrir quantos dólares dá.
valor_dolares = valor_reais / cotacao_dolar
 
# O trecho :.2f dentro da f-string formata o número com 2 casas decimais,
# que é o padrão usado para mostrar valores em dinheiro.
print(f"Você consegue comprar US$ {valor_dolares:.2f}")
 