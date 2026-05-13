# SISTEMA DE GESTÃO DE ALMOXARIFADO E SORTEIO

import random

estoque = {"monitor": 10, "mouse": 30, "teclado": 25}
historicoRetirada = []
print("Seja bem-vindo(a) a loja!\n")
while True:
    print("\nEscolha uma das opções:\n1. Consultar estoque\n2. Retirar item\n3. Ver histórico\n4. Sair e sortear\n")
    menu = int(input("Selecione uma das opções: "))
    if menu == 1:
        while True:
            print("\nProdutos disponíveis: Mouse, Monitor, Teclado, Processador.")
            print("\nQual produto você gostaria de ver no estoque? Digite o nome do produto, todos ou 'Sair' se caso queira voltar para as opções inicias.\n")
            produto = input("Selecione uma das opões: ").lower()
            if produto.lower() == "sair":
                break
            elif produto == "todos":
                print(estoque)
                break
            else:
                print(f"\nAs quantidades disponíveis de {produto} no estoque é: {estoque[produto]}")
    elif menu == 2:
        while True:
            chave = []
            valor = []

            for chave1, valor1 in estoque.items():
                chave = chave1
                valor = valor1
        
            nomeProduct = input("Digite o nome do Produto: ").lower()
        
            quantProduct = int(input("Digite a quantidade que você deseja retirar: "))
                
            if nomeProduct != estoque[chave]:
                print(f"O produto {nomeProduct} tem: {valor}")
            else:
                print(estoque.get("RA", "Produto não encontrado\n"))
                break
        
            if quantProduct <= valor:
                calculo = valor - quantProduct
                # estoque[chave]
                print(f"Restará {calculo} unidades.")
                
                certeza = int(input("Tem certeza que deseja retirar? 1. Sim  2. não: "))
                
                if certeza == 1:
                    estoque[chave] = calculo
                    historicoRetirada.insert(1, nomeProduct)
                    print(f"O produto {nomeProduct} tem: {calculo}")
                    print(historicoRetirada)
                    break
                elif certeza == 2:
                    break
                else:
                    print("Refaça e digite um valor valido!!")
                    break
                
            elif quantProduct > valor:
                print("Você não pode retirar mais do que possui no estoque\n")
                break
            elif nomeProduct.lower() == "sair":
                break
    elif menu == 3:
        print({historico})
    elif menu == 4:
        print({ganhador})
    else:
        print(f"erro no programa")
