print('******************************')
print('*    Jogo da adivinhação		*')
print('******************************')

numero_secreto = 774
total_tentativas = 3

for i in range(total_tentativas):
    print ("voce ainda possui", total_tentativas-i, "tentativas")
    print ("Rodada nº", 1+i)

    chute=int(input("Tente adivinhar o número?"))
    print("Você digitou", chute)

    if (chute == numero_secreto):
        print("Acertou")
        break

    elif (chute > numero_secreto):
        print("É maior que o numero secreto")

    elif (chute < numero_secreto):
        print("É menor que o numero secreto")

    else :
       print("Errrrrrrou")
    print("\n")



