#Nicolas Lamback de Paulo
contador = 0
numero = int(input('Digite um número: '))
maior = numero
while contador <= 1:
    numero = int(input('Digite um número: '))
    contador += 1
    if maior < numero:
        maior = numero
print(maior)
