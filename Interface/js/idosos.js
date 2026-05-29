const usuario_id = localStorage.getItem('usuario_id')


async function criarIdoso() {

    const nome = document.getElementById('nomeIdoso').value
    const idade = document.getElementById('idadeIdoso').value

    await fetch(`${API_URL}/idosos`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome,
            idade,
            usuario_id
        })
    })

    carregarIdosos()
}


async function carregarIdosos() {

    const resposta = await fetch(`${API_URL}/idosos`)

    const idosos = await resposta.json()

    const lista = document.getElementById('listaIdosos')

    lista.innerHTML = ''

    idosos.forEach(idoso => {

        const item = document.createElement('li')

        item.innerHTML = `
            <strong>${idoso.nome}</strong>
            - ${idoso.idade} anos
            <br>
            <a href="responsaveis.html">
                Ver Responsáveis
            </a>
        `

        lista.appendChild(item)

    })
}

carregarIdosos()