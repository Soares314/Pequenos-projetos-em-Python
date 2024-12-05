import re

def verificar_nome(nome):
    regex = re.compile(r'[a-zA-Z]{1,49}\s[a-zA-Z ]{1,49}' )

    if regex.fullmatch(nome):
        return True
    else:
        print("Nome inválido, tente novamente!")
        return False

def verificar_cpf(cpf):
    regex = re.compile(r'(\d{3}.\d{3}.\d{3}-\d{2})|\d{11}' )

    if regex.fullmatch(cpf):
        return True
    else:
        print("CPF inválido, tente novamente!")
        return False

def verificar_email(email):
    regex = re.compile(r'[a-zA-Z._]*[a-zA-Z][a-zA-Z._]*[a-zA-Z][a-zA-Z._]*@[a-zA-Z._]*[a-zA-Z][a-zA-Z._]*[a-zA-Z][a-zA-Z._]*.[a-z]{3}')

    if regex.fullmatch(email):
        return True
    else:
        print("Email inválido, tente novamente!")
        return False


def verificar_telefone(telefone):
    regex = re.compile(r'\(\d{2}\)\d{5}-\d{4}|\d{11}')


    if regex.fullmatch(telefone):
        return True
    else:
        print("Telefone inválido, tente novamente!")
        return False

def interface():
    while(1):
        input_nome = input("Nome:")
        if(verificar_nome(input_nome)):
            break
    while(1):
        input_cpf = input("CPF:")
        if(verificar_cpf(input_cpf)):
            break
    while(1):
        input_email = input("E-mail:")
        if(verificar_email(input_email)):
            break
    while(1):
        input_telefone = input("Telefone:")
        if(verificar_telefone(input_telefone)):
            break

    print("Cadastro realizado com sucesso")
    return True

interface()