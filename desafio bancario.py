menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = float(0)
limite = float(500)
extrato = []
numero_saques = 0 
LIMITE_SAQUES = 3


while True:
    opcao=input(menu)

    if opcao=="d":
        print("Informar o valor de depósito: \n")
        deposito=float(input())
        saldo += deposito
        f=format(deposito,".2f")
        extrato.append(f"+ R${f}")
        print(f"deposito de R$ {f} realizado com sucesso.\n")
        

    elif opcao=="s":
        

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário excedido.\n")

        else:
            print("Informar valor de saque: \n")
            saque = float(input())

            if saque > saldo:
                print("Você não possui saldo suficiente para realizar essa ação. \n")

            elif saque > limite:    
                print(f"O limite de saque é de R$ {limite} \n")

            else:
                saldo-=saque
                f=format(saque,".2f")
                extrato.append(f"- R${f}")              
                print(f"Saque de R$ {f} realizado com sucesso. ")
                numero_saques+=1



    elif opcao=="e":
        print("Lançamentos: \n")
        print(extrato)
        f=format(saldo,".2f")
        print(f"\n O seu saldo atual é de R$ {f}")

    elif opcao=="q":
        break    

    else:
        print("Operação inválida, por favor selecione novamente")


