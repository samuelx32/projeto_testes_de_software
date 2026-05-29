async function criarResponsavel() {

    const nome = document.getElementById('nomeResponsavel').value

    const telefone = document.getElementById('telefoneResponsavel').value

    const idoso_id = document.getElementById('idosoId').value

    await fetch(`${API_URL}/responsaveis`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome,
            telefone,
            idoso_id
        })
    })

    carregarResponsaveis()
}


async function carregarResponsaveis() {

    const resposta = await fetch(`${API_URL}/responsaveis`)

    const responsaveis = await resposta.json()

    const lista = document.getElementById('listaResponsaveis')

    lista.innerHTML = ''

    responsaveis.forEach(responsavel => {

        const item = document.createElement('li')

        item.innerHTML = `
            <strong>${responsavel.nome}</strong>
            <br>
            ${responsavel.telefone}
            <br>
            Idoso ID: ${responsavel.idoso_id}
        `

        lista.appendChild(item)

    })
}

carregarResponsaveis()