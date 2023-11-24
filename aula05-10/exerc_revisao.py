
# Criar duas listas contendo, uma com nome de tres pessoas e outra lista com os sobrenomes


nome = ['Renan', 'Mariana', 'Well']
sobrenome = ['Oliveira', 'Cristina', 'Ramos']


# FOR usando ZIP para pegar informações simultâneas das duas listas acima
# Primeiro 

def pega_info(nome, sobrenome):

    
    for nome, sobrenome in zip(nome, sobrenome):

        print(f'Nome - {nome} {sobrenome}')
    

pega_info(nome, sobrenome)