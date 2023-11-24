from Exercicio_blablacar.lib3 import lista_pessoas

# Fazer um sistema de blablacar para alocar pessoas dentro do carro


lugares_ocupados = [1, 2, 3, 4]

def comprar_passag():
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    poltrona = ("Informe seu acento: ")


    for pessoa in lista_pessoas:

        poltrona = pessoa['poltrona']
        print(poltrona)

        if poltrona == lista_pessoas[0]['poltrona'] or lista_pessoas[1]['poltrona'] :
            print("JÁ OCUPADO!")

        else:
            print("LUGARES NÃO OCUPADOS: {}")

            
            

        # if poltrona == lista_pessoas['poltrona']:
        #     print("LUGAR JÁ OCUPADO!")
        # else:
            

            
        



comprar_passag()