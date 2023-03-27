'''
Jogo Jo-Ken-Po!
Jogo basico de pedra, papel e tesoura
1- entrada simples do jogador                                                                   OK
2 - máquina escolhe uma das três opções                                                         OK
3 - computador verifica se jogador ganhou ou não                                                OK
4 - Mensagem de vitória e derrota, acrescimo de descrição                                       OK
5 - acrescentar icones de vitória e derrota/ prints como gravuras representando os formatos
6 - Usar padrão ANSI de cores para colocar cor nos prints                                       OK
7 - fragmentar o jogo em funções                                                                OK
8 - colocar repetição como dificuldade em tentativas (1: difícil, 3: médio, 5:fácil)            OK
9 - Colocar timer (intervalo entre jogadas) para deixar o jogo mais orgânico                    OK

papel bate pedra
pedra bate tesoura
tesoura bate papel
'''
def Jogo_jokenpo():


    from time import sleep
    from random import randrange
    import jogos


    def mensagem_inicial():
        print('~'*50)
        print('{: ^60}'.format('\033[1;34mjogo de Jo-Ken-Po!\033[m'))
        print('~'*50)
        print('')
        print('{: ^50}'.format('escolha sua dificuldade'))
        print('{:-<47} {}'.format('\033[1;32mFácil\033[m: (1)',' Tentativas: \033[1;32m5\033[m'))
        print('{:-<47} {}'.format('\033[1;33mMédio\033[m: (2)', ' Tentativas: \033[1;33m3\033[m'))
        print('{:-<47} {}'.format('\033[1;31mDifícil\033[m: (3)', ' Tentativas: \033[1;31m1\033[m'))

    def dificuldade_selecao(contadorF):
        dificuldade = 0
        while dificuldade < 1 or dificuldade > 3:
            dificuldade = int(input('Escolha: '))
        # Atribuição no contador de dificuldade
        if (dificuldade == 1):
            contadorF = 5
        elif (dificuldade == 2):
            contadorF = 3
        elif (dificuldade == 3):
            contadorF = 1
        return contadorF

    def mensagem_de_jogo_dois():
        print('~' * 50)
        print('{: ^60}'.format('\033[1;34mjogo de Jo-Ken-Po!\033[m'))
        print('~' * 50)
        print('')

        print('{: ^50}'.format('Escolha uma opção!'))
        print('{:-<48} {}'.format('\033[1;31mPedra\033[m', '\033[1;31m1\033[m'))
        print('{:-<48} {}'.format('\033[1;32mPapel\033[m', '\033[1;32m2\033[m'))
        print('{:-<48} {}'.format('\033[1;33mTesoura\033[m', '\033[1;33m3\033[m'))

    def verificacao_vitoria(escolha,maquina,venceu):
        # linhas de código para vencer
        if (escolha == 1 and maquina == 3):
            venceu = True
        elif (escolha == 2 and maquina == 1):
            venceu = True
        elif (escolha == 3 and maquina == 2):
            venceu = True
        return venceu

    def verificacao_derrota(escolha,maquina,perdeu):
        # linhas de código para perder
        if (escolha == 3 and maquina == 1):
            perdeu = True
        elif (escolha == 1 and maquina == 2):
            perdeu = True
        elif (escolha == 2 and maquina == 3):
            perdeu = True
        return perdeu

    def mensagem_de_jogo_final(venceu,empate,perdeu,Ljoken,contadorI,contadorF,escolha,maquina):
        if (venceu):
            print('Parabéns!!! você \033[1;32mvenceu\033[m!!!')
            print(f'\033[1;32m{Ljoken[escolha-1].capitalize()}\033[m vence de \033[1;31m{Ljoken[maquina-1].capitalize()}\033[m!!')

            contadorI = contadorF + 1
            sleep(2)
        elif(empate):
            print('\033[1;33mEmpate!!\033[m')
            sleep(1)
            print('Tente novamente...')
            sleep(1)
        elif (perdeu):
            print('Que pena... Você \033[1;31mperdeu\033[m a rodada.')
            print(f'\033[1;31m{Ljoken[maquina - 1].capitalize()}\033[m vence de \033[1;32m{Ljoken[escolha - 1].capitalize()}\033[m!!')
            contadorI += 1
            sleep(2)
            if(contadorI == contadorF + 1):
                print('Ah! que pena... Você \033[1;31mperdeu\033[m...')
                sleep(1)
        return contadorI
    status = False

    while (not status):
        contadorF = verificador = 0
        contadorI = 1

        Ljoken = ['pedra','papel','tesoura']


        mensagem_inicial()
        contadorF = dificuldade_selecao(contadorF)

        while contadorI <= contadorF:

            maquina = randrange(1, 4)
            #print(maquina)
            venceu = False
            perdeu = False
            empate = False
            escolha = 0
            mensagem_de_jogo_dois()

            print(f'Tentativa {contadorI} de {contadorF}')

            while (escolha < 1 or escolha > 3):
                escolha = int(input('Escolha: '))

            empate = escolha == maquina # retornar True

            venceu = verificacao_vitoria(escolha,maquina,venceu)

            perdeu = verificacao_derrota(escolha,maquina,perdeu)

            print('\033[1;32mJo\033[m')
            print()
            sleep(1)
            print('\033[1;32mKen\033[m')
            print()
            sleep(1)
            print('\033[1;32mPo!\033[m')
            print()
            sleep(1)

            contadorI = mensagem_de_jogo_final(venceu,empate,perdeu,Ljoken,contadorI,contadorF,escolha,maquina)
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


if (__name__ == '__main__'):
    Jogo_jokenpo()