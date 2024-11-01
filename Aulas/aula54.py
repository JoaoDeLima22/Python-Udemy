"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
# Inicializando a lista de compras
compras = []
while True:
    print("Selecione uma opção")
    opcao= input("[i]nserir   [a]pagar   [l]istar:")
    
    if opcao in ["i","a","l"]:
        if opcao =="l":
            if compras !=[]:
                for item in enumerate(compras):
                    indice, produto = item
                    print(f"{indice} - {produto}")
            else:
                print("Lista de compras vazia")
        elif opcao == "i":
            produto = input("Digite o produto que deseja adicionar:")
            compras.append(produto)
        elif opcao == "a":
            if compras !=[]:             
                try:
                    indice = int(input("Digite o índice do produto que deseja apagar:"))
                    del compras[indice]
                except IndexError:
                    print("Índice inexistente")
            else:
                print("Lista de compras vazia")
    