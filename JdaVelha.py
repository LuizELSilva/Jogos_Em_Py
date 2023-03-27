'''
1 - Fazer jogo utilizando listas                                               OK
2 - Colocar opção para jogar contra a máquina ou contra o jogador 2            OK
3 - Deixar a interface mais apresentável                                       OK
4 - Melhorar o grid                                                            OK
5 - Colocar cores                                                              OK
6 - fragmentar código em funções                                               OK
7 - Melhorar sistema de vítoria (diminur código)                               OK
8 - corrigir jogador caso o mesmo digite um número a cima de 9 e abaixo de 1:  OK


'''


def jogo_velha ():
    from time import sleep
    from random import randint
    import jogos

    def J_tabuleiro(jVelha): # criando tabuleiro em função

        for contador in range (0,len(jVelha)):
            print(jVelha[contador], end = ' ')
            if contador == 0 or contador == 1 or contador == 3 or contador == 4 or  contador == 6 or contador == 7:
                print('| ',end = '')
            if contador == 2 or contador == 5:
                print('')
        print('')

    def verifica_vencedor(jVelha,jogador):
        contadorV1 = 0
        contadorV2 = 1
        contadorV3 = 2

        for c in range (0,3): # verificador Horizontal
            if jVelha[contadorV1] == jogador and jVelha[contadorV2] == jogador and jVelha[contadorV3] == jogador:
                if jogador == 'X':
                    return 1
                else:
                    return 2
            contadorV1 += 3
            contadorV2 += 3
            contadorV3 += 3

        contadorV1 = 0
        contadorV2 = 3
        contadorV3 = 6

        for c in range(0, 3): # Verificador Vertical
            if jVelha[contadorV1] == jogador and jVelha[contadorV2] == jogador and jVelha[contadorV3] == jogador:
                if jogador == 'X':
                    return 1
                else:
                    return 2
            contadorV1 += 1
            contadorV2 += 1
            contadorV3 += 1

        if jVelha[0] == jogador and jVelha[4] == jogador and jVelha[8] == jogador: # Verifica Diagonal
            if jogador == 'X':
                return 1
            else:
                return 2
        elif jVelha[2] == jogador and jVelha[4] == jogador and jVelha[6] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
        return 0

    def mensagem_inicial(jogador): # Mensagem inicial e escolha de jogadores
        from time import sleep
        print('='*65)
        print('{: ^70}'.format('\033[1;32mJogo da Velha simples\033[m'))
        print('='*65)
        sleep(1)
        print('{: ^70}'.format('\033[1;31mRegras\033[m'))
        print('{: ^70}'.format('Complete linhas \033[1;31mverticais\033[m ou \033[1;31mhorizontais\033[m para completar o jogo.'))
        print('{: ^70}'.format('Escolha uma opção no Grid de acordo com sua \033[1;31mnumeração\033[m.'))
        sleep(1)
        print('{: ^60}'.format('Segue exemplo:'))

        print('{: ^60}'.format('_ | _ | _   >   1  2  3'))
        print('{: ^60}'.format('_ | _ | _   >   4  5  6'))
        print('{: ^60}'.format('_ | _ | _   >   7  8  9'))
        print('='*65)
        sleep(1)

        print('{: ^70}'.format('\033[1;31mEscolha\033[m'))
        print('{: ^70}'.format('Jogador VS Máquina \033[1;32m[1]\033[m'))
        print('{: ^70}'.format('Jogador VS Jogador \033[1;34m[2]\033[m'))
        while jogador <= 0 or jogador > 2:
            jogador = int(input('Escolha: '))
        return jogador

    def jogador_1(escolha): # Jogada do jogador 1
        escolha = 0
        print('')
        print('\033[1;32mJogador 1\033[m')
        while escolha < 1 or escolha > 9:
            escolha = int(input('Escolha uma opção Vazia: '))
        while jVelha[escolha - 1] != '_':
            escolha = 0
            print('Jogada inválida!\nSua escolha já abriga uma jogada!')
            print()
            while escolha < 1 or escolha > 9:
                escolha = int(input('Escolha uma opção Vazia: '))
        return escolha

    def jogada_maquina(escolha_pc):
        escolha_pc = randint(1, 9)
        while jVelha[escolha_pc - 1] != '_':
            escolha_pc = randint(1, 9)
        return escolha_pc

    def jogador_2(escolha):
        escolha = 0
        print('\033[1;34mJogador 2\033[m')
        while escolha < 1 or escolha > 9:
            escolha = int(input('Escolha uma opção Vazia: '))
        while jVelha[escolha - 1] != '_':
            escolha = 0
            print('Jogada inválida!\nSua escolha já abriga uma jogada!')
            print()
            while escolha < 1 or escolha > 9:
                escolha = int(input('Escolha uma opção Vazia: '))
        return escolha

    def mensagem_fim_do_jogo(jogadores,vencedor):
        if jogadores == 1:
            if vencedor == 1:
                sleep(1)
                print('Parabéns você ganhou!!!')
                sleep(1)
                print("\033[1;33m       ___________      \033[m")
                print("\033[1;33m      '._==_==_=_.'     \033[m")
                print("\033[1;33m      .-\\:      /-.    \033[m")
                print("\033[1;33m     | (|:.     |) |    \033[m")
                print("\033[1;33m      '-|:.     |-'     \033[m")
                print("\033[1;33m        \\::.    /      \033[m")
                print("\033[1;33m         '::. .'        \033[m")
                print("\033[1;33m           ) (          \033[m")
                print("\033[1;33m         _.' '._        \033[m")
                print("\033[1;33m        '-------'       \033[m")
            elif vencedor == 2:
                sleep(1)
                print('que pena perdeu...')
                sleep(1)
            else:
                sleep(1)
                print('Empate!!!')
                sleep(1)

        elif jogadores == 2:
            if vencedor == 1:
                sleep(1)
                print('Parabéns! Jogador 1 Ganhou!!!')
                sleep(1)
                print("\033[1;33m       ___________      \033[m")
                print("\033[1;33m      '._==_==_=_.'     \033[m")
                print("\033[1;33m      .-\\:      /-.    \033[m")
                print("\033[1;33m     | (|:.     |) |    \033[m")
                print("\033[1;33m      '-|:.     |-'     \033[m")
                print("\033[1;33m        \\::.    /      \033[m")
                print("\033[1;33m         '::. .'        \033[m")
                print("\033[1;33m           ) (          \033[m")
                print("\033[1;33m         _.' '._        \033[m")
                print("\033[1;33m        '-------'       \033[m")
                sleep(1)
            elif vencedor == 2:

                sleep(1)
                print('Parabéns! Jogador 2 Ganhou!!!')
                sleep(1)
                print("\033[1;33m       ___________      \033[m")
                print("\033[1;33m      '._==_==_=_.'     \033[m")
                print("\033[1;33m      .-\\:      /-.    \033[m")
                print("\033[1;33m     | (|:.     |) |    \033[m")
                print("\033[1;33m      '-|:.     |-'     \033[m")
                print("\033[1;33m        \\::.    /      \033[m")
                print("\033[1;33m         '::. .'        \033[m")
                print("\033[1;33m           ) (          \033[m")
                print("\033[1;33m         _.' '._        \033[m")
                print("\033[1;33m        '-------'       \033[m")
                sleep(1)

            else:
                sleep(1)
                print('Empate!!!')
                sleep(1)
    status = False

    while (not status):

        escolha = vencedor = Q_escolhas = jogadores = escolha_pc = verificador = 0
        jVelha = ['_' for c in range(0, 9)] # criando lista

        jogadores = mensagem_inicial(jogadores) # Retorno em função de escolha de jogadores

        print()
        print('O stauts atual do grid é:\n')

        J_tabuleiro(jVelha)
        while True:

            escolha = jogador_1(escolha)
            jVelha[escolha - 1] = 'X'
            Q_escolhas += 1

            vencedor = verifica_vencedor(jVelha,'X')

            if vencedor != 0:
                break
            elif Q_escolhas == 9:
                break

            print()
            print('O stauts atual do grid é:\n')
            J_tabuleiro(jVelha)

            if jogadores == 1:
                escolha_pc = jogada_maquina(escolha_pc)
                jVelha[escolha_pc - 1] = 'O'
                Q_escolhas += 1
                print('Jogada da máquina:\n')

            elif jogadores == 2:
                escolha = jogador_2(escolha)
                jVelha[escolha - 1] = 'O'
                Q_escolhas += 1
                print('O stauts atual do grid é:\n')

            vencedor = verifica_vencedor(jVelha,'O')

            if vencedor != 0:
                break
            elif Q_escolhas == 9:
                break

            J_tabuleiro(jVelha)

        mensagem_fim_do_jogo(jogadores,vencedor)
        print()
        print('Grid Final: ')
        J_tabuleiro(jVelha)

        sleep(1)
        print()

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


if (__name__ == "__main__"):
    jogo_velha()


