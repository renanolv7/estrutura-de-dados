
# DICIONÁRIOS

diciBob = {
    'nome': 'Bob',
    'idade': 18,
    'altura': 1.80,
    'trab-entregues': 2,
    'datas-entrega': ('16-02', '30-02'),
    'notas': (90, 60),
}


diciCarl = {
    'nome': 'Carl',
    'idade': 28,
    'altura': 1.65,
    'trab-entregues': 3,
    'datas-entrega': ('14-02', '20-02', '01-03'),
    'notas': (60, 40, 80),
}


# Pegando as informações e printando
# Informações dos alunos
diciAnna = {
    'nome': 'Anna',
    'idade': 22,
    'altura': 1.70,
    'trab-entregues': 1,
    'datas-entrega': '15-02',
    'notas': (80, )
}

#Anna
notas = diciAnna["notas"]
mediaAnna =  sum(notas) / len(notas)

#Verifica se a qtde de notas presentes na tupla for menor que 2, ele só vai imprimir a minha nota
qtde = len(notas)

if(qtde < 2):
    print("Anna, media: ", mediaAnna)
else:
    pass

#Bob
notas = diciBob["notas"]
mediaBob = sum(notas) / len(notas)

print("Bob, Media: ", mediaBob)

#Carl
notasCarl = diciCarl["notas"]
mediaCarl =  sum(notasCarl) / len(notasCarl)

print("Carl, media: ", mediaCarl)


# TUPLAS
tuplaAnna = ('Anna', 22, 1.70, 1, '15-02', 80)
tuplaBob = ('Bob', 18, 1.80, 2, ('16-02', '30-02'), (90, 60))
tuplaCarl = ( 'Carl', 28, 1.65, 3, ('14-02', '20-02', '01-03'), (60, 40, 80))

