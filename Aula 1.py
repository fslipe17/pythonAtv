#Atividade pratica Aula 1

    #Entrada de Dados
    # Solicite o Nome Completo do estudante.
    # Solicite o nome do Curso (ex: ADS ou Engenharia de Software).
    # Solicite o Ano de Nascimento (converta obrigatoriamente para int).
    # Solicite a Cidade onde o aluno reside.

        # nome_completo = input('Escreva seu Nome completo: ')
        # nome_curso = input('Escreva o nome do seu Curso completo (ex: ADS ou Engenharia de Software): ')
        # ano_nascimento = int(input('Escreva sua Ano de Nascimento: '))
        # cidade = input('Escreva a Cidade onde reside: ')

    # Calcule a idade aproximada do aluno subtraindo o ano de nascimento do ano atual
    # (considere 2026 como ano de referência)

        # idade = ano_nascimento - 2026
        
    ######################

    #Lista Atividades Aula 1

        #Atividade 1

            # nome = input('Digite seu nome: ')
            # idade = input('Digite sua Idade: ')
            # cidade = input('Digite a cidade onde reside: ')
            
            # print(f'Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}.')
            
        #####################

        #Atividade 2

            # frase = input('Digite uma Frase: ')
            
            # print(frase)
            # print(frase)
            # print(frase)
            
        #####################
            
        #Atividade 3
        
            # algo = input('Digite algo: ')
                
            # print(type(algo))
            
        #####################
            
        #Atividade 4
        
            # n = 10
            # n2 = "10"
            
            # print(n + n2)
            
            #TypeError: unsupported operand type(s) for +: 'int' and 'str'
            
            #Sendo Python uma linguagem de alto nivel, ela é muito rigorosa sobre
            # as regras impostas a ela, isso significa que eu nao posso somar um numero
            # com uma string, pois a linguagem não sabe se vc quer somar numeros ou
            # concatenar strins. 
            
        #####################
            
        #Atividade 5

            # print('Dica de e-mail..\n')        
            
            # nome = input('Digite um nome: ')
            # sobre_nome = input('Digite seu sobrenome: ')
            
            # print('Processando....\n')
            
            # e_mail = nome.lower() + "." + sobre_nome.lower() + "@faculdade.com.br" 
            
            # print(f'Aqui está {e_mail}')
            
        #####################
            
        #Atividade 6
        
            # produto = input('Digite o nome do produto: ')
            # quant_estoque = int(input('Digite a quantidade no estoque: '))
            # preco_uni = float(input('Digite o valor do produto: '))
            
            # print(f'\n{produto}.\nQuantidade: {quant_estoque}\nPreço: R${preco_uni}')
        
        #####################
        
        #Atividade 7
        
            # n1 = input('Digite um numero: ')
            # n2 = input('Digite outro numero: ')
            
            # n3 = n1 + n2
            
            # print(n3)
            
            #O "calculo" acima, ao invez de soma os "numeros" ele concatena os numeros,
            # pois o input ele extrai só string, sendo assim o desenvolvedor precisa expecificar
            # qual tipo de variavel ele quer int, float ou bool
        
        #####################
        
        #Atividade 8
        
            # idade = int(input('Digite sua idade: \n'))
            
            # ano_nascimento = 2026 - idade
            
            # print(f'Você nasceu em: {ano_nascimento}')
                    
        #####################
        
        #Atividade 9
        
            # a = int(input('Digite um numero: \n'))
            # b = int(input('Digite outro numero: \n'))
            
            # c = b
            
            # d = a
            
            # a = b
            
            # b = d
            
            # print(a)
            # print(b)
            
            # print(c)
            # print(d)
        
        #####################
        
        #Atividade 10
        
convidado = input('Nome do convidado: \n')

evento = input('Nome do evento: \n')

largura = 19
largura_borda = 21

borda = "=" * largura_borda

titulo = linha_conv = 'Convite'.center(largura)
linha_vazia = "*" + " " * largura + "*"
linha_foi = "*" + 'Vc Foi'.center(largura) + "*"
linha_conv = "*" + 'convidado'.center(largura) + "*"
linha_nome = "*" + f"{convidado}".center(largura) + "*"
linha_para = "*" + 'para o'.center(largura) + "*"
linha_evento = "*" + f" Evento no(a) {evento} ".center(largura) + "*"

print(borda)
print(titulo)
print(borda)
print(linha_vazia)
print(linha_nome)
print(linha_conv)
print(linha_para)
print(linha_evento)
print(linha_vazia)
print(borda)

####################
