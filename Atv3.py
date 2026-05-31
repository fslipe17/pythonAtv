# Lista de Exercícios: Condicionais e Lógica

# LUIZ FELIPE DA SILVA

# =========================

# Nível 1: Condicional Simples e Composta (if/else)

# 1. Maior de Idade: Peça a idade do usuário e diga se ele é "Maior de Idade"
# ou "Menor de Idade".

# =========================

#Lê a idade do usuário e converte para inteiro
idade = int(input('Digite sua idade: '))

#Verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("Você é maior de idade")  # Se idade é maior ou igual a 18
else: 
    print('Você é menor de idade')  # Caso contrário 

print("Fim do programa\n")


# =========================

# 2. Positivo ou Negativo: Receba um número e informe se ele é positivo,
# negativo ou zero.

# =========================

# Recebe um número inteiro
numero = float(input("Digite um numero: "))

#Verifica se variavel numero maior que zero
if numero > 0:
    print('Este numero é Positivo') # se numero for maior que 0..
elif numero < 0:
    print('Este numero é Negativo')  # Se numero for menor que zero
else: 
    print('Zero')  # Se numero for igual a zero

print("Fim do programa\n")


# =========================

# 3. Par ou Ímpar: Receba um número inteiro e diga se ele é par ou ímpar
# (Dica: use % 2).

# =========================

# variavel numero que recebe um input que logo é convertido para numero inteiro 
numero = int(input('Digite um numero inteiro: '))

# Verifica se o resto da divisão por 2 é zero
if numero % 2 == 0:
    print('Número par') # Se o resto da divisão por 2 é == 0
else:
    print('Número ímpar') # Caso contrario

print("Fim do programa\n")

# =========================

# 4. Aprovação Escolar: Peça duas notas, calcule a média e diga "Aprovado"
# se a média for 7.0 ou superior, caso contrário diga "Reprovado".

# =========================

# Recebe a média do aluno em uma variavel float
media = float(input("Digite sua média: "))

# Verifica se a média é suficiente para aprovar
if media >= 7:
    print("Aprovado") # Se a media for maior ou igual a 7 
else:
    print("Reprovado") # Caso Contrario

print("Fim do programa\n")

# =========================

# 5. Maior de Dois: Peça dois números e exiba qual deles é o maior.

# =========================

#Recebe dois números inteiro 
n = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

#Compara os dois valores Se n é maior que n2
if n > n2:
    print(f'O Numero {n} é maior que o {n2}')
elif n < numero2:
    print(f'O Numero {n2} é maior que o {n}') # Se n2 é maior que n
else:
    print('Os numeros são iguais')  # Caso sejam iguais

print("Fim do programa\n")

# =========================

# Nível 2: Condicional Encadeada (if/elif/else)

# 6. Classificação de Atleta: Receba a idade de um nadador e classifique-o: 5-7
# anos (Infantil A), 8-10 (Infantil B), 11-13 (Juvenil A), 14-17 (Juvenil B), acima de
# 18 (Adulto)

# =========================

# Recebe idade do usuário
idedeNadador = int(input('Digite sua idade: '))

# Classifica usando if e elif conforme faixa etária
if idedeNadador >= 5 and idedeNadador <= 7:
    print('Infantil A')
elif idedeNadador >= 8 and idedeNadador <= 10:
    print('Infantil B')
elif idedeNadador >= 11 and idedeNadador <= 13:
    print('Juvenil A')
elif idedeNadador >= 14 and idedeNadador <= 17:
    print('Juvenil B')
elif idedeNadador >= 18:
    print('Adulto')

print("Fim do programa ...")
# =========================

# 7. Calculadora de IMC: Peça peso e altura, calcule o IMC (peso/altura2). Exiba se
# está: Abaixo do peso (<18.5), Peso ideal (18.5-24.9) ou Sobrepeso (>=25).

# =========================

# Recebe peso e altura
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# Calcula o IMC do usuario
imc = peso / (altura*altura) 

