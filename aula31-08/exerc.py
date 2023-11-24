from biblioteca import lista

def captura_infos():
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    notas = []
    for nota in range(3):
        
        notaDigi = int(input(f"Informe a {nota + 1} ° nota: "))
        notas.append(notaDigi)

    dici = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
    }

    
    return dici

def mostrar_lista(lista):

    for pessoa in lista:
        nome = pessoa["nome"]
        notas = pessoa["notas"]

        print()
        print("Nome:", nome)
        print("Notas:", notas)
        print()


def opcao():

    print(" - '0' MOSTRAR LISTA - ")
    print(" - '1' CAPTURAR NOVA PESSOA -")
    opcao = int(input("Informe uma opção acima: "))

    if opcao == 0:
        ret = mostrar_lista(lista)
        print(lista)

    elif opcao == 1:
        ret2 = captura_infos()
        lista.append(ret2)
        
        print("Pessoa adicionada!")


opcao()

        

