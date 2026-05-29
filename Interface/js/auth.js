async function cadastrarUsuario() {

    const nome = document.getElementById('nomeCadastro').value
    const email = document.getElementById('emailCadastro').value

    const resposta = await fetch(`${API_URL}/usuarios`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome,
            email
        })
    })

    const dados = await resposta.json()

    alert(`Usuário criado: ${dados.nome}`)
}


async function login() {

    const email = document.getElementById('emailLogin').value

    const resposta = await fetch(`${API_URL}/usuarios`)

    const usuarios = await resposta.json()

    const usuario = usuarios.find(
        u => u.email === email
    )

    if (!usuario) {
        alert('Usuário não encontrado')
        return
    }

    localStorage.setItem(
        'usuario_id',
        usuario.id
    )

    window.location.href = 'idosos.html'
}