#Atividade pratica Aula 1

Luiz Felipe Da Silva

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

        # 1. Dados Pessoais: Crie variáveis para armazenar seu nome, sua idade e sua
        #     cidade. Imprima uma frase como: "Olá, meu nome é [nome], tenho [idade]
        #     anos e moro em [cidade]."

            # nome = input('Digite seu nome: ')
            # idade = input('Digite sua Idade: ')
            # cidade = input('Digite a cidade onde reside: ')
            
            # print(f'Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}.')
            
        #####################

        #2. Eco Computacional: Escreva um programa que peça uma frase ao usuário e a
            # imprima três vezes seguidas

            # frase = input('Digite uma Frase: ')
            
            # print(frase)
            # print(frase)
            # print(frase)
            
        #####################
            
        # 3. Investigação de Tipos: Peça para o usuário digitar algo. Imprima o valor
        #       digitado e, em seguida, use a função type() para mostrar ao aluno qual é o tipo
        #       de dado que o Python capturou (lembre-o que o input sempre gera str).
        
            # algo = input('Digite algo: ')
                
            # print(type(algo))
            
        #####################
            
        # 4. Comentário Didático: Crie um código que armazene o número 10 em uma
            # variável e o texto "10" em outra. Use um comentário de código (#) para
            # explicar por que não podemos somar essas duas variáveis diretamente.
        
            # n = 10
            # n2 = "10"
            
            # print(n + n2)
            
            #TypeError: unsupported operand type(s) for +: 'int' and 'str'
            
            #Sendo Python uma linguagem de alto nivel, ela é muito rigorosa sobre
            # as regras impostas a ela, isso significa que eu nao posso somar um numero
            # com uma string, pois a linguagem não sabe se vc quer somar numeros ou
            # concatenar strins. 
            
        #####################
            
        # 5. Montador de E-mail: Peça o nome e o sobrenome do usuário separadamente. Ao final, imprima uma
        # sugestão de e-mail corporativo: nome.sobrenome@faculdade.com.br.

            # print('Dica de e-mail..\n')        
            
            # nome = input('Digite um nome: ')
            # sobre_nome = input('Digite seu sobrenome: ')
            
            # print('Processando....\n')
            
            # e_mail = nome.lower() + "." + sobre_nome.lower() + "@faculdade.com.br" 
            
            # print(f'Aqui está {e_mail}')
            
        #####################
            
        # 6. Ficha de Produto: Solicite o nome de um produto, a quantidade em estoque (converta para int) e o
        # preço unitário (converta para float). Imprima as informações formatadas.

            # produto = input('Digite o nome do produto: ')
            # quant_estoque = int(input('Digite a quantidade no estoque: '))
            # preco_uni = float(input('Digite o valor do produto: '))
            
            # print(f'\n{produto}.\nQuantidade: {quant_estoque}\nPreço: R${preco_uni}')
        
        #####################
        
        # 7. Concatenador de Números: Peça dois números ao usuário, mas não os converta para int. Imprima a
        # soma deles. O aluno verá que o resultado será a junção dos números (ex: 5 + 5 = 55). Peça para ele
        # explicar isso em um comentário.
        
            # n1 = input('Digite um numero: ')
            # n2 = input('Digite outro numero: ')
            
            # n3 = n1 + n2
            
            # print(n3)
            
            #O "calculo" acima, ao invez de soma os "numeros" ele concatena os numeros,
            # pois o input ele extrai só string, sendo assim o desenvolvedor precisa expecificar
            # qual tipo de variavel ele quer int, float ou bool
        
        #####################
        
        # 8. Ano de Nascimento: Peça a idade atual do usuário e calcule o ano em que ele nasceu (considere o ano
        # atual 2026). Use apenas a subtração -.
        
            # idade = int(input('Digite sua idade: \n'))
            
            # ano_nascimento = 2026 - idade
            
            # print(f'Você nasceu em: {ano_nascimento}')
                    
        #####################
        
        # 9. Troca de Valores: Crie duas variáveis, a e b, e peça valores para elas. Em seguida, faça com que a
        # receba o valor de b e b receba o valor de a. Imprima os novos valores (Dica: você precisará de uma
        # terceira variável "auxiliar" para não perder os dados).
        
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
        
        # 10. Gerador de Convite: Peça o nome de um convidado e o nome de um evento. Imprima um convite
        # personalizado com bordas decorativas usando caracteres como * ou =.
        
            # convidado = input('Nome do convidado: \n')
            
            # evento = input('Nome do evento: \n')
            
            # largura = 19
            # largura_borda = 21
            
            # borda = "=" * largura_borda
            
            # titulo = linha_conv = 'Convite'.center(largura)
            # linha_vazia = "*" + " " * largura + "*"
            # linha_foi = "*" + 'Vc Foi'.center(largura) + "*"
            # linha_conv = "*" + 'convidado'.center(largura) + "*"
            # linha_nome = "*" + f"{convidado}".center(largura) + "*"
            # linha_para = "*" + 'para o'.center(largura) + "*"
            # linha_evento = "*" + f" Evento no(a) {evento} ".center(largura) + "*"
            
            # print(borda)
            # print(titulo)
            # print(borda)
            # print(linha_vazia)
            # print(linha_nome)
            # print(linha_conv)
            # print(linha_para)
            # print(linha_evento)
            # print(linha_vazia)
            # print(borda)

##################
