# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual o nome do criador do Linux?',
        'Opções': ['Pedro Sampaio', 'Luis Assis', 'Linus Torvalds'],
        'Resposta': 'Linus Torvalds',
    },
    {
        'Pergunta': 'Qual linguagem roda principalmente no navegador?',
        'Opções': ['Java', 'JavaScript', 'C'],
        'Resposta': 'JavaScript',
    },
    {
        'Pergunta': 'Qual sistema de controle de versão é mais utilizado?',
        'Opções': ['Git', 'SVN', 'Mercurial'],
        'Resposta': 'Git',
    },
    {
        'Pergunta': 'Qual empresa criou o sistema operacional Windows?',
        'Opções': ['Apple', 'Microsoft', 'Google'],
        'Resposta': 'Microsoft',
    },
    {
        'Pergunta': 'Qual banco de dados é do tipo relacional?',
        'Opções': ['MongoDB', 'MySQL', 'Redis'],
        'Resposta': 'MySQL',
    },
    {
        'Pergunta': 'Qual protocolo é usado para transferir páginas web?',
        'Opções': ['FTP', 'HTTP', 'SMTP'],
        'Resposta': 'HTTP',
    },
    {
        'Pergunta': 'Qual estrutura de dados segue o princípio LIFO?',
        'Opções': ['Fila', 'Lista', 'Pilha'],
        'Resposta': 'Pilha',
    },
    {
        'Pergunta': 'Qual estrutura de dados segue o princípio FIFO?',
        'Opções': ['Fila', 'Pilha', 'Árvore'],
        'Resposta': 'Fila',
    },
]

quantidade_de_acertos = 0
quantidade_de_perguntas = len(perguntas)

for questao in perguntas:
    print(f'\nPergunta: {questao['Pergunta']}')  
    
    print('Opções:')
    for i, opcao in enumerate(questao['Opções']):
        print(f'{i+1}) {opcao}')

    resposta_usuario = int(input('Escolha uma opção: ')) - 1
    if questao['Opções'][resposta_usuario] == questao['Resposta']:
        print('Acertou ✅')
        quantidade_de_acertos = quantidade_de_acertos + 1
        continue
    
    print('Errou!❌')

print(f'\nVocê acertou {quantidade_de_acertos} de {quantidade_de_perguntas}')
