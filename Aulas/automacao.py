import os

# Defina o número inicial e o número final desejado
inicio = 33
fim = 39  # Substitua pelo número final desejado

# Obtém o diretório atual (onde o script está sendo executado)
diretorio_atual = os.getcwd()

# Loop para criar os arquivos no diretório atual
for i in range(inicio, fim + 1):
    nome_arquivo = f'aula{i}.py'
    caminho_completo = os.path.join(diretorio_atual, nome_arquivo)  # Cria o caminho completo no diretório atual
    with open(caminho_completo, 'w') as arquivo:
        arquivo.write(f'# Arquivo {nome_arquivo}\n')  # Escreve um comentário no início do arquivo
    print(f'Arquivo {nome_arquivo} criado em {diretorio_atual}.')
