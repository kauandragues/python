def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

saudacao1 = criar_saudacao('Bom dia', 'Kaua')
saudacao2 = criar_saudacao('Bom noite', 'Pedro')

print(saudacao1())
print(saudacao2())