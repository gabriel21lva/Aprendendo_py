while True: 
        print("Calculadora Simples:")

        N1 = int(input("Digite um numero:"))
        N2 = int(input("Digite outro numero:"))

        print("1- adiçao")
        print("2- subtraçao")
        print("3- multipliçao")
        print("4- divisao")
        print("5- Sair")

        operacao = int(input("Qual operaçao deseja fazer?"))

        if operacao == 5:
             print("Saindo da Calculadora...")
             break

        if operacao == 1:
            print(N1 + N2)

        elif operacao == 2:
            print(N1-N2)

        elif operacao == 3:
            print(N1*N2)

        elif operacao == 4:
            print(N1/N2)

        

