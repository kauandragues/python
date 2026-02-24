# jogo da palavra secreta
#autor: kauandragues

palavra_jogo = "perfume"
palavra_formatada = len(palavra_jogo)*"*"
letras_chutadas = ""
num_tentativas = 0

while True:
    letra_usuario = input("Digite uma letra:").lower()

    # se a letra não estiver no alfabeto
    if  not letra_usuario.isalpha() or len(letra_usuario) > 1:
        print("Digite uma letra do alfabeto")
        continue
    
    if letra_usuario in letras_chutadas:
        print("Você já digitou esse letra")
        continue
    
    letras_chutadas += letra_usuario # adiciona a letra em letras chutadas
    num_tentativas += 1 # add +1 no número de tentativas
    
    if palavra_jogo.count(letra_usuario) == 0:
        print("Palavra formatada:",palavra_formatada)
        continue
    
    palavra = "" # nova string mudar a palavra formatada
    for i in range(len(palavra_jogo)):
        if letra_usuario == palavra_jogo[i]: # mostra a letra que o jogador digitou
            palavra += letra_usuario
            continue
        
        if palavra_formatada[i] != "*": # mostra que o jogador já acertou até agora
            palavra += palavra_formatada[i]
            continue
        
        palavra += "*" # oculta as letras que ainda não foram acertadas
    
    palavra_formatada = palavra
        
    print("Palavra formatada:",palavra_formatada)
        
    # verificar se o jogo acabou
    if palavra_formatada == palavra_jogo:
        print("Parabéns! Você conseguiu!")
        print("O seu número de tentativas foi:", num_tentativas)
        break

    
    