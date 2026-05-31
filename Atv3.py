# Lista de Exercícios: Condicionais e Lógica

# Luiz Felipe Da Silva

# Nível 1: Condicional Simples e Composta (if/else)

# 1. Maior de Idade: Peça a idade do usuário e diga se ele é "Maior de Idade"
# ou "Menor de Idade".

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     print("Você é maior de idade")
# else: 
#     print('Você é menor de idade')
    
################################

# 2. Positivo ou Negativo: Receba um número e informe se ele é positivo,
# negativo ou zero.

# numero = float(input("Digite um numero: "))

# if numero > 0:
#     print('Este numero é Positivo')
# elif numero < 0:
#     print('Este numero é Negativo')
# else: 
#     print('Zero')
    
################################

# 3. Par ou Ímpar: Receba um número inteiro e diga se ele é par ou ímpar
# (Dica: use % 2).

# numero = int(input('Digite um numero inteiro: '))

# # numero = numero % 2

# if numero % 2 == 0:
#     print('Esse numero é par')
# else: # numero == 1:
#     print('Este numero é impar')

##################################

# 4. Aprovação Escolar: Peça duas notas, calcule a média e diga "Aprovado"
# se a média for 7.0 ou superior, caso contrário diga "Reprova

# media_aluno = (float(input("Qual sua média: ")))
# #falta_aluno = (float(input("Quantas faltas vc tem? ")))

# if media_aluno >= 7: #and falta_aluno <= 24:
#     print(f'Passou de ano. A media foi {media_aluno}')
# else: 
#     print(f'Reprovou de ano. A media foi {media_aluno}')

####################################

# 5. Maior de Dois: Peça dois números e exiba qual deles é o maior.

# numero = int(input('Digite um numero inteiro: '))

# numero2 = int(input('Digite outro numero inteiro: '))

# if numero > numero2:
#     print(f'O Numero {numero} é maior que o {numero2}')
# elif numero < numero2:
#     print(f'O Numero {numero2} é maior que o {numero}')
# else:
#     print('Os numeros são iguais')

#####################################

# Nível 2: Condicional Encadeada (if/elif/else

# 6. Classificação de Atleta: Receba a idade de um nadador e classifique-o: 5-7
# anos (Infantil A), 8-10 (Infantil B), 11-13 (Juvenil A), 14-17 (Juvenil B), acima de
# 18 (Adulto)

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

####################################

# 7. Calculadora de IMC: Peça peso e altura, calcule o IMC (peso/altura2). Exiba se
# está: Abaixo do peso (<18.5), Peso ideal (18.5-24.9) ou Sobrepeso (>=25).

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# imc = peso / (altura*altura) 

# if imc < 18.5:
#     print('Abaixo do peso')
# elif imc >= 18.5 and imc <= 24.9:
#     print('Peso ideal! Parabéns!!')
# else:
#     print('Acima do peso')

#####################################

# 8. Conversor de Temperatura: Peça uma temperatura e pergunte se o usuário
# quer converter de Celsius para Fahrenheit ou vice-versa. Use elif para
# processar a escolha.

# print("Olá esse programa converte Celsius para Fahrenheit e vice-versa. o que vc deseja fazer?\n")

# escolha = int(input("Digite para calcular: 1. Celsius => Fahrenheit  2. Fahrenheit => Celsius: \n"))

# if escolha == 1:
#     celsius = float(input('Digite a temperatura em Celsius: \n')) 
    
#     convertido = (celsius * 9/5) + 32
#     print(f'O grau {celsius} em Fahrenheit é {convertido}' + "º Fahrenheit\n")
    
#     print("Fim do programa ...")
# elif escolha == 2:
#     fahrenheit = float(input('Digite a temperatura em Fahrenheit: \n')) 

#     # (32 °F − 32) × 5/9 = 0 °C
#     convertido = (fahrenheit - 32) * 5/9
#     print(f'O grau {fahrenheit} em Celsius é {convertido}' + "º Celsius\n")
    
#     print("Fim do programa ...")
# else:
#     print("Resposta invalida, Fim do programa ...")

###############################

# 9. Análise de Produto: Peça o preço de um produto e categorize-o: "Barato" (até
# R$ 50), "Médio" (entre R$ 50 e R$ 100) ou "Caro" (acima de R$ 100). 

# produto = int(input("Digite o valor de um produto: "))

# if produto < 0:
#     print(f'O produto tem um valor negativo')
# elif produto <= 50:
#     print(f'O valor do produto está Barato')
# elif produto <= 100:
#     print(f'O valor do produto está em um preço medio')
# elif produto > 100:
#     print(f'O valor do produto está Caro')

#############$#############