# Classifica resultado do calculo corforme os parametros
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso ideal! Parabéns!!')
else:
    print('Acima do peso')

print("Fim do programa ...")
# =========================

# 8. Conversor de Temperatura: Peça uma temperatura e pergunte se o usuário
# quer converter de Celsius para Fahrenheit ou vice-versa. Use elif para
# processar a escolha.

# =========================

# Mostra opções ao usuário
print("Olá esse programa converte Celsius para Fahrenheit e vice-versa. o que vc deseja fazer?\n")

#Recebe escolha do usuario
escolha = int(input("Digite para calcular: 1. Celsius => Fahrenheit  2. Fahrenheit => Celsius: \n"))

if escolha == 1: # esse if vai receber a temperatura em celcius e converter para Fahrenheit conforme a formula
    celsius = float(input('Digite a temperatura em Celsius: \n')) 
    convertido = (celsius * 9/5) + 32  # Fórmula
    print(f'O grau {celsius} em Fahrenheit é {convertido}' + "º Fahrenheit\n") # ele vai printar os resultado e fechar o programa
    print("Fim do programa ...")

elif escolha == 2: # esse if vai receber a temperatura em Fahrenheit e converter para celcius conforme a formula
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: \n')) 
    convertido = (fahrenheit - 32) * 5/9  # Fórmula inversa
    print(f'O grau {fahrenheit} em Celsius é {convertido}' + "º Celsius\n") # ele vai printar os resultado e fechar o programa
    print("Fim do programa ...")

else:
    print("Resposta invalida, Fim do programa ...") # caso o usuario digite qualquer coisa a não ser 1 ou 2 Respostaerrada e fecha o programa


# =========================

# 9. Análise de Produto: Peça o preço de um produto e categorize-o: "Barato" (até
# R$ 50), "Médio" (entre R$ 50 e R$ 100) ou "Caro" (acima de R$ 100).

# =========================

# Recebe valor de um produto
produto = int(input("Digite o valor de um produto: "))

#Classifica preço conforme a resposta do usuario
if produto < 0:
    print(f'O produto tem um valor negativo')
elif produto <= 50:
    print(f'O valor do produto está Barato')
elif produto <= 100:
    print(f'O valor do produto está em um preço medio')
elif produto > 100:
    print(f'O valor do produto está Caro')

print("Fim do programa ...")
# =========================

# 10. Turno de Estudo: Pergunte em que turno o aluno estuda (M para Matutino, V
# para Vespertino, N para Noturno). Imprima "Bom Dia!", "Boa Tarde!" ou "Boa
# Noite!".

# =========================

# pede ao usuario para digitar o turna em que estuda e converte a resposta para minusculo, para que não de erro
turno = input("Digite o Turno da sua aula, Usando M. Manhâ, V. Tarde, N. Noite: ").lower()

# Verifica o turno e printa
if turno == 'm':
    print('Bom dia')
elif turno == 'v':
    print('Boa Tarde')
elif turno == 'n':
    print('Boa Noite')
else: 
    print("Resposta invalida!! Fim do programa ...")

print("Fim do programa ...")
# =========================

# Nível 3: Operadores Lógicos (and, or, not)

# 11. Acesso ao Sistema: Peça usuário e senha. Exiba "Acesso Permitido" apenas se
# o usuário for "admin" e a senha for "fatec123".

# =========================
# Recebe login e senha
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

# Verifica se ambos estão corretos
if login == 'admin' and senha == 'fatec123':
    print('Acesso Permitido. Bem vindo!!')
else:
    print('CAI FORA DAQUI!!!')

print("Fim do programa\n")


# ========================= 

# 12. Triângulo Válido: Receba três lados (A, B, C). Verifique se podem formar um
# triângulo: (A < B+C) e (B < A+C) e (C < A+B).

# =========================

# Recebe lados
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Verifica condição de existência de triângulo
if (a < b + c) and (b < a + c) and (c < a + b):
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")

