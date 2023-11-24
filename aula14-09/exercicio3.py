from biblioteca import lista


def media_trab_entregue():
    conta = 0

    for pessoa in lista:
        conta += len(pessoa['notas'])

    result = conta / len(lista)

media_trab_entregue()
