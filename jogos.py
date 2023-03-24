'''
Objetivo com a nova pasta: refazer jogos um e dois. Puxando código.
1 - Menu jogos                                                                     OK
2 - Jogo adivinhação                                                               ok
3 - Jogo forca                                                                     OK
4 - Jo-ken-po                                                                      OK
5 - Jogo da velha                                                                  OK
5- usar recursos de puxar informações de outros arquivos, além de listas e funções OK
'''
def escolha_de_Jogo():
    import ForcaVF
    import AdivinhacaoVF
    import Jo_ken_po_VF
    import JdaVelha
    from time import sleep
    escolha = -1
    verificador = False
    print('~'*55)
    print('{: ^65}'.format('\033[1;32mJogos\033[m'))
    print('~'*55)
    print('{: ^55}'.format('Favor selecionar um dos jogos disponíveis'))
    print('')
    print('{:-<38} {:>1}'.format('Digite: \033[1;32m1\033[m ','\033[1;32mForca\033[m'))
    print('{:-<38} {:>1}'.format('Digite: \033[1;33m2\033[m ','\033[1;33mAdivinhação\033[m'))
    print('{:-<38} {:>1}'.format('Digite: \033[1;34m3\033[m ','\033[1;34mJo-Ken-Po!\033[m'))
    print('{:-<38} {:>1}'.format('Digite: \033[1;31m4\033[m ', '\033[1;31mJogo da Velha\033[m'))
    print('~'*55)

    while not verificador:
        escolha = int(input('Faça sua escolha: '))

        if (escolha > 0 and escolha <= 4):
            verificador = True
    if (escolha == 1):
        print('Você escolheu \033[1;32mForca\033[m!')
        print('Abrindo o jogo...')
        sleep(2)
        ForcaVF.Jogo_forca() # puxa arquivo/ função
    elif(escolha == 2):
        print('Você escolheu \033[1;33mAdivinhação\033[m')
        print('Abrindo o jogo...')
        sleep(2)
        AdivinhacaoVF.Jogo_Adivinhacao()
    elif(escolha == 3):
        print('Você escolheu \033[1;34mJo-Ken-Po!\033[m')
        print('Abrindo o jogo...')
        sleep(2)
        Jo_ken_po_VF.Jogo_jokenpo()
    elif(escolha == 4):
        print('Você escolheu \033[1;31mJogo da Velha\033[m')
        print('Abrindo o jogo...')
        sleep(2)
        JdaVelha.jogo_velha()

if(__name__ == "__main__"): # Verificar novamente essa parte de código
    escolha_de_Jogo()
