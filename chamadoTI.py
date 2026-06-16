# Nomes:
#   Gabriel Seiji Furuta Soares - RA 47017198 
#   Gabriel Victor de Nogueira e Silva - RA 48549975
#   Bruno Suzuki - RA 47142740
#   Luiz Felipe da Silva - RA 48553522
#   Erick Miguel Ranolfi - RA 47752840

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
        
        if num_id not in banco:
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
            print("Sistema diz: Operação de prioridade de chamado registrada.")
        
        prioridade_ = prioridade
        break
    
    try:
        id_ = escolher_id(banco)
    
        if id_ < 0:
            raise ValueError("ID inválido: Numero negativo.")
            
    
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    finally:
        print("Sistema diz: Tentativa de criação registrada.\n")
    
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
        print("\n--------------------------------------------------------\n")

def menu_ti1(banco):
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
                menu_ti_princ(banco)
                break
            else:
                print("Codigo inválido.\n")
        finally:
            print("Sistema diz: Operação Menu-Tecnico registrada.\n")

def menu_ti_princ(banco):
    print("=== Bem-Vindo Tecnico ===\n")
    
    while True:
        menu_tecnico()
        
        try:
            op_tec = int(input("\n- Digite o numero de sua escolha: "))
        except ValueError:
            print("\nALERTA!!\n- Erro de valor encontrado!!")
            continue
        else:
            if op_tec not in [1,2,3,4,5]:
                print("Opção inválida.\n")
                continue
        finally:
            print("Sistema diz: Operação Menu-Tecnico-Cadastrado registrada.\n")
            
        if op_tec == 1:
            listar_chamado(banco)
        elif op_tec == 2:
            atender_chamado(banco)
        elif op_tec == 3:
            ver_historico_fechados(banco)
        elif op_tec == 4:
            excluir_chamado(banco)
        elif op_tec == 5:
            print("Até breve.")
            break

def menu_tecnico():
    print("1. Ver Chamado")
    print("2. Atender Chamado")
    print("3. Ver Historico de Chamados Fechados")
    print("4. Excluir Chamado")
    print("5. Sair")

def atender_chamado(banco):
    print("=== Atender Chamado ===")
    
    try:
        id_chamado = int(input("Digite o ID do chamado: "))
        chamado = banco[id_chamado]
    except:
        print("Chamado inválido.")
        return
    
    if chamado["status"] == "Aberto":
        print("- Este chamado está disponível para atendimento.")
    else:
        print("- Este chamado não está disponível para atendimento.")
    
    tecnico = input("Nome do técnico responsável: ")
    diagnostico = input("Informe o diagnóstico inicial: ")
    
    chamado["tecnico"] = tecnico
    chamado["diagnostico"] = diagnostico
    chamado["status"] = "Em Atendimento"
    
    print("\nChamado atribuído com sucesso!")
    
    while True:
        resolver = input("\nO problema foi resolvido? (S/N): ").upper()
        
        if resolver not in ["S","N"]:
            print("Opção inválida.")
            continue
        
        print("Sistema diz: Operação de problema registrada.\n")
        
        if resolver == "S":
            chamado["status"] = "Fechado"
            chamado["solucao"] = input("Descreva a solução aplicada: ")
            print("Chamado encerrado com sucesso!")
        else:
            print("Chamado permanece em atendimento.")
        
        break

def excluir_chamado(banco):
    try:
        id_chamado = int(input("ID para excluir: "))
        
        if id_chamado < 0:
            raise ValueError("ID não pode ser negativo.")

        banco.pop(id_chamado)

    except ValueError as e:
        print(f"Erro: {e}")

    except KeyError:
        print("Erro: Chamado não encontrado.")

    else:
        print("Chamado excluído com sucesso.")

    finally:
        print("Sistema diz: Tentativa de exclusão registrada.\n")
        
def ver_historico_fechados(banco):
    print("=== Histórico de Chamados Fechados ===\n")
    
    encontrados = False

    for id_, dados in banco.items():
        if dados["status"] == "Fechado":
            encontrados = True
            print(f"ID: {id_}")
            print(f"Nome: {dados['nome']}")
            print(f"Problema: {dados['problema']}")
            print(f"Status: {dados['status']}")
            
            if "tecnico" in dados:
                print(f"Técnico: {dados['tecnico']}")
            
            if "solucao" in dados:
                print(f"Solução: {dados['solucao']}")
            
            print("\n--------------------------------------\n")

    if not encontrados:
        print("Nenhum chamado fechado encontrado.\n")

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
            if opcao < 1 or opcao > 4:
                print("Opção inválida.\n")
                continue
        finally:
            print("Sistema diz: Operação do menu registrada.\n")
            
        if opcao == 1:
            criar_chamado(banco)
    
        elif opcao == 2:
            listar_chamado(banco)
    
        elif opcao == 3:
            menu_ti1(banco)
    
        elif opcao == 4:
            print("Até breve.")
            break

opcao_menu()
