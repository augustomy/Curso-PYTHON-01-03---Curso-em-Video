x = input('Digite uma frase: ')
aux = x.strip()
aux2 = aux.upper()
aux3 = aux2.count('A')
print('Quantidade de letras A na frase digitada: {}'.format(aux3))
aux4 = aux2.find('A')
print('Posição da primeira letra A: {}'.format(int(aux4+1)))
aux5 = aux2.rfind('A')
print('Posição da última letra A: {}'.format(int(aux5+1)))  
  