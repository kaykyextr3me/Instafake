from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import bd
import func

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def homepag():
    if not session.get("name"):
        return redirect("/login")
    usuario_atual = session.get("name")
    usuario = bd.moldar_perfil(usuario_atual)
    feed = bd.moldar_feed()
    id_user = bd.selecionarid(usuario_atual)
    recomendados = bd.moldar_recomendados(id_user)
    return render_template('index.html', usuario=usuario, feed=feed, recomendados=recomendados)


@app.route('/cadastro')
def cadastropagge():
    return render_template('telacadastro.html')


@app.route('/cadastro_insta', methods=['POST'])
def cadastrar():
    email_celular_cadastro = request.form['email_celular_cadastro']
    nome_cadastro = request.form['nome_cadastro']
    usuario = request.form['usuario_cadastro']
    senha_cadastro = request.form['senha_cadastro']
    func.armazenanar_temporariamente(email_celular_cadastro, nome_cadastro, usuario, senha_cadastro)
    return redirect('/verificaremail')


@app.route('/verificaremail')
def verificaremail():
    celular_email = func.ler_dados_temporariemente(True)
    try:
        func.gerar_email(celular_email)
    except Exception as error:
        print(f'Problema encontrado foi {error.__class__}')
        func.limpar_lixo()
        return render_template('telacadastro.html', msg='email inválido')
    else:
        return render_template('/verificar_email.html', email=celular_email)


@app.route('/verificar_emailform', methods=['POST'])
def verificaremail_form():
    digito01 = request.form['digito01']
    digito02 = request.form['digito02']
    digito03 = request.form['digito03']
    digito04 = request.form['digito04']
    codigo = digito01 + digito02 + digito03 + digito04
    if func.verificar_email(codigo):
        celular_email = func.ler_dados_temporariemente(True)
        bd.cadastrar_usuario()
        session['name'] = None
        session["name"] = celular_email
        return redirect('/perfil')
    else:
        func.limpar_lixo()
        return redirect('/cadastro')


@app.route('/login')
def loginpage():
    return render_template('telalogin.html')


@app.route('/deslogar')
def deslogar():
    session["name"] = None
    return redirect('/login')


@app.route('/login_insta', methods=['POST', 'GET'])
def logar():
    celular_email = request.form['celular_email_login']
    senha = request.form['senha_login']
    try:
        credenciais = bd.autenticar_login(celular_email, senha)
    except ValueError:
        credenciais = bd.selecionar_usuario(celular_email, senha)
    if len(credenciais) != 0:
        session["name"] = celular_email
        return redirect("/perfil")
    return render_template("telalogin.html", msg='Usuario ou Senha Incorretos')


@app.route('/perfil')
def perfilpag():
    if not session.get("name"):
        return redirect("/login")
    func.limpar_lixo()
    usuario_atual = session.get("name")
    id_usuario = bd.selecionarid(usuario_atual)
    usuario = bd.moldar_perfil(usuario_atual)
    posts = bd.selecionar_posts(id_usuario)
    usuario['qtd_publicacoes'] = len(posts)
    return render_template('perfil_page.html', usuario=usuario, posts=posts)


@app.route('/editarperfil')
def editarperfilpage():
    if not session.get("name"):
        return redirect("/login")
    usuario_atual = session.get("name")
    usuario = bd.moldar_perfil(usuario_atual)
    return render_template('telaeditarperfil.html', usuario=usuario)


@app.route('/editar_perfilform', methods=['POST'])
def editarperfil():
    usuario_atual = session.get("name")
    nova_foto_perfil = request.files['foto_perfil']
    bd.alterar_foto_perfl(usuario_atual, nova_foto_perfil)
    nome_usuario = request.form['nome_usuario']
    if len(nome_usuario) > 0:
        bd.alterar_nome_usuario(usuario_atual, nome_usuario)
    biografia = request.form['biografia']
    if len(biografia) > 0:
        bd.alterar_biografia(usuario_atual, biografia)

    return redirect('/perfil')


@app.route('/editar_senhaform', methods=['POST'])
def editarsenha():
    usuario_atual = session.get("name")
    senha_atual = request.form['senha_atual']
    nova_senha = request.form['nova_senha']
    id_usuario = bd.selecionarid(usuario_atual)
    bd.alterar_senha(id_usuario, nova_senha)
    return redirect('/perfil')


@app.route('/criar_nova_publicao')
def janela_novapublicacao():
    if not session.get("name"):
        return redirect("/login")
    return render_template('janela_nova_pub.html')


@app.route('/novo_post', methods=['POST'])
def novapublicacao():
    usuario_atual = session.get("name")
    nova_publicacao = request.files['nova_publicacao']
    id_usuario = bd.selecionarid(usuario_atual)
    bd.realizar_nova_publicacao(usuario_atual, id_usuario, nova_publicacao)
    return render_template('janela_nova_pub.html', fechar='window.close()')


@app.route('/user', methods=['GET'])
def outrousuario_page():
    usuario_selecionado = request.args.get('user')
    id_usuario = bd.selecionarid(usuario_selecionado)
    usuario = bd.moldar_perfil(usuario_selecionado)
    posts = bd.selecionar_posts(id_usuario)
    return render_template('outrousuario.html', usuario=usuario, posts=posts)


app.run(debug=True)
