estoque = { "MONITOR": 10, "MOUSE": 4, "TECLADO": 6 }

historicoRetirada = []

while True:
    escolha = int(input("Sistema de Gestão de Almoxarifado e Sorteio \n1. Consultar Estoque, 2. Retirar Item, 3. Ver Histórico, 4. Sair e Sortear \nEscolha um numero... "))
    if escolha == 1:
        for chave, valor in estoque.items():
            print(f"{chave.upper()}: {valor}")
    elif escolha == 2:
        while True:
            nomeProduct = input("Digite o nome do Produto: ").upper()
            
            if nomeProduct not in estoque:
                print("Produto não encontrado\n")
                break
            
            valor = estoque[nomeProduct]
            
            quantProduct = int(input("Digite a quantidade que você deseja retirar: "))
            
            if quantProduct <= valor:
                calculo = valor - quantProduct
                print(f"Restará {calculo} unidades.")
                
                certeza = int(input("Tem certeza que deseja retirar? 1. Sim  2. não: "))
                
                if certeza == 1:
                    estoque[nomeProduct] = calculo
                    historicoRetirada.insert(0, nomeProduct)
                    print(f"O produto {nomeProduct} agora tem: {calculo}")
                    # print(historicoRetirada)
                    break
                else:
                    break
            
            else:
                print("Você não pode retirar mais do que possui no estoque\n")
                break
