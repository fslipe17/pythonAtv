import random

def escolher_pergunta():
    perguntas = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "alternativas": ["A) São Paulo", "B) Brasília", "C) Rio de Janeiro", "D) Salvador"],
            "resposta": "B"
        },
        {
            "pergunta": "Quanto é 2 + 2?",
            "alternativas": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual linguagem estamos usando?",
            "alternativas": ["A) Java", "B) C++", "C) Python", "D) JavaScript"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual planeta é conhecido como planeta vermelho?",
            "alternativas": ["A) Terra", "B) Marte", "C) Júpiter", "D) Vênus"],
            "resposta": "B"
        }
    ]
    
    for i, p in enumerate(perguntas):
        print(f"\nPergunta {i + 1}: {p['pergunta']}")

        for alt in p["alternativas"]:
            print(alt)
            
        resposta = input("Sua resposta: ").upper()

        if resposta == p["resposta"]:
            print("Correto!")
            pontuacao()
        else:
            print(f"Errado! Resposta correta: {p['resposta']}")
        

def pontuacao(jogador):
    jogador.append(1)
    
    
def verificar_resposta(resp, correta):
    return resp == correta

def saudacoes():
    print("=============================================================")
    print("    Bem-Vindo ao C, um jogo de perguntas e respostas.\n \nFeito para você se divertir e aprender tudo em um só lugar.\n")
    print("=============================================================")
    
    nome_jogador = input("- Para começarmos me diga seu nome de jogador: ")
    
    print(f"\n- Boas Vindas {nome_jogador}...\n")
    
    return nome_jogador
    

def exibir_menu():
    print("-------MENU-------")
    print("-----1. Jogar-----")
    print("-2. Exibir Pontos-")
    print("-----3. Sair------")
    
    resposta = int(input("\n- Digite sua escolha: \n"))
    
    return resposta
    
def criar_jogador(nome):
    return {
        "nome": nome,
        "pontos": 0,
        "vidas": 3,
        "historico": []
    }

def exibir_status(jogador):
    print("\n=== STATUS ===")
    print(f"Nome: {jogador['nome']}")
    print(f"Pontos: {jogador['pontos']}")
    print(f"Vidas: {jogador['vidas']}")
    print(f"Acertos: {jogador['historico'].count(True)}")
    
def jogar():
    escolher_pergunta()

def play():
    nome_jogador = saudacoes()
    
    menu_res = exibir_menu()
    
    jogador = criar_jogador(nome_jogador)
    
    while True:
        if menu_res == 1:
            jogar()
            
        elif menu_res == 2:
            exibir_status(jogador)
            break
            
        elif menu_res == 3:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


play()
