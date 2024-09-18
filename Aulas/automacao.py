import os

# Definir o número inicial e o número final desejado
inicio = 22
fim = 31 # Substitua pelo número final desejado

# Loop para criar os arquivos
for i in range(inicio, fim +1):
    nome_arquivo = f'aula{i:03}.py' # O {03} mantém os números com 3 dígitos (ex: aula021.py)
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f'# Arquivo {nome_arquivo}\n')
    print(f'Arquivo {nome_arquivo} criado.')