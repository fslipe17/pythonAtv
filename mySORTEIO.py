estoque = { "MONITOR": 10, "MOUSE": 4, "TECLADO": 6 }

historicoRetirada = []

while True:
    escolha = int(input("Sistema de Gestão de Almoxarifado e Sorteio \n1. Consultar Estoque, 2. Retirar Item, 3. Ver Histórico, 4. Sair e Sortear \nEscolha um numero... "))
    if escolha == 1:
        for chave, valor in estoque.items():
            print(f"{chave.upper()}: {valor}")
    elif escolha == 2:
        while True:
            for chave, valor in estoque.items():
                
                nomeProduct = input("Digite o nome do Produto: ").upper()
            
                quantProduct = int(input("Digite a quantidade que você deseja retirar: "))
                
                if nomeProduct != estoque[chave]:
                    print(f"O produto {nomeProduct} tem: {valor}")
                    
                else:
                    print(estoque.get("RA", "Produto não encontrado\n"))
            
            
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
