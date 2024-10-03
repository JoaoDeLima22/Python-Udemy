while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-*/): ')
    
    numeros_validos = None
    
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) >1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta.')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)        
    elif operador =='*':
        print(num1_float * num2_float)
    elif operador =='/':
        print(num1_float / num2_float)
    else:    
        print('Não deveria ter mostrado isso')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    