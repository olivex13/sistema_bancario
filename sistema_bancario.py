print ("SISTEMA BANCÁRIO DO BANCO LARANJA".center(60, " "))
print ("")
saldo_conta = 0
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR = 500
selecionar_funcao = None


menu = """
[1] Sacar
[2] Depositar
[3] Extrato 
[0] Sair
"""

while True:
    selecionar_funcao = input(menu)

    if selecionar_funcao == '1':
        valor_saque = float(input("Digite o valor do saque: "))
        excedeu_limite = valor_saque > LIMITE_VALOR
        excedeu_saques = numero_saques > LIMITE_SAQUES
        excedeu_saldo = valor_saque > saldo_conta
        
        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! O valor do saque excede o limite de saques.")
        elif excedeu_saldo:
            print("Operação falhou! O valor do saque excede o Saldo.")
        elif valor_saque > 0:
            saldo_conta -= valor_saque
            numero_saques += 1
            print(f'Saque realizado com sucesso, seu novo saldo é R$ {saldo_conta:.2f}')
            extrato += f"Saque: R${valor_saque:.2f} \n"
           
    elif selecionar_funcao == '2':
        valor_deposito = float(input("Digite o valor do deposito: "))
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato += f"Deposito: R${valor_deposito:.2f} \n"
            print(f"Valor depositado com sucesso, seu novo saldo é: R$ {saldo_conta:.2f}")
        else:
            print("Operação falhou! Digite um valor válido.")
        
    elif selecionar_funcao == '3':
        print(f"O extrato da sua conta é: \n {extrato} O valor em conta é: {saldo_conta:.2f}")

    elif selecionar_funcao == 0:
        print("Obrigado por usar nossos serviços, até breve.")
        break
    
    else:
        print("Digite uma opção válida")