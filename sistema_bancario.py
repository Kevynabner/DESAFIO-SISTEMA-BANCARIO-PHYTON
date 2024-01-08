

menu = """
==== MENU ==== 
[d] = DEPÓSITO
[s] = SAQUE
[e] = EXTRATO
[q] = QUIT
"""
saldo = 0
limite_saque = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3
print(menu)

while True:

    opcao = input(menu)

    if opcao == "d": 
    
        valor_deposito = float(input("digite valor para depósito ?"))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("OPERAÇÃO FALHOU : valor inválido ")
    
    elif opcao == "s":
        valor_saque = float(input("Qual valor deseja sacar ? "))
        
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite_saque
        excedeu_limite_diario = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("OPERAÇÃO FALHOU: saldo insuficiente!")

        elif excedeu_limite:
            print("OPERAÇÃO FALHOU: excedeu o valor para saque! ") 

        elif excedeu_limite_diario:
            print("OPERAÇÃO FALHOU: limite de saque diário atingido!")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"  
            numero_saques += 1

        else:
            print("OPERAÇÃO FALHOU : O valor informado é inválido!")   

    elif opcao == "e":       
        print("\n===============EXTRATO===============")
        print("Não houve movimentações nessa conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break 

    else:
        print("OPERAÇÃO INEXISTENTE: Selecione uma opção válida!")  



          
     
     
     




          
     
     
     

