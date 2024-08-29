primeiro_Valor = input('Digite um valor: ')
segundo_Valor = input('Digite outro valor: ')

if primeiro_Valor > segundo_Valor:
    print('primeiro_Valor={} é maior que o segundo_Valor={}'.format(primeiro_Valor,segundo_Valor))
elif segundo_Valor > primeiro_Valor:
    print('segundo_Valor={} é maior que o primeiro_Valor={}'.format(segundo_Valor,primeiro_Valor))
else :
    print('os valores são iguais')