import random

def jogar():
    imprime_mens()
    palavra_secreta = carrrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while(not acertou and not enforcou):
        chute = pede_chute()
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        acertou = '_' not in letras_acertadas
        enforcou = erros == 6

        print(letras_acertadas)

    if(acertou):
        imprime_m_venc()
    else:
        imprime_m_perd(palavra_secreta)
    

def imprime_mens():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

def carrrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def pede_chute():
    chute = input('Digite uma letra: ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertada, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertada[posicao] = letra
        posicao += 1

def imprime_m_venc():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_m_perd(palavra_secreta):
    print('Você foi enforcado!')
    print('A palavra era {}'.format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")
