import random

def loading_perguntas():
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
        },
        {
            "pergunta": "Quem pintou a Mona Lisa?",
            "alternativas": ["A) Van Gogh", "B) Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual é o maior oceano do mundo?",
            "alternativas": ["A) Atlântico", "B) Índico", "C) Ártico", "D) Pacífico"],
            "resposta": "D"
        },
        {
            "pergunta": "Quantos continentes existem?",
            "alternativas": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual é o símbolo químico do ouro?",
            "alternativas": ["A) Au", "B) Ag", "C) Fe", "D) O"],
            "resposta": "A"
        },
        {
            "pergunta": "Quem escreveu 'Dom Casmurro'?",
            "alternativas": ["A) Machado de Assis", "B) José de Alencar", "C) Clarice Lispector", "D) Monteiro Lobato"],
            "resposta": "A"
        },
        {
            "pergunta": "Qual planeta é o maior do sistema solar?",
            "alternativas": ["A) Terra", "B) Marte", "C) Júpiter", "D) Saturno"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual linguagem é usada para estilizar páginas web?",
            "alternativas": ["A) HTML", "B) CSS", "C) Python", "D) Java"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é a raiz quadrada de 64?",
            "alternativas": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "resposta": "C"
        },
        {
            "pergunta": "Quem foi o primeiro homem a pisar na Lua?",
            "alternativas": ["A) Yuri Gagarin", "B) Neil Armstrong", "C) Buzz Aldrin", "D) Elon Musk"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o idioma mais falado no mundo?",
            "alternativas": ["A) Inglês", "B) Espanhol", "C) Mandarim", "D) Português"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual é o menor país do mundo?",
            "alternativas": ["A) Mônaco", "B) Vaticano", "C) Malta", "D) Luxemburgo"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o animal terrestre mais rápido?",
            "alternativas": ["A) Leão", "B) Guepardo", "C) Cavalo", "D) Tigre"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual gás é essencial para a respiração humana?",
            "alternativas": ["A) Oxigênio", "B) Nitrogênio", "C) Gás carbônico", "D) Hélio"],
            "resposta": "A"
        },
        {
            "pergunta": "Qual empresa criou o Windows?",
            "alternativas": ["A) Apple", "B) Microsoft", "C) Google", "D) IBM"],
            "resposta": "B"
        },
        {
            "pergunta": "Em que país fica a Torre Eiffel?",
            "alternativas": ["A) Itália", "B) Espanha", "C) França", "D) Alemanha"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual é o resultado de 10 x 10?",
            "alternativas": ["A) 50", "B) 100", "C) 10", "D) 1000"],
            "resposta": "B"
        }
    ]
    return perguntas

def escolher_pergunta(jogador, perguntas):
    i = 0
    
    while i < len(perguntas):
        j = int(random.random() * len(perguntas))
        
        perguntas[i], perguntas[j], perguntas[j], perguntas[i]
        
        i += 1

    for i, p in enumerate(perguntas):
        
        print(f"\nPergunta {i + 1}: {p['pergunta']}")
        
        alternativas = p["alternativas"][:]
        
        k = 0
        
        while k < len(alternativas):
            j =  int(random.random() * len(alternativas))
            
            perguntas[k], perguntas[j], perguntas[j], perguntas[k]
            
            k += 1

        for alt in p["alternativas"]:
            print(alt)
            
        
        text_correto = None
        
        for alt in p["alternativas"]:
            if alt[0] == p["resposta"]:
                text_correto = alt
                
        
        nova_resp = None
        
        for alt in alternativas:
            if alt == text_correto:
                nova_resp = alt[0]
                
            
        resposta = input("Sua resposta: ").upper()

        if verificar_resposta(resposta, nova_resp):
            print("Correto!")
            pontuacao(jogador)
            jogador["historico"].append(True)
        else:
            print(f"Errado! Resposta correta: {nova_resp}")
            jogador["historico"].append(False)
            jogador["vidas"] -= 1

def pontuacao(jogador):
    jogador["pontos"] += 1
    
    
def verificar_resposta(resp, correta):
    return resp == correta

def saudacoes():
    print("=============================================================")
    print("    Bem-Vindo ao C, um jogo de perguntas e respostas.\n \nFeito para você se divertir e aprender tudo em um só lugar.\n")
    print("=============================================================")
    
    nome_jogador = input("- Para começarmos me diga seu nome de jogador: ")
    
    print(f"\n- Boas Vindas {nome_jogador}...\n")
    
    return nome_jogador

def tela_jogo():
    print("Adorei sua Resposta, Vamos começar nosso GAME.. ")
    

def exibir_menu():
    print("------- MENU -------")
    print("----- 1. Jogar -----")
    print("- 2. Exibir Pontos -")
    print("----- 3. Sair ------")
    
    resposta = int(input("\n- Digite sua escolha: "))
    
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
    
def jogar(jogador):
    perguntas = loading_perguntas()
    tela_jogo()
    escolher_pergunta(jogador, perguntas)

def play():
    nome_jogador = saudacoes()
    
    jogador = criar_jogador(nome_jogador)
    
    while True:
        menu_res = exibir_menu()
        
        if menu_res == 1:
            jogar(jogador)
            
        elif menu_res == 2:
            exibir_status(jogador)
            break
            
        elif menu_res == 3:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


play()
