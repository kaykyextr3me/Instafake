# Instafake
## → Resumo
Projeto de uma cópia do Instagram. Ele conta com a maioria das funções do Instagram real. Desde criação de conta, até realizar publicações. O instafake é constituído de sistema conectado a um banco de dados, onde ficam salvos os dados de cadastro de usuários da rede social, e todas suas postagens. Outro diferencial é que as senhas são gravadas criptografadas criando um nível de proteção maior.

## → Tecnologias
→ Python <br>
→ Flask <br>
→ Flask Session <br>
→ Mysql <br>
→ HTML5, CSS3 <br>
→ bcrypt <br>
→ smtplib <br>

## → Descrição detalhada

## ► Banco de dados
O Instafake possui um banco de dados desenvolvido no MySQL Workbench. <br>
O db_instafake possui as tabelas usuario_dadospessoais e publicacoes que possuem uma relação (1,n) <br>

### → Modelo Físico: <br>
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/d14ee0adedb9021bf10f722fc7dd4ff78fe771b2/files_readme/banco%20de%20dados.png" width="500x">
</div>
<br>

## ► Cadastrar Usuários
Para realizar o cadastro no Instafake foi desenvolvido um sistema com código de verificação com a biblioteca smtplib. Ao realizar o cadastro é gerado um número aletório que é enviado para o email cadastrado que deve ser inserido na tela de verificação de código para que seja possível efetuar o cadastro.

### → Tela de Cadastro
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/d14ee0adedb9021bf10f722fc7dd4ff78fe771b2/files_readme/tela_cadastro_.png" width="500x">
</div> <br>

### → Tela de Verificação de Email
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/d14ee0adedb9021bf10f722fc7dd4ff78fe771b2/files_readme/tela_ver_email.png" width="500x">
</div>

<br> As senhas dos usuários são criptografadas e depois salvas no banco de dados com o auxílio da biblioteca bcrypt.


## ► Autenticação de Usuários
Os usuários previamente cadastrados podem se conectar ao Instafake a partir de um celular ou email (de sua escolha no momento do cadastro) e da senha salvas no banco. O programa verifica a existência do usuário no banco de dados e valida a entrada, caso a senha tenha sido inserida corretamente. As senhas são comparadas criptografadas, aumentando a segurança do Instafake.

### → Tela de Login
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/75c917f53bfd22ea4c9bd0f4ebc89d920753e9b0/files_readme/tela_login.png" width="500x">
</div>

## ► Perfils dos Usuários do Instafake
Após realizado o cadastro ou o login, o usuário é redirecionado para a sua página de perfil onde ele terá acesso a uma série de funções. A pagina do perfil contêm uma dois botões principais. Um para criar publicações, que abrirá uma janela pop up onde será realizada a inserção de novas fotos ou gifs no perfil e na página do feed e um botão Editar perfil que redireciona o usuário para uma nova página para realizar certas alterações no seu perfil.

### → Tela de Perfil de Usuário
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/dbd40be5b70d332326a313571ae913cf479c5f7c/files_readme/tela_perfil_usuario.png" width="500x">
</div>

### → PopUp Realizar Nova Publicação
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/05381de62504891fd7a34d200a827ca4213c4d39/files_readme/pop_up_novopost.png" width="500x">
</div>

## ► Atualização de Dados de Usuário
Ao ser redirecionado para a tela de edição de perfil, o usuário tem acesso a novas funcionalidaes. Por aqui ele pode alterar sua foto de perfil, seu nome de usuário e até inserir uma biografia. Além disso o usuário pode alterar a sua senha. De forma bem parecida ao que existe no Instagram real.

### → Tela de Edição de Perfil
<div align="center">
  <img src="https://github.com/kaykyextr3me/Instafake/blob/98741d66c2e90711c5e4fcc65b2205baa88e8d8b/files_readme/tela_editar_perfil.png" width="500x">
</div>




