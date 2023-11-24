pessoa1 = {
    'nome': 'Anna',
    'idade': 22,
    'altura': 1.70,
    'trab-entregues': 1,
    'datas-entrega': '15-02',
    'notas': 80, 
}

pessoa2 = {
    'nome': 'Bob',
    'idade': 18,
    'altura': 1.80,
    'trab-entregues': 2,
    'datas-entrega': ('16-02', '30-02'),
    'notas': (70, 30),
}

pessoa3 = {
    'nome': 'Carl',
    'idade': 28,
    'altura': 1.65,
    'trab-entregues': 3,
    'datas-entrega': ('14-02', '20-02', '01-03'),
    'notas': (90, 70, 40),
}

pessoa4 = {
    'nome': 'Daniel',
    'idade': 28,
    'altura': 1.65,
    'trab-entregues': 3,
    'datas-entrega': ('14-02', '20-02'),
    'notas': (70, 100),
}


# Exercicio 2
# for pessoa in lista:

#     notas = pessoa["notas"]

#     if type(notas) == int:
#         notas = [notas]

#     soma = float(sum(notas))
#     tam = len(notas)
#     media = soma / tam

#     nome = pessoa["nome"]
#     print(f'Nome: {nome} nota = {media}')


# # Exercicio 3
# total = 0
# for pessoa in lista:
#     notas = pessoa["notas"]

#     if type(notas) == int:
#         notas = [notas]

#     soma = sum(notas)
#     total += soma

# quant = len(lista) * 3 
# resposta = total / quant       


# Mostrar quem teve maior média, considerando somente provas feitas;
lista = [pessoa1, pessoa2, pessoa3, pessoa4]

maiorMedia = 0
nome_maior = " "

for pessoa in lista:

    notas = pessoa["notas"]
    nome = pessoa["nome"]

    if type(notas) == int:notas = [notas]

    soma = sum(notas)
    tam = len(notas)

    media = soma / tam

    if media > maiorMedia:
        maiorMedia = media
        nome_maior += nome

print(f'Nome: {nome} tem média = {media}')






