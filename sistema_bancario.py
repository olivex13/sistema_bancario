print ("SISTEMA BANCÁRIO DO BANCO LARANJA")
saldo_conta = 500
selecionar_funcao = None

while selecionar_funcao !=0:
    selecionar_funcao = int(input("[1] Sacar\n[2] Depositar\n[3] Consultar Saldo\n[0] Sair\n Digite a opção desejada: "))

    if selecionar_funcao == 1:
        valor_saque = int(input("Digite o valor do saque: "))
        if valor_saque <= saldo_conta:
                saldo_conta -= valor_saque
                print(f"Saque realizado com sucesso, o valor do saldo é {saldo_conta}")
        else:
                print("Saldo insuficiente. Operação de saque cancelada.")

    elif selecionar_funcao == 2:
        valor_deposito = int(input("Digite o valor do deposito: "))
        saldo_conta += valor_deposito
        print(f"Deposito realizado com sucesso, seu novo saldo é {saldo_conta}")
        
    elif selecionar_funcao == 3:
        print(f"O seu saldo é {saldo_conta}")

    elif selecionar_funcao == 0:
        print("Obrigado por usar nossos serviços, até breve.")
        break
    
    else:
        print("Digite uma opção válida")