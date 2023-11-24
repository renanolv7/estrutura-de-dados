

pessoa5 = {
   'nome': 'Carl',
   'idade': 28,
   'altura': 1.65,
   'trab-entregues': 3,
   'datas-entrega': ('14-02', '20-03','01-03'),
   'notas': (60, 40, 80),

}
pessoa6 = ('Carl', 28, 1.65, 3, ('14-02', '20-03','01-03'), (60, 40, 80))

nome = pessoa6[0]

print(f'Dicionário Carl: {pessoa5}')
print(f'Tupla Carl:', pessoa6)
print(nome)