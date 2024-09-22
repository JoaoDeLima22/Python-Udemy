"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
n1=0
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'

while n1 < tamanho_nome:
    if nome[n1] == ' ':  # Verifica se o caractere é um espaço
        nova_string += ' '  # Adiciona o espaço sem asterisco
    else:
        nova_string += '*' + nome[n1]  # Adiciona '*' e a letra

    n1 += 1

nova_string += '*'  # Adiciona um asterisco no final

print(nova_string)
