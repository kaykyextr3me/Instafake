import mysql.connector as mc
import func


def conecta_banco():
    conexao = mc.connect(host='localhost',
                         user='root',
                         password='admin',
                         database='db_instafake')
    return conexao


def cadastrar_usuario():
    celular_email, nome_completo, nome_usuario, senha = func.ler_dados_temporariemente()
    senha = func.criptografar_senha(senha)
    if celular_email.isnumeric():
        sql_insert = 'insert into usuario_dadospessoais(celular, nome_completo, nome_usuario, senha, ' \
                     'foto_perfil, biografia) values (%s, %s, %s, %s, %s, %s)'
    else:
        sql_insert = 'insert into usuario_dadospessoais(email, nome_completo, nome_usuario, senha, ' \
                     'foto_perfil, biografia) values (%s, %s, %s, %s, %s, %s)'

    biografia = 'Usuário do Instagram'
    foto_perfil = 'static/dadosuser/foto-instagram.jpg'
    valores = (celular_email, nome_completo, nome_usuario, senha, foto_perfil, biografia)
    conexao = conecta_banco()
    manipulador = conexao.cursor()
    manipulador.execute(sql_insert, valores)
    conexao.commit()


def selecionar_usuario(celular_email, senha):
    if celular_email.isnumeric():
        sql_select = 'select * from  usuario_dadospessoais where celular = %s and senha = %s'
    else:
        sql_select = 'select * from  usuario_dadospessoais where email = %s and senha = %s'
    valores = (celular_email, senha)
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(sql_select, valores)
    return maipulador.fetchall()


def autenticar_login(celular_email, senha):
    if celular_email.isnumeric():
        sql_select = f'select senha from  usuario_dadospessoais where celular = {celular_email}'
    else:
        print('email')
        sql_select = f'select senha from  usuario_dadospessoais where email = "{celular_email}"'

    print(celular_email)
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(sql_select,)
    dados = maipulador.fetchone()
    if func.validar_senha(dados, senha):
        return 'senha correta'
    else:
        return ''


def moldar_perfil(user_atual):
    if user_atual.isnumeric():
        select_dados = 'select nome_completo, nome_usuario, foto_perfil, biografia ' \
                       'from usuario_dadospessoais where celular = %s'
    else:
        select_dados = 'select nome_completo, nome_usuario, foto_perfil, biografia ' \
                       'from usuario_dadospessoais where email = %s'

    valor = (user_atual,)
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(select_dados, valor)

    dados_perfil = dict()
    for dado in maipulador.fetchall():
        dados_perfil.update({'nome': dado[0],
                             'usuario': dado[1],
                             'foto_perfil': dado[2],
                             'biografia': dado[3],
                             'qtd_publicacoes': 0
                             })
    return dados_perfil


def alterar_foto_perfl(usuario, foto):
    from pathlib import Path
    import shutil
    import os
    foto.save(f'static/lixo/{usuario}_{foto.filename}')
    tamanho = Path(f'static/lixo/{usuario}_{foto.filename}').stat().st_size
    print(tamanho)
    if tamanho > 0:
        src = 'static/lixo'
        trg = 'static/dadosuser'
        files = os.listdir(src)
        for fname in files:
            if os.path.exists(f'static/dadosuser/{usuario}_{foto.filename}'):
                os.remove(f'static/dadosuser/{usuario}_{foto.filename}')
            shutil.move(os.path.join(src, fname), trg)
        if usuario.isnumeric():
            sql_update = f'update usuario_dadospessoais set foto_perfil = "static/dadosuser/{usuario}_{foto.filename}" \
         where celular = "{usuario}"'
        else:
            sql_update = f'update usuario_dadospessoais set foto_perfil = "static/dadosuser/{usuario}_{foto.filename}" \
         where email = "{usuario}"'
        conexao = conecta_banco()
        manipulador = conexao.cursor()
        manipulador.execute(sql_update)
        conexao.commit()
    else:
        os.remove(f'static/lixo/{usuario}_{foto.filename}')


