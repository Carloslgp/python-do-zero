# Exercício 3 — Saudação interativa
# Aula 01: print(), input() e variáveis
 
# A função input() pausa o programa e espera o usuário digitar algo.
# O texto entre parênteses é a pergunta exibida na tela.
# O que o usuário digitar é guardado na variável nome_usuario como string.
nome_usuario = input("Digite seu nome: ")
 
# Usamos f-string para montar a mensagem final com o nome digitado.
print(f"Seja bem-vindo(a), {nome_usuario}!")