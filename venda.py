def validar_idade(idade):
  if idade < 18:
    print(f'\nDesculpe, você não tem a idade para prosseguir, {nome}.')
    return False
  else:
    print(f'\nVamos prosseguir, {nome}')
  return True

def escolher_carta():
  print('Escolha uma das opções abaixo (número): ')
  print('1 - Carro\n2 - Moto\n3 - Carro e moto')

  return int(input())

def calcular_preco(escolha):
  valor_carro = 1500.00
  valor_moto = 1000.00

  if escolha == 1:
    return valor_carro
  elif escolha == 2:
    return valor_moto
  else:
    return valor_carro + valor_moto

def desconto(valor):
  return valor-(valor * 0.10)

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))


if validar_idade(idade):
  escolha = escolher_carta()

  print('\nVou calcular o valor.')
  valor = calcular_preco(escolha)

  print('\n' +nome,'o valor total é de R$', valor)
  print('Mas eu vou verificar com meu gerente se posso dar um desconto...')
  valor = desconto(valor)

  print('\nCom desconto eu consigo fazer por R$ ', valor)
  print('Te interessa?\n1 - Sim\n2 - Não')
  interesse = int(input())

  if interesse == 1:
    print('\nPerfeito! Começaremos amanhã 👏🏻👏🏻')
  else:
    print('\nTudo bem 😕.\n Me avise se mudar de ideia 😉')
