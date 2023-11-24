from biblioteca import lista

#Exercicio 2 - Mostrar o número de trabalhos entregues por cada pessoa


def pega_notas(pessoa):
    notas = pessoa["notas"]
    if type(notas) == int : notas = [notas]

    return notas

def num_trab():
    for p in lista:
        num_trabs = len(pega_notas(p))
        print(p['nome'], " - ", num_trabs)


num_trab()