#Nicolas Lamback de Paulo
letra = 'Z'
tentativa = 1
usuario = ''
print('===Jogo==da==Forca===')
print('Adivinhe a letra!')
while tentativa <= 5 and usuario != letra:
    usuario = str(input('Sua letra:')).upper()
    if usuario == letra:
        print('Meus parabéns você acertou!\n')
    elif usuario != letra and tentativa <= 4:
        print('Errou, tente novamente!\n')
    elif usuario != letra and tentativa == 5:
        print('Você perdeu :c Tente novamente mais tarde!')
    tentativa += 1