def alterar_nome_usuario(usuario, nome):
    if usuario.isnumeric():
        sql_update = f'update usuario_dadospessoais set nome_usuario = "{nome}" where celular = "{usuario}"'
    else:
        sql_update = f'update usuario_dadospessoais set nome_usuario = "{nome}" where email = "{usuario}"'
    conexao = conecta_banco()
    manipulador = conexao.cursor()
    manipulador.execute(sql_update)
    conexao.commit()


def alterar_biografia(usuario, biografia):
    if usuario.isnumeric():
        sql_update = f'update usuario_dadospessoais set biografia = "{biografia}" where celular = "{usuario}"'
    else:
        sql_update = f'update usuario_dadospessoais set biografia = "{biografia}" where email = "{usuario}"'
    conexao = conecta_banco()
    manipulador = conexao.cursor()
    manipulador.execute(sql_update)
    conexao.commit()


def alterar_senha(id_usuario, nova_senha):
    nova_senha = func.criptografar_senha(nova_senha)
    sql_update = f'update usuario_dadospessoais set senha = "{nova_senha}" where id = "{id_usuario}"'
    conexao = conecta_banco()
    manipulador = conexao.cursor()
    manipulador.execute(sql_update)
    conexao.commit()


def selecionarid(celular_email):
    if celular_email.isnumeric():
        sql_select = 'select id from  usuario_dadospessoais where celular = %s'
    else:
        sql_select = 'select id from  usuario_dadospessoais where email = %s'
    valores = (celular_email,)
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(sql_select, valores)
    id_usuario = maipulador.fetchone()
    return id_usuario[0]


def realizar_nova_publicacao(usuario_atual, id_usuario, post):
    import os
    from datetime import datetime
    sql_insert = 'insert into publicacoes(name_post, data_post, fk_usuario_dadospessoais_id) ' \
                 'values (%s, %s, %s)'
    data = str(datetime.now())
    existe = os.path.isdir(f'./static/dadosuser/POSTS_{id_usuario}')
    if existe is False:
        os.makedirs(f'./static/dadosuser/POSTS_{id_usuario}')
    post.save(f'static/dadosuser/POSTS_{id_usuario}/POST_{usuario_atual}_{data[-7]}{post.filename}')
    caminho = f'static/dadosuser/POSTS_{id_usuario}/POST_{usuario_atual}_{data[-7]}{post.filename}'
    valores = (caminho, data[:-7], id_usuario)
    conexao = conecta_banco()
    manipulador = conexao.cursor()
    manipulador.execute(sql_insert, valores)
    conexao.commit()


def selecionar_posts(id_usuario):
    sql_select = f'select name_post from publicacoes where fk_usuario_dadospessoais_id = {id_usuario} order by id desc'
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(sql_select)
    return maipulador.fetchall()


def moldar_feed():
    sql_select = 'select publicacoes.id, name_post, fk_usuario_dadospessoais_id, data_post, nome_usuario,' \
                 ' foto_perfil from publicacoes, usuario_dadospessoais where' \
                 ' publicacoes.fk_usuario_dadospessoais_id=usuario_dadospessoais.id order by id desc'
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(sql_select)

    dados = list()
    for dado in maipulador.fetchall():
        dados_feed = dict()
        dados_feed.update({'id': dado[0],
                           'name_post': dado[1],
                           'id_usuario': dado[2],
                           'data_post': dado[3],
                           'nome_usuario': dado[4],
                           'foto_perfil': dado[5]
                           })
        dados.append(dados_feed)
    return dados


def moldar_recomendados(id_usuario_atual):
    sql_select = f'select id, nome_usuario, foto_perfil, email from usuario_dadospessoais' \
                 f' where id != {id_usuario_atual} ORDER BY RAND() LIMIT 5'
    conexao = conecta_banco()
    maipulador = conexao.cursor()
    maipulador.execute(sql_select)
    dados = list()
    for dado in maipulador.fetchall():
        dados_feed = dict()
        dados_feed.update({'id_usuario': dado[0],
                           'nome_usuario': dado[1],
                           'foto_perfil': dado[2],
                           'email': dado[3]
                           })
        dados.append(dados_feed)
    return dados
