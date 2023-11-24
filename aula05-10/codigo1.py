from lib2 import lista_pessoas

# Capturar uma lista de informações 
# Arranjar um jeito de incorporar mais elementos nessa lista
# Comando que adiciona novas coisas dentro da lista


def listar_notas():
    print("Listando notas...")

    for p in lista_pessoas:
        print(p)
    print('-'*80)



def inserir_element(nome, idade, notas):

    novo_dict = {
        'nome' : nome,
        'idade' : idade,
        'notas' : notas
    }

    lista_pessoas.append(novo_dict)



def captura_infos():

    nome = input("Informe um nome: ")
    idade = int(input("Informe a sua idade: "))
    notas = []

    for i in range(3):
        tmp = int(input(f'Informe a {i + 1} ° nota:  '))
        notas.append(tmp)
    print('-'*80)

    return nome, idade, notas


def teste():

    nome, idade, notas = captura_infos()
    inserir_element(nome, idade, notas)
    listar_notas()


teste()