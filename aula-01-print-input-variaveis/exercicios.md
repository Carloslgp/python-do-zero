# Aula 01 — print(), input() e variáveis

Nesta primeira aula, vamos praticar a base de qualquer programa. Você vai aprender a mostrar mensagens na tela, pedir informações para o usuário e guardar esses dados na memória do computador usando variáveis. 

Para resolver estes exercícios, lembre-se de que o `input()` sempre lê textos. Quando precisar fazer contas, você deve converter a entrada usando `int()` para números inteiros ou `float()` para números com vírgula.

Os exercícios estão em ordem crescente de dificuldade. Tente resolver antes de olhar a resposta.

Bons estudos...

---

## O que você vai praticar
 
- Mostrar texto e valores com `print()`
- Ler dados do teclado com `input()`
- Criar variáveis e usar os tipos `str`, `int` e `float`
- Converter texto em número com `int()` e `float()`
---
 
## Exercício 1 — Sua primeira mensagem
 
**Dificuldade:** Fácil
 
**Enunciado:** Escreva um programa que mostre na tela a frase "Olá, mundo! Estou aprendendo Python." em uma única linha.
 
**Exemplo de execução:**
 
```
Olá, mundo! Estou aprendendo Python.
```
 
### Resolução
 
```python
print("Olá, mundo! Estou aprendendo Python.")
```
 
### Explicação
 
A função `print()` serve para mostrar algo na tela. Tudo que vai entre parênteses é exibido para o usuário.
 
O texto fica entre aspas porque é uma **string** (str), que é o tipo usado para representar palavras e frases em Python. Você pode usar aspas duplas ou simples, desde que abra e feche com o mesmo tipo.
 
### Arquivo: [`solucoes/exercicio_01.py`](exercicio_01.py)
 
---
 
## Exercício 2 — Guardando seu nome
 
**Dificuldade:** Fácil
 
**Enunciado:** Crie uma variável chamada `nome` com o seu nome dentro. Em seguida, mostre na tela uma saudação personalizada usando essa variável.
 
**Exemplo de execução:**
 
```
Olá, Carlos! Bons estudos.
```
 
### Resolução
 
```python
nome = "Carlos"
print(f"Olá, {nome}! Bons estudos.")
```
 
### Explicação
 
A linha `nome = "Carlos"` cria uma variável. Pense em variável como uma caixinha com um nome (`nome`) que guarda um valor dentro (`"Carlos"`). O sinal de igual `=` faz essa atribuição.
 
Depois usamos uma **f-string** (texto que começa com `f` antes das aspas). Dentro dela, o que está entre chaves `{}` é substituído pelo valor da variável. Assim, `{nome}` vira `Carlos` quando o programa roda.
 
### Arquivo: [`solucoes/exercicio_02.py`](exercicio_02.py)
 
---
 
## Exercício 3 — Saudação interativa
 
**Dificuldade:** Fácil
 
**Enunciado:** Peça ao usuário que digite o nome dele. Depois, mostre uma mensagem de boas-vindas usando o nome informado.
 
**Exemplo de execução:**
 
```
Digite seu nome: Ana
Seja bem-vinda, Ana!
```
 
### Resolução
 
```python
nome_usuario = input("Digite seu nome: ")
print(f"Seja bem-vindo(a), {nome_usuario}!")
```
 
### Explicação
 
A função `input()` pausa o programa e espera o usuário digitar algo. O texto que vai entre os parênteses é a pergunta que aparece na tela. Quando o usuário aperta Enter, o que foi digitado vira o valor da variável `nome_usuario`.
 
Tudo que `input()` devolve é uma **string**, mesmo que o usuário digite um número. Aqui isso não é um problema porque queremos um nome mesmo.
 
### Arquivo: [`solucoes/exercicio_03.py`](exercicio_03.py)
 
---
 
## Exercício 4 — Calculadora de idade
 
**Dificuldade:** Médio
 
**Enunciado:** Peça ao usuário o ano em que ele nasceu e o ano atual. Calcule e mostre a idade aproximada dele.
 
**Exemplo de execução:**
 
```
Digite o ano em que você nasceu: 2003
Digite o ano atual: 2026
Você tem aproximadamente 23 anos.
```
 
### Resolução
 
```python
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))
 
idade = ano_atual - ano_nascimento
 
print(f"Você tem aproximadamente {idade} anos.")
```
 
### Explicação
 
Como `input()` sempre devolve uma string, não dá para fazer contas direto com o resultado. Por isso envolvemos a chamada com `int()`, que converte o texto em **número inteiro**. Sem essa conversão, Python tentaria "subtrair textos" e daria erro.
 
Depois guardamos o resultado da subtração em uma nova variável `idade` e mostramos com `print()`. Note como uma variável pode receber o valor de uma conta entre outras variáveis.
 
### Arquivo: [`solucoes/exercicio_04.py`](exercicio_04.py)
 
---
 
## Exercício 5 — Conversor de reais para dólares
 
**Dificuldade:** Médio
 
**Enunciado:** Peça ao usuário um valor em reais e a cotação atual do dólar. Mostre quantos dólares ele consegue comprar com aquele valor, com duas casas decimais.
 
**Exemplo de execução:**
 
```
Valor em reais: 500
Cotação do dólar: 5.20
Você consegue comprar US$ 96.15
```
 
### Resolução
 
```python
valor_reais = float(input("Valor em reais: "))
cotacao_dolar = float(input("Cotação do dólar: "))
 
valor_dolares = valor_reais / cotacao_dolar
 
print(f"Você consegue comprar US$ {valor_dolares:.2f}")
```
 
### Explicação
 
Aqui usamos `float()` em vez de `int()` porque queremos aceitar números com casas decimais, como `5.20`. O tipo `float` representa números reais (com vírgula).
 
A divisão `valor_reais / cotacao_dolar` produz o resultado em dólares. Dentro da f-string, o trecho `:.2f` é uma formatação especial que arredonda o número para **duas casas decimais**, deixando o resultado mais limpo para mostrar dinheiro.
 
### Arquivo: [`solucoes/exercicio_05.py`](exercicio_05.py)
 
---
 
## Próximos passos
 
Na próxima aula vamos aprender a tomar decisões no código com `if`, `elif` e `else`. Assim seus programas poderão reagir de formas diferentes dependendo do que o usuário digitar.
 
Bons estudos...