'''
Jogo da Forca
Jogador deve adivinhar um número entre 0 e 100

Temos que ter três dificuldades: fácil: 10 tentativas/ Médio: 5 Tentativas/ Difícil: 3 Tentativas
Caso o jogador Chute um número maior que o escolhido: O programa deve informar que passou do número da máquina.
Caso o jogador Chute um número menor que o escolhido: O programa deve informar que deve tentar um número maior
pontuação = começa em 1000 e é diminuído confome desempenho

Acrescimos:

Adicionar elementos tipo Troféu e uma imagem para representar derrota.
Colocar código dividido em funções
Colocar cores
'''

def Jogo_Adivinhacao():
    from random import randrange
    maquina = randrange(0,100)
    escolha = tentativa = 0
    pontuacao = 1000
    #print(maquina)

    def mensagem_inicial():
        print('~'*50)
        print('{: ^60}'.format('\033[1;33mAdivinhação!\033[m'))
        print('~'*50)
        print('{: ^50}'.format('Adivinhe um número entre 0 e 100'))
        print('~' * 50)
        print('')
        print('{: ^50}'.format('Escolha sua dificuldade: '))
        print('{:-<25}{}'.format('1 ',' \033[1;32mFácil\033[m: Tentativas (10)'))
        print('{:-<25}{}'.format('2 ', ' \033[1;33mMédio\033[m: Tentativas (5)'))
        print('{:-<25}{}'.format('3 ', ' \033[1;31mDifícil\033[m: Tentativas (4)'))
        print('')

    def jogo_modo_facil(pontuacao):

        print('Dificuldade \033[1;32mFácil\033[m')
        tentativa = 10
        while tentativa > 0:
            chute = int(input('Digite seu chute: '))
            if (chute == maquina):
                print('Parabéns, você \033[1;32macertou\033[m!!')
                print(f'Pontuação final: {pontuacao}')
                break
            elif (chute != maquina):
                tentativa -= 1
                pontuacao -= 100
                print('Resposta \033[1;31mErrada!!\033[m')
                if (tentativa == 0):
                    print('Mas que pena, você \033[1;31mperdeu\033[m...')
                    print('Número correto: \033[1;31m{}\033[m'.format(maquina))
                    print(f'Pontuação final: {pontuacao}')
                elif (chute > maquina and tentativa > 0):
                    print('Tente um número a baixo!!')
                    print('')
                elif (chute < maquina and tentativa > 0):
                    print('Tente um número a cima!!')
                    print('')

    def jogo_modo_medio(pontuacao):
        print('Dificuldade \033[1;33mMédio\033[m')
        tentativa = 5
        while tentativa > 0:
            chute = int(input('Digite seu chute: '))
            if (chute == maquina):
                print('Parabéns, você \033[1;32macertou\033[m!!')
                print(f'Pontuação final: {pontuacao}')
                break
            elif (chute != maquina):
                tentativa -= 1
                pontuacao -= 200
                print('Resposta \033[1;31mErrada!!\033[m')
                if (tentativa == 0):
                    print('Mas que pena, você \033[1;31mperdeu\033[m...')
                    print('Número correto: \033[1;31m{}\033[m'.format(maquina))
                    print(f'Pontuação final: {pontuacao}')
                elif (chute > maquina and tentativa > 0):
                    print('Tente um número a baixo!!')
                    print('')
                elif (chute < maquina and tentativa > 0):
                    print('Tente um número a cima!!')
                    print('')

    def jogo_modo_dificil(pontuacao):
        print('Dificuldade \033[1;31mDifícil\033[m')
        tentativa = 4
        while tentativa > 0:
            chute = int(input('Digite seu chute: '))
            if (chute == maquina):
                print('Parabéns, você \033[1;32macertou\033[m!!')
                print(f'Pontuação final: {pontuacao}')
                break
            elif (chute != maquina):
                tentativa -= 1
                pontuacao -= 250
                print('Resposta \033[1;31mErrada!!\033[m')
                if (tentativa == 0):
                    print('Mas que pena, você \033[1;31mperdeu\033[m...')
                    print('Número correto: \033[1;31m{}\033[m'.format(maquina))
                    print(f'Pontuação final: {pontuacao}')
                elif (chute > maquina and tentativa > 0):
                    print('Tente um número a baixo!!')
                    print('')
                elif (chute < maquina and tentativa > 0):
                    print('Tente um número a cima!!')
                    print('')

    mensagem_inicial()

    while escolha < 1 or escolha > 4:
        escolha = int(input('Escolha: '))
    if (escolha == 1):
        jogo_modo_facil(pontuacao)
    elif (escolha == 2):
        jogo_modo_medio(pontuacao)
    elif(escolha == 3):
        jogo_modo_dificil(pontuacao)

if (__name__ == '__main__'):
    Jogo_Adivinhacao()