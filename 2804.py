# Luiz Felipe Da Silva

# Exercicios 28/04

# 1. Criação e Acesso: Crie uma lista com 5 nomes de cidades. Imprima
# apenas a primeira e a última cidade da lista

# cidades = ["Londrina", "Loanda", "Ibiporã", "Maringá", "Cambé"]

# print(cidades[0])

# print(cidades[-1])

###################

# 2. Alteração Manual: Dada a lista numeros = [10, 20, 30, 40, 50], altere o
# valor do terceiro elemento para 100 e imprima a lista atualizada.

# numeros = [10, 20, 30, 40, 50]

# numeros.remove(30)
# numeros.insert(2, 100)

# numeros [2] = 100

# print(numeros)

# 3. Uso da Tupla: Crie uma tupla com os meses do ano. Tente alterar o
# primeiro mês para "Janeiro Alterado" e observe o erro gerado pelo
# Python. Escreva em um comentário por que o erro ocorreu.

# meses = ("Janeiro", "Fevereiro", "Março")

# meses.remove(1)
# AttributeError: 'tuple' object has no attribute 'remove'
# Deu Erro de atributo, pois a lista tupla, não pode sem mudada, ou no caso remover a palavra

####################

# 4. Entrada Dinâmica: Crie um programa que peça ao usuário 5 números,
# adicione-os em uma lista usando .append() e, ao final, exiba a soma de
# todos os itens (use a função sum()).

# num = int(input("Digite um numero: "))
# num1 = int(input("Digite outro numero: "))
# num2 = int(input("Digite outro numero: "))
# num3 = int(input("Digite outro numero: "))
# num4 = int(input("Digite outro numero: "))

contador = 0

lista = []

# lista.append(num)
# lista.append(num1)
# lista.append(num2)
# lista.append(num3)
# lista.append(num4)

while contador < 5:
    num = int(input("Digite um numero: "))
    lista.append(num)
    
    contador = contador + 1

soma = sum(lista)

print(lista)

print(soma)

# 5. Ordenação de Nomes: Peça ao usuário nomes de convidados até que ele
# digite "fim". Guarde os nomes em uma lista, coloque-os em ordem
# alfabética e exiba a lista final.

# convidados = []

# while True:
#     nome = input("Digite o nome do convidado (ou 'sair'): ")
#     if nome.lower() == 'sair':
#         break

#     convidados.append(nome) # Organizando dados dinamicamente
    
# convidados.sort() # Organização alfabética

# print(f"\nLista de Presença ({len(convidados)} pessoas):")

# for pessoa in convidados:
#     print(f"- {pessoa}")

# 6. Fatiamento (Slicing): Crie uma lista de 1 a 10. Use o fatiamento para
# extrair e imprimir apenas os números do índice 2 ao 7.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# subNumeros = numeros[2:7]

# print(subNumeros)

# 7. Busca de Item: Crie uma lista de cores. Peça ao usuário para digitar uma
# cor e, usando o operador in, verifique se a cor está na lista. Informe o
# resultado.

# cores = ["vermelho", "azul", "verde", "amarelo", "preto"]

# corUsuario = input("Digite uma cor: ").lower()

# if corUsuario in cores:
#     print("A cor está na lista!")
# else:
#     print("A cor não está na lista.")

# 8. Remoção de Duplicatas: Dada uma lista com números repetidos, crie
# uma nova lista que contenha apenas os números únicos da lista original
# (dica: percorra a lista original com um for).

# listaDuplicatas = [1, 1, 2, 2, 3, 3, 4, 5, 6]

# listaUnica = []

# for i in listaDuplicatas:
#     if i not in listaUnica:
#         listaUnica.append(i)

# print("Lista original:", listaDuplicatas)
# print("Lista sem duplicatas:", listaUnica)

# 9. Filtro de Dados: Peça 10 notas de alunos e armazene em uma lista.
# Calcule a média e, em seguida, exiba apenas as notas que ficaram abaixo
# da média da turma.

# notas = []

# contador = 0

# while contador < 10:
#     nota = float(input("Digite uma nota: "))
    
#     notas.append(nota)
#     contador = contador + 1
    
#     print(notas)


# print(notas)

# soma = sum(notas) # Função nativa que soma a lista toda

# media = soma / len(notas)

# print(f"Média da turma: {media:.1f}")
# print("Notas acima da média:")

# for n in notas:
#     if n > media:
#         print(f"{n}")

# 10. Matriz Simples (Desafio): Crie uma lista chamada estoque que contenha
# 3 sublistas. Cada sublista deve ter [nome_produto, quantidade]. Percorra
# essa lista e imprima o nome de cada produto e o total de itens no
# estoque somando todas as quantidades.

# estoque = [
#           ["Maça", 50], # Nome, Qtd
#           ["banana", 100],
#           ["acabaxi", 20]
#           ]
          
# for i in estoque:
#     print(f"Estoque tem: {i[0:2]}")

# Fim do Programa

###############