print("Fim do programa\n")

# =========================

# 13. Votação Obrigatória: Peça a idade do usuário. Diga se o voto é: "Obrigatório"
# (entre 18 e 70 anos) ou "Facultativo/Não vota" (menor de 18 ou maior de 70).
# Use or.

# =========================

# Recebe idade
idade = int(input("Digite sua idade: "))

# Usa OR para verificar as 2 possibilidades
if idade < 18 or idade > 70:
    print("Facultativo/Não vota")
else:
    print("Obrigatório votar")

print("Fim do programa\n")


# =========================

# 14. Desconto de Farmácia: Um desconto é dado se o cliente tiver mais de 65 anos
# ou se o valor da compra for maior que R$ 100. Verifique se o cliente tem
# direito.

# =========================

# Recebe idade e valor
idade = int(input("Digite sua idade: "))
valor = float(input("Digite o valor da compra: "))

# Se qualquer condição for verdadeira, tem desconto
if idade > 65 or valor > 100:
    print("Tem direito ao desconto")
else:
    print("Não tem direito ao desconto")

print("Fim do programa\n")


# =========================

# 15. Ano Bissexto: Um ano é bissexto se for divisível por 4 e (não divisível por 100
# ou divisível por 400). Peça um ano e verifique.

# =========================

# Recebe ano
ano = int(input("Digite o Ano atual: "))

# Regra: divisível por 4 e (não por 100 ou sim por 400)
if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é bissexto")

print("Fim do programa\n")


# =========================

# Nível 4: Estruturas Aninhadas (if dentro de if)

# 16. Sistema de Empréstimo: Pergunte o valor do empréstimo e a renda mensal. Se
# a renda for maior que R$ 2000, pergunte em quantas parcelas. Se a parcela
# exceder 30% da renda, negue o empréstimo; caso contrário, aprove.

# =========================

# Recebe dados
valor = float(input("Digite o valor do empréstimo: "))
renda = float(input("Digite sua renda mensal: "))

# Primeiro verifica renda mínima
if renda > 2000:
    parcelas = int(input("Em quantas parcelas deseja pagar? "))
    valor_parcela = valor / parcelas

    # Verifica se parcela cabe no orçamento
    if valor_parcela > renda * 0.3:
        print("Empréstimo negado")
    else:
        print("Empréstimo aprovado")
else:
    print("Empréstimo negado. Renda não coincide")

print("Fim do programa\n")

# =========================

# 17. Login com Níveis: Peça o login. Se for "admin", peça a senha. Se a senha
# estiver correta, pergunte se quer "Reiniciar Sistema" ou "Desligar". Se o login
# não for "admin", diga "Acesso de Usuário Comum".

# =========================

# Recebe login
login = input("Digite o login: ")

# Verifica se é admin
if login == "admin":
    senha = input("Digite a senha: ")

    # Verifica senha
    if senha == "1234":
        opcao = input("Deseja 'Reiniciar Sistema' ou 'Desligar'? ")
        print(f"Opção escolhida: {opcao}")
    else:
        print("Senha incorreta")
else:
    print("Acesso de Usuário Comum")

print("Fim do programa\n")


# =========================

# 18. Clima e Vestimenta: Pergunte se está chovendo (S/N). Se sim, pergunte se está
# ventando forte (S/N). Se chover e ventar, diga "Use capa de chuva reforçada".
# Se apenas chover, "Use guarda-chuva". Se não chover, diga "Tenha um bom
# dia"

# =========================

# Pergunta se está chovendo
chuva = input("Está chovendo? (S/N): ").upper()

# Se estiver chovendo
if chuva == "S":
    vento = input("Está ventando forte? (S/N): ").upper()

    # Se também estiver ventando
    if vento == "S":
        print("Use capa de chuva reforçada")
    else:
        print("Use guarda-chuva")
else:
    print("Tenha um bom dia")

print("Fim do programa\n")



