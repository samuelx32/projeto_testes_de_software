*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    file:///C:/Users/samue/OneDrive/Ambiente%20de%20Trabalho/projeto_testes_de_software/Interface/index.html

*** Test Cases ***
Cadastrar Responsavel Valido

    Open Browser    ${URL}    chrome

    Sleep      2s

    Input Text     id=emailLogin    joao@email.com

    Click Button    Entrar 

    Sleep      2s

    Click Link     Ver Responsáveis

    Sleep      2s

    Input Text    id=nomeResponsavel    Maria Oliveira
    Input Text    id=telefoneResponsavel    999999999
    Input Text    id=idosoId            1

    Sleep     2s

    Click Button    Salvar

    Sleep     2s

    Page Should Contain
    ...    Cadastro realizado com sucesso

    Close Browser