import bcrypt


def criptografar_senha(senha):
    senha = senha.encode('utf-8')
    salt = bcrypt.gensalt(8)
    senha_cript = bcrypt.hashpw(senha, salt)
    senha_cript = senha_cript.decode('utf-8')
    return senha_cript


def validar_senha(senha_banco, senha_digitada):
    if senha_banco is None:
        return False
    senha_banco = str(senha_banco[0])
    senha_digitada = senha_digitada.encode('utf-8')
    senha = senha_banco.encode('utf-8')
    return bcrypt.hashpw(senha_digitada, senha) == senha


def armazenanar_temporariamente(email_celular, nome_cadastro, usuario, senha_cadastro):
    arquivo = open('dados.txt', 'w')
    arquivo.write(f'{email_celular} - {nome_cadastro} - {usuario} - {senha_cadastro} ')
    arquivo.close()


def ler_dados_temporariemente():
    with open("dados.txt", "r") as cadastro:
        lista = list()
        for lin in cadastro.readlines():
            dado = lin.split('-')
            for d in dado:
                lista.append(d.strip())
    return lista


def gerar_email(email):
    import smtplib
    import random
    codigo = random.randint(1000, 9999)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("remetente@gmail.com", "temjtturvlmznnct")
    server.sendmail(
        "remetente@gmail.com",
        f"{email}",
        f"{codigo}")
    server.quit()

    arquivo = open('codigo_temporario.txt', 'w')
    arquivo.write(f'{codigo}')
    arquivo.close()


def verificar_email(codigo):
    import os
    with open('codigo_temporario.txt', 'r') as codigo_txt:
        for lin in codigo_txt.readlines():
            cod_email = lin
    print(f'o codigo salvo é {cod_email}')
    os.remove('codigo_temporario.txt')
    if codigo == cod_email:
        return True
    else:
        return False


def limpar_lixo():
    import os
    if os.path.exists(f'dados.txt'):
        os.remove('dados.txt')
