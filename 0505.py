# Luiz Felipe Da Silva

# Nivel Basico: Sintaxe e Mapeamento.

# 1. Meu primeiro dicionario: Crie um dicionario chamado contato que armazene o nome, telefone e email de uma pessoa.
# Imprima apenas o email usando a chave correspondente.

# contatos = {}

# contatos["nome"] = input("Digite seu nome: ")
# contatos["telefone"] = int(input("Digite seu telefone: "))
# contatos["email"] = input("Digite seu email: ").lower()

# print(contatos["email"])

# 2. Cardápio Digital: Crie um dicionário precos onde as chaves são nomes de produtos (ex: "Salgado", "Suco", "Doce")
# e os valores são os preços. Altere o preço do "Suco" para um novo valor e adicione um novo item chamado "Café" ao dicionário.

# preço = {"Salgado": 10, "Suco": 5, "Doce": 7}

# preço["Suco"] = 7

# preço["Café"] = 12

# print(preço)

# 3. Conjunto de Cores: Crie uma lista chamada lista_cores com várias cores, repetindo algumas delas (ex: "azul", "verde", "azul", "vermelho").
# Converta essa lista para um Conjunto (set) e imprima o resultado. Explique, em um comentário, o que aconteceu com as cores repetidas.

# listaCores = ("azul", "verde", "azul", "vermelho")

# conjunto = set()

# conjunto.update(listaCores)

# print(conjunto)

# ("azul", "verde", "vermelho")

# Aconteceu o seguinte um conjunto/Set() não armazena elementos duplicados,
# então como já tinha a cor azul, ele ignorou o outro elemento azul 

# 4. Acesso Seguro: Utilize o dicionário de precos do exercício 2. Peça ao usuário para digitar o nome de um produto.
# Use o método .get() para exibir o preço, mostrando a mensagem "Produto não encontrado" caso a chave não exista.

# precos = {"salgado": 10, "suco": 5, "doce": 7}

# produto = input("Digite o nome do produto: ").lower()

# preco = precos.get(produto, "Produto não encontrado")


# print(f"O Preço do {produto} é: {preco}")

# Dicionário de Notas: Crie um programa que armazene o nome de 3 alunos e suas respectivas notas em um dicionário.
# Percorra o dicionário usando um laço for e imprima: "O aluno [Nome] tirou nota [Nota]".

alunos = {
    "felipe": 7,
    "joao": 8,
    "camila": 3
    
}

for chave, valor in alunos.items():
    print(f"O aluno {chave} tirou nota {valor}")
