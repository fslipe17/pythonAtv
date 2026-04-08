#Luiz Felipe Da Silva

#Nivel 1
#atv 1

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     print("Você é maior de idade")
# else: 
#     print('Você é menor de idade')
    
######

#atv 2

# numero = float(input("Digite um numero: "))

# if numero > 0:
#     print('Este numero é Positivo')
# elif numero < 0:
#     print('Este numero é Negativo')
# else: 
#     print('Zero')
    
#####

#atv 3

# numero = int(input('Digite um numero inteiro: '))

# # numero = numero % 2

# if numero % 2 == 0:
#     print('Esse numero é par')
# else: # numero == 1:
#     print('Este numero é impar')

#####

#atv 4

# media_aluno = (float(input("Qual sua média: ")))
# #falta_aluno = (float(input("Quantas faltas vc tem? ")))

# if media_aluno >= 7: #and falta_aluno <= 24:
#     print(f'Passou de ano. A media foi {media_aluno}')
# else: 
#     print(f'Reprovou de ano. A media foi {media_aluno}')

#####

#atv 5

# numero = int(input('Digite um numero inteiro: '))

# numero2 = int(input('Digite outro numero inteiro: '))

# if numero > numero2:
#     print(f'O Numero {numero} é maior que o {numero2}')
# elif numero < numero2:
#     print(f'O Numero {numero2} é maior que o {numero}')
# else:
#     print('Os numeros são iguais')

####

#Nivel 2

#Atv 6

# idedeNadador = int(input('Digite sua idade: '))

# if idedeNadador >= 5 and idedeNadador <= 7:
#     print('Infantil A')
    
# elif idedeNadador >= 8 and idedeNadador <= 10:
#     print('Infantil B')
    
# elif idedeNadador >= 11 and idedeNadador <= 13:
#     print('Juvenil A')
# elif idedeNadador >= 14 and idedeNadador <= 17:
#     print('Juvenil B')
# elif idedeNadador >= 18:
#     print('Adulto')

####

#atv 7

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# imc = peso / (altura*altura) 

# if imc < 18.5:
#     print('Abaixo do peso')
# elif imc >= 18.5 and imc <= 24.9:
#     print('Peso ideal! Parabéns!!')
# else:
#     print('Acima do peso')

#####

#atv 8

# celcius = float(input('Digite a temperatura em Celsius: ')) 

# fahrenheit = bool(input('Você quer converter para Fahrenheit? Sim ou Não? ')).lower

# convertido

# if fahrenheit == true:
#     convertido = (celsius * 9/5) + 32
#     print(f' O grau {celsius} em Fahrenheit é {convertido}')
# else:
#     print(celsius)

##########

# Atv 9 

# produto = int(input("Digite o valor de um produto: "))

# if produto < 0:
#     print(f'O produto tem um valor negativo')
# elif produto <= 50:
#     print(f'O valor do produto está Barato')
# elif produto <= 100:
#     print(f'O valor do produto está em um preço medio')
# elif produto > 100:
#     print(f'O valor do produto está Caro')

#############

# Atv 10

# turno = input("Digite o Turno da sua aula, Usando M, V, N: ").lower()


# if turno == 'm':
#     print('Bom dia')
# elif turno == 'v':
#     print('Boa Tarde')
# elif turno == 'n':
#     print('Boa Noite')

###########

# Atv 11

# login = input('Digite seu login: ')
# senha = input('Digite sua senha: ')

# if login == 'admin' and senha == 'fatec123':
#     print('Bem vindo!!')
# else:
#     print('CAI FORA DAQUI!!!')

#########

# Atv 12

######


# EXERCÍCIOS COM LAÇO WHILE (Condições e Validações)
# Foco: Repetição baseada em estados e interatividade.
# dia 07/04/26
 
# 1. Até o Zero: Peça números ao usuário repetidamente. O
# programa só para quando ele digitar 0.

# num = int(input('Digite um numero: '))

# while num != 0:
#     num = int(input('Digite outro numero até vc acertar o numero: '))
# print('Fim do programa')
    
# 2. Validação de Nota: Peça uma nota entre 0 e 10. Enquanto o
# valor for inválido, continue pedindo.

# nota = float(input('Digite a nota: '))

