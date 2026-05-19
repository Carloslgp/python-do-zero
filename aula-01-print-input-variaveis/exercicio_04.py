# Exercício 4 — Calculadora de idade
# Aula 01: print(), input() e variáveis
 
# input() sempre retorna uma string. Como queremos fazer contas, precisamos
# converter o texto digitado em número inteiro usando int().
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))
 
# Guardamos o resultado da subtração em uma nova variável chamada idade.
# Variáveis podem receber tanto valores fixos quanto resultados de operações.
idade = ano_atual - ano_nascimento
 
# Mostramos a idade calculada usando f-string para misturar texto e número.
print(f"Você tem aproximadamente {idade} anos.")
 