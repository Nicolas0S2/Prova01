#Nicolas Lamback de Paulo
idade = int(input('Digite sua idade: '))
tempoServ = int(input('Digite seu tempo de serviço: '))
if idade >= 65:
    print('Já pode se aposentar!')
elif tempoServ >= 30:
    print('Já pode se aposentar!')
elif idade >= 60 and tempoServ >= 25:
    print('Já pode se aposentar!')
else:
    print('Ainda não pode se aposentar!')