# while nota < 0 or nota > 10:
#     nota = float(input('Digite um numero valido: '))
#     print('Voce Digitou um numero valido')

# print('Fim do programa')

# 3. Senha de Acesso: Crie um sistema que peça uma senha e só
# libere o acesso quando a senha "python123" for digitada.
    
# senha = input('Digite a senha: ').lower()

# senhaCerta = "python123"

# while senha != senhaCerta:
#     senha = input('Digite a senha certa: ').lower()
#     print('Bem vindo!')
    
# print('Fim do programa')

# 4. Soma Acumulada: Peça números ao usuário e vá somando-os.
# Pare quando a soma total ultrapassar 100.

# num = int(input('Digite um numero: '))

# while num < 100:
#     num2 = int(input('Digite outro numero'))
#     num = num + num2
#     print('Voce excedeu o limite')

# print('Fim do programa')

# 5. Menu de Calculadora: Exiba um menu: [1] Somar [2] Subtrair
# [0] Sair. O programa deve repetir até o usuário escolher 0

# num = int(input('[1] Somar [2] Subtrair [0] Sair.\n'))

# while num != 0:
#     if num == 1:
#         num1 = int(input('Digite o primeiro numero: '))
#         num2 = int(input('Digite o segundo numero: '))
#         resultadoSoma = num1 + num2
#         print(resultadoSoma)
#     elif num == 2:
#         num1 = int(input('Digite o primeiro numero: '))
#         num2 = int(input('Digite o segundo numero: '))
#         resultadoSub = num1 - num2
#         print(resultadoSub)
#     else:
#         print('Até mais...')
#     num = int(input('\nGostei vamos de novo: [1] Somar [2] Subtrair [0] Sair.\n'))
    
# print('Fim do programa')

# 6. Adivinhação Simples: Defina um número secreto. O usuário deve tentar
# adivinhar; o programa avisa se o chute foi alto ou baixo até ele acertar.

# print("================================")
# print("Bem-vindo ao jogo de Adivinhação")
# print("================================")


# import random

# numero = random.randint(0, 100)

# print("")

# tentativas = 10
# rodada = 1

# while (rodada <= tentativas):
#     print("Tentativa {} de 10".format(rodada, tentativas))

#     chute_str = input("Digite o seu numero: ")
#     print("Você Digitou", chute_str)
#     chute = int(chute_str)

#     acertou = chute == numero
#     maior = chute < numero
#     menor = chute > numero

#     if(acertou):
#         print("Parabéns!! Você acertou ;)")
#         rodada = rodada + 1
#     else:
#         if(maior):
#             print("O número é maior que", chute)
#         elif(menor):
#             print("O numero é menor que", chute)

#     rodada = rodada + 1

# print("Fim de jogo")

# 7. População de Bactérias: Uma colônia dobra a cada hora. Começando
# com 1 bactéria, em quantas horas ela ultrapassará 1.000.000?

bacterias = 1
horas = 0

while bacterias <= 1000000:
    bacterias *= 2 #2 horas
    horas += 1 #variavel horas adicina mais 1, e a cada 2h a variavel bactéria 
    #multiplica por 2

print(f'Ultrapassa 1.000.000 em {horas} horas')
    

    



    


#media_aluno = (float(input("Qual sua média: ")))
#falta_aluno = (float(input("Quantas faltas vc tem? ")))

#if media_aluno >= 6 and falta_aluno <= 24:
#    print("Passou de ano")
#    print(f'A media foi {media_aluno}')
#else: 
#    print("Reprovou de ano")
#    print(f'A media foi: {media_aluno}')
    
#####

# tipo_cliente = input("Digite o tipo: Comum, Gestante, Idoso: ").lower()
    
# if tipo_cliente == 'idoso' or tipo_cliente == 'gestante':
#     print('Dirija-se para o Guichê Prioritario.')
# elif tipo_cliente == 'comum':
#     print('Dirija-se para o Guichê 1')

#####

# salario = float(input('Digite seu salario: '))

# if salario <= 1000:
#     print('Faixa 1')
# elif salario <= 10000 and salario > 1000:
#     print('Faixa 2')
#     if salario > 4000:
#         print('Nordeste')
# else:
#     print('Faixa 3')
    
