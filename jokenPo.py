# import random

# posicao = int(input("Digite [1]Pedra, [2]tesoura, [3]papel\n"))

# maquina = 3 #random.randint(1, 3)

# print(f"Você escolheu {posicao} ")
# print(f"A maquina escolheu {maquina}")

# # while posicao != maquina:
# if posicao == 1 and maquina == 3:
#     print('Você perdeu!!!!')
#         # continue
# elif posicao == 2 and maquina == 1:
#     print('Você perdeu!!!')
#         # continue
# elif posicao == 3 and maquina == 2:
#     print('Você perdeu!!')
#         # continue
    
# if posicao == 3 and maquina == 1:
#     print('Você ganhou!!!!')
#         # break
# elif posicao == 1 and maquina == 2:
#     print('Você ganhou!!!!')
#         # break
# elif posicao == 2 and maquina == 3:
#     print('Você ganhou!!!!')
#         # break
# else:
#     print('Empate')

import random

posicao = int(input("Vamos jogar joken Pô? [1]Sim, [2]Não\n"))

while posicao > 2 or posicao < 1:
    if posicao > 2 or posicao < 1:
        print('Numero invalido. Digite novamente!!\n')
        posicao = int(input("Vamos jogar joken Pô? [1]Sim, [2]Não\n"))
    else:
        print('Numero invalido. Digite novamente!!\n')
        posicao = int(input("Vamos jogar joken Pô? [1]Sim, [2]Não\n"))

if posicao == 1:
    
    for i in range(3):
        vitoria = 0
        derrota = 0
        while posicao != 2:
            print('Placar')
            print(f"Derrotas: {derrota}")
            print(f"Vitórias: {vitoria}")
            
            posicao2 = int(input("Digite [1]Pedra, [2]tesoura, [3]papel\n"))
            
            # pedra = 1
            # tesoura = 2
            # papel = 3
                
            reinicio = 0
            
            playAgain = 0
            
            maquina2 = 3 #random.randint(1, 3)
                
            print(f"Você escolheu {posicao2} ")
            print(f"A maquina escolheu {maquina2}")
            
            
            if posicao2 == 1 and maquina2 == 3:
                print('Você perdeu!!!!')
                derrota = derrota + 1
                        # continue
            elif posicao2 == 2 and maquina2 == 1:
                print('Você perdeu!!!')
                derrota = derrota + 1
                        # continue
            elif posicao2 == 3 and maquina2 == 2:
                print('Você perdeu!!')
                derrota = derrota + 1
                        # continue
                        
            elif posicao2 == 3 and maquina2 == 1:
                print('Você ganhou!!!!')
                vitoria = vitoria + 1
                        # break
            elif posicao2 == 1 and maquina2 == 2:
                print('Você ganhou!!!!')
                vitoria = vitoria + 1
                        # break
            elif posicao2 == 2 and maquina2 == 3:
                print('Você ganhou!!!!')
                vitoria = vitoria + 1
                        # break
                            
            elif posicao2 == 3 and maquina2 == 3:
                print('Empate')
            elif posicao2 == 2 and maquina2 == 2:
                print('Empate')
            elif posicao2 == 1 and maquina2 == 1:
                print('Empate')
                    
            
                
            if reinicio == 2:
                print(f"Derrotas: {derrota}")
                print(f"Vitórias: {vitoria}")
                print('Bom Jogo... Até a proxima..')
                break
                
            playAgain = int(input('Você deseja continuar?? [1]Sim, [2]Não\n'))
            
            if playAgain > 3:
                print('Ops. Já foi melhor de 3')
                break
        
else:
    print('Tudo Bem. Até a proxima..')
    
#     contador = 0
# for i in range(10):
#     contador += 1
# print(contador) # Resultado: 10
