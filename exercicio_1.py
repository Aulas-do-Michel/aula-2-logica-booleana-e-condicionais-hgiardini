"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""
Numerodousuario=int(input("Digite um número:"))

if Numerodousuario % 2 == 0:
    print("Par")

if not Numerodousuario % 2 == 0:
    print("Ímpar")
