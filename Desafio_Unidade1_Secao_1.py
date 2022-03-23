'''
Considerando que você receberá duas estruturas, conforme foi mencionado, crie uma função que trate os dados e retorne uma lista com os e-mails que ainda não foram enviados.
'''
def extrair_lista_email(dados_1):
    lista_1 = list(zip(dados_1['nome'], dados_1['email'], dados_1['enviado']))

    emails = [item[1] for item in lista_1 if not item[2]]

    return print(emails)
    
dados_1 = {
    'nome':['Joao','Rafael','Alex','Fernanda'],
    'email':['joao@gmail.com','rafael@gmail.com','alex@gmail.com','fernanda@gmail.com'],
    'enviado':[False, True, True, False]
}

extrair_lista_email(dados_1)