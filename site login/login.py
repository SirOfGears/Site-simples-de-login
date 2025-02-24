nomes = ['2', '3', '4', '5']
senhas = ['0000', '1234', '5575', '1144']


nome = input('Digite seu nome: ')

if nome == "1":
    print('Acesso liberado e direto sem senha')

else: 
    senha = (input('Digite sua senha de 4 dígitos: '))
    if senha in senhas:
        print('Acesso liberado')
    else: 
        print('Acesso negado')
    

