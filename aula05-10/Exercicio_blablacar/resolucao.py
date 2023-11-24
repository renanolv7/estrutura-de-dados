from lib3 import assentos

def listar_vazio():
    for pessoa  in assentos:
        if pessoa['idade'] == 0:
            print(pessoa['poltrona'], '-- vazia' )
    

def listar():
    for pessoa  in assentos:
        if pessoa['idade'] == 0:
            print(pessoa['poltrona'], '-- vazia' )
        
        else:
            print(pessoa ['poltrona'], 'ocupador por:', pessoa['nome'])
   
def novo():
    encontrou = 0
    for poltrona  in assentos:
        if poltrona['idade'] == 0:
            encontrou = poltrona
            break
        
    if encontrou == 0:
        print('Procure outro carona, aqui é cheio')
    
    encontrou['nome'] = input('Novo passageiro:')
    encontrou['idade'] = input('Idade: ')
    
        

listar_vazio()         
novo()
listar_vazio
novo()
listar()
novo()
listar()
