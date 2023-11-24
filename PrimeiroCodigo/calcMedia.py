pessoa5 = {
   'nome': 'Carl',
   'idade': 28,
   'altura': 1.65,
   'trab-entregues': 3,
   'datas-entrega': ('14-02', '20-03','01-03'),
   'notas': (60, 40, 80),

}

pessoa6 = ('Carl', 28, 1.65, 3,  ('14-02', '20-03','01-03'), (60, 40, 80))

notas = pessoa5['notas']
soma = 0

for nota in notas:
    soma += nota
media = (notas[0] + notas[1] + notas[2]) / len(notas)


# sum(var2[ : ]) / len(var2)

print(f'Media das notas de {pessoa6[0]} = {media}')
