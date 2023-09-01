import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = float(0)
limite = float(500)
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3


while True:
    opcao=input(menu)

    if opcao=="d":
        print("Informar o valor de depósito: \n")
        deposito=float(input())
        saldo += deposito
        data = datetime.datetime.now()
        data_formatada = data.strftime("%d/%m/%Y, %H:%M:%S")
        f=format(deposito,".2f")
        extrato +=(f"Data: {data_formatada},  Depósito: + R$ {f}\n")
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
                data = datetime.datetime.now()
                data_formatada = data.strftime("%d/%m/%Y, %H:%M:%S")
                f=format(saque,".2f")
                extrato +=(f"Data: {data_formatada},  Saque:    - R$ {f}\n")
                numero_saques+=1
                print(f"saque de R$ {f} realizado com sucesso.\n")

    elif opcao=="e":

        if extrato=="":
            print("\n---SEM MOVIMENTAÇÕES---\n")

        else:
            print("==== LANÇAMENTOS ====\n\n")
            print(extrato)
            f=format(saldo,".2f")
            print(f"\n O seu saldo atual é de R$ {f}")

    elif opcao=="q":
        break    

    else:
        print("Operação inválida, por favor selecione novamente")
