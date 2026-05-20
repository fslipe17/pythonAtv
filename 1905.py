def exibir_saudacoes(nome):
    print("------------------------------------------------------")
    print(f"-- BEM VINDO {nome}, AO SISTEMA DE CALCULOS --")
    print("------------------------------------------------------")
    
def div_linhas():
    print("----------------------")


def print_end():
    print("FIM DO PROGRAMA")
    
def capturar_notas(num):
    n1 = float(input(f"Digite a nota {num}: "))
    
    div_linhas()
    
    return n1
    
def soma_notas(num, num1, num2, num3):
    soma = num + num1 + num2 + num3
    
    return soma
    
def media_calc(soma):
    media = soma / 4
    
    return media
    
##############

def calcular_dobro(num):
    dobro = num * 2
    
    return dobro
    
##############

def celsius_para_fahrenheit(celcius):
    # F = C * 1.8 + 32.
    fahr = celcius * 1.8 + 32
    
    return fahr

############

def eh_par(num):
    if num % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"
        
##############

def encontrar_maior(a, b):
    if a > b:
        return f"O Número {a} é maior que {b}."
    elif a == b:
        return f"Os Números são iguais."
    elif a < b:
        return f"O Número {b} é maior que {a}."
        
###############

def calcular_preco_viagem(km, custoKm):
    viagem_preco = km * custoKm 
    
    return viagem_preco

nome = input("Digite seu nome para começarmos: ").upper()
    
exibir_saudacoes(nome)

tipo = int(input("Escolha a função: 1. Calcular Média, 2. Calcular Dobro, 3. Celcius para Fahrenheit, 4. Par ou impar, 5. Numero maior, 6. Preço da Viagem: "))

if tipo == 1:
    nota1 = capturar_notas(1)
    nota2 = capturar_notas(2)
    nota3 = capturar_notas(3)
    nota4 = capturar_notas(4)
    
    soma_result = soma_notas(nota1, nota2, nota3, nota4)
    
    media_result = media_calc(soma_result)
    
    print(f"A Média do aluno foi {media_result}\n")
    
elif tipo == 2:
    num = int(input("Digite um numero: "))
    
    dobro = calcular_dobro(num)
    print(f"O numero {num} multiplicado por 2 é {dobro}.\n")
    
elif tipo == 3:
    celcius = float(input("Digite a temperatura em Celcius: \n"))
    
    fahr = celsius_para_fahrenheit(celcius)
    
    print(f"A Conversao de {celcius}° celcius. o Resultado é: {fahr} Fahrenheit \n")
    
elif tipo == 4:
    par_impar = int(input("Digite um numero: "))
    
    result = eh_par(par_impar)
    
    print(f"O valor {par_impar} é: {result}\n")
    
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
elif tipo == 5:
    maiorA = int(input("Digite um numero: "))
    maiorB = int(input("Digite outro numero: "))
    
    result = encontrar_maior(maiorA, maiorB)
    
    print(result)
    
elif tipo == 6:
    km = float(input("Digite a Distância em KM: "))
    precokm_user = float(input("Digite o valor por KM, Se não tsouber escreva 0: "))
    
    if precokm_user == 0:
        precokm_user = 0.50
        print(precokm_user)
        preco_viagem = calcular_preco_viagem(km, precokm_user)
        
        print(f"A sua viagem de {km}km, irá custar {preco_viagem}")
    else:
        preco_viagem = calcular_preco_viagem(km, precokm_user)
        
        print(f"A sua viagem de {km}km, irá custar {preco_viagem} Reais")
    
    
print_end()

