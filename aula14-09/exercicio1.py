from biblioteca import lista


# Exercicio 1 - Fazer funções para capturar e mostrar informações

def captura_info():
    nomePessoa = input("Informe seu nome: ")
    idadePessoa = int(input("Informe sua idade: "))

    newPessoa = {
        "nome" : nomePessoa,
        "idade" : idadePessoa,
    }   

    return newPessoa

    


def mostrar_valores(lista):

    for pessoa in lista:

        nome = pessoa['nome']
        idade = pessoa['idade']

        print(f"Nome - {nome} com idade de: {idade} anos")
        print()
        


# p4 = captura_info()
# lista.append(p4)

# apresentar = mostrar_valores(lista)
# print(apresentar)


