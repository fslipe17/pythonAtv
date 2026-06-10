# import random

# def benvindo():
#     print("==== Bem-Vindo ao Chamados de TI ====\n")
    
# def menu():
#     print("Digite o numero relacionado ao seu caso..")
#     print("\n1. Criar Chamado")
#     print("2. Listar Ordem de Chamado")
#     print("3. Atualizar Status")
#     print("4. Tecnico de TI")
#     print("5. Sair")
    
# def escolher_id(banco):
#     while True:
#         num_id = random.randint(100, 999)

#         existe = False
#         for chamado in banco:
#             if chamado["id"] == num_id:
#                 existe = True
#                 break

#         if not existe:
#             return num_id
            
    
# def criar_chamado():
#     print("=== Criar Chamado ===")
    
#     nome = input("Seu nome: ")
#     problema = input("Descreva o problema: ")
    
#     banco_db = []   
    
#     id_ = escolher_id(banco_db)
    
#     banco_db = {
#         "id": id_,
#         "nome": nome,
#         "problema": problema,
#         "status": "Aberto"
#     }
    
#     print(f"\nChamado criado com sucesso! ID: {id_}\n")
    
#     return banco_db

# def opcao_menu():
#     benvindo()
#     menu()
    
#     while True:
#         try:
#             opcao = int(input("\n- "))
#         except ValueError:
#             print("\nALERTA!!\n- Erro de valor encontrado!!")
#             print("\n- Digite apenas números!")
            
#             print("\n1. Criar Chamado")
#             print("2. Listar Ordem de Chamado")
#             print("3. Atualizar Status")
#             print("4. Tecnico de TI")
#             print("5. Sair")
#             continue

#         else:
#             if opcao < 1 or opcao > 5:
#                 print("\nALERTA!!\n- Opção inválida!!\n")
                
#                 continue
#             else:
#                 print("\n- Menu Acessado com sucesso!!\n")
            
#         if opcao == 1:
#             criar_chamado()
#         elif opcao == 2:
#             listar_chamado()
#         elif opcao == 3:
#             atualizar_status()
#         elif opcao == 4:
#             menu_ti()
#         elif opcao == 5:
#             print("Até Breve..")
            
#         finally:
#             print("LOG: operação do menu registrada.\n")
        
# opcao_menu()

###############

import random

def benvindo():
    print("==== Bem-Vindo ao Chamados de TI ====\n")


def menu():
    print("Digite o numero relacionado ao seu caso..")
    print("1. Criar Chamado")
    print("2. Lista de Chamados")
    print("3. Tecnico TI")
    print("4. Sair")


def escolher_id(banco):
    while True:
        num_id = random.randint(100, 999)

        if num_id in banco:
            continue
        else:
            return num_id


def criar_chamado(banco):
    print("=== Criar Chamado ===")

    nome = input("Seu nome: ")
    problema = input("Descreva o problema: ")
    
    while True:
        try:
            prioridade = int(input("Qual Nivel de prioridade? 1. Alto, 2. Médio, 3. Baixo\n- "))
        except ValueError:
            print("\nALERTA!!\n- Erro de valor encontrado!! Escolha um Numero..")
            continue
        else:
            if prioridade < 1 or prioridade > 3:
                print("Opção inválida.\n")
                continue
        finally:
            print("Sistema diz- [LOG] operação de prioridade de chamado registrada.")
            
        if prioridade == 1:
            prioridade_ = prioridade
            break

        elif prioridade == 2:
            prioridade_ = prioridade
            break

        elif prioridade == 3:
            prioridade_ = prioridade
            break
    
    try:
        id_ = escolher_id(banco)

        if id_ < 0:
            raise ValueError("ID inválido: Numero negativo.")

    except ValueError as e:
        print(f"Erro: {e}")

    finally:
        print("Sistema diz- [LOG] tentativa de criação registrada.\n")
    
    banco[id_] = {
        "nome": nome,
        "problema": problema,
        "prioridade": prioridade_,
        "status": "Aberto"
    }

    print(f"\nChamado criado com sucesso! ID: {id_}\n")

    


def listar_chamado(banco):
    print("=== Lista de Chamados ===\n")
    
    if not banco:
        print("Nenhum chamado cadastrado.\n")
        return
    
    for id_, dados in banco.items():
        print(f"ID: {id_}")
        print(f"Nome: {dados['nome']}")
        print(f"Problema: {dados['problema']}")
        print(f"Status: {dados['status']}")
        print("-" * 30)
        

def atualizar_status(banco):
    print("=== Atualizar Status ===")
    
    try:
        id_busca = int(input("Digite o ID do chamado: "))

        if id_busca < 0:
            raise ValueError("ID não pode ser negativo.")

        chamado = banco[id_busca]  # pode dar KeyError

    except ValueError as e:
        print(f"Erro: {e}")

    except KeyError:
        print("Erro: Chamado não encontrado.")

    else:
        novo_status = input("Novo status: ")
        chamado["status"] = novo_status
        print("Status atualizado com sucesso.\n")

    finally:
        print("LOG: tentativa de atualização registrada.\n")


def menu_ti(banco):
    print("=== Menu do Técnico ===")
    
    cod_tec = 2310
    
    while True:
        try:
            cod = int(input("Digite seu Codigo de Técnico: "))
        except ValueError:
            print("\nALERTA!!\n- Erro de valor encontrado!!")
            continue
        else:
            if cod == cod_tec:
                print("=== Bem-Vindo Tecnico ===\n")
                break
            else:
                print("Codigo inválido.\n")
                continue
            
    menu_tecnico()
    
    print("nao acabou")
    

def menu_tecnico():
    print("1. Criar Chamado")
    print("2. Lista de Chamados")
    print("3. Tecnico TI")
    print("4. Sair")

def opcao_menu():
    banco = {}
    benvindo()
    
    while True:
        
        menu()

        try:
            opcao = int(input("- "))

        except ValueError:
            print("\nALERTA!!\n- Erro de valor encontrado!!")
            continue

        else:
            if opcao < 1 or opcao > 5:
                print("Opção inválida.\n")
                continue
        finally:
            print("Sistema diz- [LOG] operação do menu registrada.\n")
            
        if opcao == 1:
            criar_chamado(banco)

        elif opcao == 2:
            listar_chamado(banco)

        elif opcao == 3:
            menu_ti(banco)

        elif opcao == 4:
            print("Até breve.")
            break
        
opcao_menu()