# 10. Turno de Estudo: Pergunte em que turno o aluno estuda (M para Matutino, V
# para Vespertino, N para Noturno). Imprima "Bom Dia!", "Boa Tarde!" ou "Boa
# Noite!

# turno = input("Digite o Turno da sua aula, Usando M. Manhâ, V. Tarde, N. Noite: ").lower()

# if turno == 'm':
#     print('Bom dia')
# elif turno == 'v':
#     print('Boa Tarde')
# elif turno == 'n':
#     print('Boa Noite')

#######################3######

# Nível 3: Operadores Lógicos (and, or, not)

# 11. Acesso ao Sistema: Peça usuário e senha. Exiba "Acesso Permitido" apenas se
# o usuário for "admin" e a senha for "fatec123".

# login = input('Digite seu login: ')
# senha = input('Digite sua senha: ')

# if login == 'admin' and senha == 'fatec123':
#     print('Acesso Permitido. Bem vindo!!')
# else:
#     print('CAI FORA DAQUI!!!')

#############################

# 12. Triângulo Válido: Receba três lados (A, B, C). Verifique se podem formar um
# triângulo: (A < B+C) e (B < A+C) e (C < A+B).

# a = float(input("Digite o lado A: "))
# b = float(input("Digite o lado B: "))
# c = float(input("Digite o lado C: "))

# if (a < b + c) and (b < a + c) and (c < a + b):
#     print("Forma um triângulo")
# else:
#     print("Não forma um triângulo")

#################################

# 13. Votação Obrigatória: Peça a idade do usuário. Diga se o voto é: "Obrigatório"
# (entre 18 e 70 anos) ou "Facultativo/Não vota" (menor de 18 ou maior de 70).
# Use or.

# idade = int(input("Digite sua idade: "))

# if idade < 18 or idade > 70:
#     print("Facultativo/Não vota")
# else:
#     print("Obrigatório votar")

##################################

# 14. Desconto de Farmácia: Um desconto é dado se o cliente tiver mais de 65 anos
# ou se o valor da compra for maior que R$ 100. Verifique se o cliente tem
# direito.

# idade = int(input("Digite sua idade: "))
# valor = float(input("Digite o valor da compra: "))

# if idade > 65 or valor > 100:
#     print("Tem direito ao desconto")
# else:
#     print("Não tem direito ao desconto")

#################################

# 15. Ano Bissexto: Um ano é bissexto se for divisível por 4 e (não divisível por 100
# ou divisível por 400). Peça um ano e verifique.

# ano = int(input("Digite o Ano atual: "))

# if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
#     print("Ano bissexto")
# else:
#     print("Não é bissexto")

###############################

# Lista de Exercícios: Condicionais e Lógica

# Nível 4: Estruturas Aninhadas (if dentro de if)

# 16. Sistema de Empréstimo: Pergunte o valor do empréstimo e a renda mensal. Se
# a renda for maior que R$ 2000, pergunte em quantas parcelas. Se a parcela
# exceder 30% da renda, negue o empréstimo; caso contrário, aprove.

# valor = float(input("Digite o valor do empréstimo: "))
# renda = float(input("Digite sua renda mensal: "))

# if renda > 2000:
#     parcelas = int(input("Em quantas parcelas deseja pagar? "))
#     valor_parcela = valor / parcelas

#     if valor_parcela > renda * 0.3:
#         print("Empréstimo negado")
#     else:
#         print("Empréstimo aprovado")
# else:
#     print("Empréstimo negado (renda insuficiente)")

################################

# 17. Login com Níveis: Peça o login. Se for "admin", peça a senha. Se a senha
# estiver correta, pergunte se quer "Reiniciar Sistema" ou "Desligar". Se o login
# não for "admin", diga "Acesso de Usuário Comum".

# login = input("Digite o login: ")

# if login == "admin":
#     senha = input("Digite a senha: ")

#     if senha == "1234":
#         opcao = input("Deseja 'Reiniciar Sistema' ou 'Desligar'? ")
#         print(f"Opção escolhida: {opcao}")
#     else:
#         print("Senha incorreta")
# else:
#     print("Acesso de Usuário Comum")

################################

# 18. Clima e Vestimenta: Pergunte se está chovendo (S/N). Se sim, pergunte se está
# ventando forte (S/N). Se chover e ventar, diga "Use capa de chuva reforçada".
# Se apenas chover, "Use guarda-chuva". Se não chover, diga "Tenha um bom
# dia"

# chuva = input("Está chovendo? (S/N): ").upper()

# if chuva == "S":
#     vento = input("Está ventando forte? (S/N): ").upper()

#     if vento == "S":
#         print("Use capa de chuva reforçada")
#     else:
#         print("Use guarda-chuva")
# else:
#     print("Tenha um bom dia")

#############################
