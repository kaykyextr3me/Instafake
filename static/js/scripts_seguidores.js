function mudarBotaoSeguir(){
    document.getElementById('botao_seguir').innerHTML = 'seguindo';
    var usuario_seguindo_email = usuario_email

    fetch('/seguir', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "usuario_seguindo_email": usuario_seguindo_email })
      })

    alert(usuario_seguindo_email)
}
