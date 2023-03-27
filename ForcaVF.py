'''
Jogo da forca
1- O jogo vai ter sete tentativas                                                                                    OK
2 - O programa vai puxar arquivos txt de dentro da pasta                                                             OK
3 - temos que usar listas                                                                                            OK
4 -  Colocar mensagens quando jogador errar e acertar                                                                ok
5 - Colocar imagens (por texto para representar a forca)                                                             ok
6 - Fragmentar jogo em partes usando as funções (Deixando o código de fácil compreensão)                             OK
7 - Usar padão ANSI para colocar cores                                                                               OK
8 - Colocar intervalos entre jogadas para deixar o jogo mais orgânico                                                OK
9 - colocar pergunta para jogador se o mesmo quer tentar um chute da palavra inteira, caso erre ganha mais um erro   OK
10 - Melhorar texto inicial                                                                                          OK
11 - Fazer o jogador escolher a temática que ele quer seguir (para o jogo da forca)                                  OK
12 - verificar palavras com acento (se tem como colocar nas listas sem gerar bug)                                   verificando

'''

import jogos

def Jogo_forca():
    #_*_ coding: utf-8 _*_
    from time import sleep
    from random import randrange
    status = False #enforcado = acertar = False

    palavras = verificador = tema = 0 # acertos = erros = 0
    chutePal = '0'
    # verificador = 0

    def mensagem_inicial():
        print('~'*68)
        print('{: ^77}'.format('\033[1;032mJogo da Forca\033[m'))
        print('~'*68)
        sleep(1)
        print('{: ^75}'.format('~~~\033[1;032mRegras\033[m~~~'))
        print('{: ^67}'.format('O jogador tem que adivinhar qual a \033[1;031mfruta\033[m foi escolhida pela máquina.'))
        print('')
        print('{: ^67}'.format('Durante a chute de letras o jogador pode \033[1;031mtentar acertar\033[m a palavra,'))
        print('{: ^68}'.format('caso ele acerte o mesmo \033[1;031mvence\033[m, caso contrário ele(a) \033[1;031mperde\033[m uma chance.'))
        print('')
        print('{: ^68}'.format('O mesmo vale para caso o jogador \033[1;031macerte todas a letras\033[m, ele(a) ganha.'))
        print('{: ^68}'.format('Caso \033[1;031merre sete vezes\033[m o jogador perde.'))

        print('~'*68)

    def escolha_tema(tema):
        print('{: ^58}'.format('Escolha um Tema'))
        print('{:-<58} {}'.format('Digite: 1', 'Frutas'))
        print('{:-<58} {}'.format('Digite: 2', 'Objetos'))
        while tema < 1 or tema > 2:
            tema = int(input('Faça sua escolha: '))
        return tema

    def arquivo_do_tema(tema,palavras):
        print('~' * 68)
        if (tema == 1):
            with open('palavrasFrutas.txt') as arquivo:
                palavras = [linha.strip() for linha in arquivo]
            arquivo.close()
        elif (tema == 2):
            with open('palavrasObjetos.txt') as arquivo:
                palavras = [linha.strip() for linha in arquivo]
            arquivo.close()
        return palavras

    def contador_de_erros(erros):
        erros += 1
        sleep(1)
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      \033[1;031m(_)\033[m   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \033[1;031m\ \033[m     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |     \033[1;031m \| \033[m     ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |     \033[1;031m \|/ \033[m   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |      \033[1;031m | \033[m   ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |    \033[1;031m  /  \033[m    ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |     \033[1;031m / \ \033[m   ")

        print(" |            ")
        print("_|___         ")
        print()
        return erros

    def mensagem_enforcado(enforcado):
        print('Que pena, você foi \033[1;031menforcado...\033[m')
        sleep(1)
        print(f'Palavra \033[1;032mcorreta \033[m: {fruta}')
        sleep(1)
        enforcado = True
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        return enforcado
        sleep(1)

    def mensagem_ganhou(acertar):
        print('Parabéns, Você \033[1;032mganhou!\033[m')
        sleep(1)
        print(f'Palavra: {fruta}')

        acertar = True

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
        sleep(1)
        return acertar

    while (not status):
        acertos = erros = tema = 0
        acertar = enforcado = False

        #verificador = 1
        mensagem_inicial()
        sleep(2)
        tema = escolha_tema(tema)
        palavras = arquivo_do_tema(tema,palavras)

        numero = randrange(0, len(palavras))
        fruta = palavras[numero].upper()
        print(fruta) #fruta no jogo
        print()
        print(f'Quantidade de letras: {len(fruta)}')
        tamanho = ['_' for letras in fruta]  # o que vai ser inserido está como primeiro elemento
        # print(fruta) # Mostra palavra escolhida
        while (not acertar and not enforcado):

            chutePal = '0'
            print(tamanho)
            print()
            letra = str(input('Digite uma letra: ')).upper().strip()[0]
            if (letra in fruta): # verifica se tem letras digitadas corretas
                for contador in range(0,len(fruta)):
                    if fruta[contador] == letra:
                        tamanho[contador] = letra
            else:
                erros = contador_de_erros(erros)

            print(tamanho)
            if erros < 7:
                while (chutePal != 'S' and chutePal != 'N'):
                    print()
                    chutePal = str(input('Quer fazer seu palpite? [S/N] ')).upper().strip()
            if chutePal == 'S':
                print()
                palpite = str(input('Digite seu palpite: ')).upper().strip()
                if (palpite == fruta.upper()):
                    for contador in range (0,len(fruta)):
                        tamanho[contador] = fruta
                else:
                    erros = contador_de_erros(erros)

            if (erros == 7):
                enforcado = mensagem_enforcado(enforcado)

            if ('_' not in tamanho):
                acertar = mensagem_ganhou(acertar)

        print('Digite sua escolha: \nJogar novamente: \033[1;032m1\033[m\nvoltar ao menu: \033[1;031m2\033[m\nEncerrar o programa: \033[1;034m3\033[m')
        while  (verificador < 1 or verificador > 3):
            verificador = int(input('Escolha: '))
        if (verificador == 1):
            status = False
            verificador = 0
            print()
            sleep(1)
        elif (verificador == 2):
            print()
            sleep(1)
            jogos.escolha_de_Jogo()  # puxa arquivo/ função
        elif (verificador == 3):
            print('Encerrando o programa...')
            sleep(2)
            status = True

if (__name__ == '__main__'):
    Jogo_forca()