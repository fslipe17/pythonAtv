# Luiz Felipe Da Silva

# EXERCICIOS DE FIXAÇÃO
# • Nível 1: Aquecimento (Operadores Básicos)
# • Foco: Entrada, Saída e Aritmética Simples.

# 1. Soma de Inteiros: Peça ao usuário dois números inteiros e exiba a soma
# deles.

# num1 = int(input("Digite um numero inteiro: "))
# num2 = int(input("Digite outro numero inteiro: "))

# soma = num1 + num2

# print(f"\nA soma dos numeros é: {soma}")

#######

# 2. Calculadora de Idade: Pergunte o ano atual e o ano de nascimento do
# usuário. Calcule e exiba a idade aproximada.

# nascimento = int(input("Digite a ano do seu nascimento: "))
# ano = int(input("Digite o ano atual: "))

# idade = ano - nascimento 

# print(f"\nA sua idade é: {idade}")

# 3. Conversor de Moeda: Crie um programa que receba um valor em Reais
# (float) e a cotação do Dólar do dia. Exiba o valor convertido em Dólares.

# valor = float(input("Digite um valor em Reais: "))

# quantidade = float(input("Digite quantos dólares você quer converter: "))
# cotacao = float(input("Digite a cotação do dólar: "))

# conversao = quantidade * cotacao

# print("Valor convertido:", conversao)

# • Nível 2: Intermediário (Precedência e Tipos de Divisão)
# • Foco: Uso de parênteses e operadores / e %.

# 4. Média Aritmética: Receba três notas de um aluno e calcule a média.
# (Atenção ao uso dos parênteses!).

# nota1 = int(input("Digite sua nota: "))
# nota2 = int(input("Digite sua nota: "))
# nota3 = int(input("Digite sua nota: "))

# media = nota1 + nota2 + nota3 
# media = media / 3

# print(media)

# 5. Divisão de Conta: Receba o valor total de uma conta de restaurante e a
# quantidade de pessoas na mesa. Exiba quanto cada um deve pagar
# (divisão real).

# conta = float(input("Digite o valor da mesa: "))
# quantPessoas = int(input("Digite quantas pessoas tem na mesa: "))

# total = conta / quantPessoas

# print(total)

# 6. Distribuição de Doces: Uma professora tem X balas para dividir
# igualmente entre Y alunos. Quantas balas inteiras cada aluno recebe e
# quantas sobram com a professora? (Use // e %).

# bolas = int(input("Digite quantas bolas a professora tem: "))
# alunos = int(input("Digite quantos alunos tem: "))

# divisao = int(bolas / alunos)
# resto = alunos % bolas

# print(f"Cada aluno recebe {divisao}, e restaram {resto}")

# • Nível 3: Avançado (Biblioteca math e Fórmulas)
# • Foco: Importação de módulos e funções especializadas.

# 7. Cálculo de Potência: Peça uma base e um expoente ao usuário e calcule o
# resultado usando math.pow().

# import math

# base = float(input("Digite uma base: "))
# expoente = float(input("Digite um expoente: "))

# potencia = math.pow(base, expoente)

# print(potencia)

# 8. Raiz Quadrada de Pitágoras: Peça os valores dos dois catetos de um triângulo
# retângulo. Calcule a hipotenusa usando math.sqrt().

# import math

# cat1 = float(input("Digite o cateto 1: "))
# cat2 = float(input("Digite o cateto 2: "))

# hipotenusa = math.sqrt(cat1*2 + cat2*2) *2

# print("Hipotenusa:", hipotenusa)


# 9. Área e Perímetro: Peça o raio de um círculo. Exiba a área e o perímetro
# utilizando a constante math.pi.

# import math

# raio = float(input("Digite o raio de um circulo: "))

# area = math.pi * raio**2
# perimetro = 2 * math.pi * raio

# print(f"Área: {area:.2f}")
# print(f"Perímetro: {perimetro:.2f}")

# 10. O Teto da Obra: Um galão de tinta pinta 15 metros quadrados. Peça ao usuário
# a área que ele deseja pintar e diga quantos galões ele precisa comprar. (Dica:
# Use math.ceil(), pois não se vende meio galão).

# import math

# area = float(input("Digite a área a ser pintada em m²: "))

# galoes = area / 15
# galoes_necessarios = math.ceil(galoes)

# print(f"Você precisará de {galoes_necessarios} galões de tinta.")

# • Nível 4: Desafio de Pensamento Computacional
# • Foco: Decomposição de problemas.

# 11. Decomposição de Tempo: Peça ao usuário um valor em segundos.
# Converta e exiba quantos minutos e quantos segundos esse valor
# representa (Ex: 130 segundos = 2 minutos e 10 segundos).

# segundos = int(input("Digite um valor em segundos: "))

# minutos = segundos // 60
# resto_segundos = segundos % 60

# print(f"{segundos} segundos = {minutos} minuto(s) e {resto_segundos} segundo(s)")

# 12. Cálculo de Distância: Receba as coordenadas (x1, y1) e (x2, y2) de dois
# pontos no plano cartesiano e calcule a distância entre eles usando a
# fórmula: d =

# import math

# x1 = float(input("Digite x1: "))
# y1 = float(input("Digite y1: "))
# x2 = float(input("Digite x2: "))
# y2 = float(input("Digite y2: "))

# distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# print(f"Distância entre os pontos: {distancia:.2f}")
