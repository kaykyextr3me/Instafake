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

As senhas dos usuários são criptografadas e depois salvas no banco de dados com o auxílio da biblioteca bcrypt.





