import time
saldo = 0 
deposito = 0 
saque = 0 
extrato = 0
quantidade_de_saques_disponiveis = 3
while True:
    print("""Para acessar as operações clique em :
          1 para depositar 
          2 para sacar
          3 para conferir o saldo atual
          4 para verificar o extrato
          """)
    time.sleep(2)
    operação = int(input("Digite aqui a operação desejada"))
    if operação == 1:
        time.sleep(1)
        deposito = float(input("Digite o valor que você deseja depositar"))
        saldo += deposito
        extrato = "".join(f"""
                    depósito no valor de R${deposito}
                    totalizando um valor de {saldo}""")
    elif operação ==2:
        time.sleep(1)
        saque = float(input("Digite o valor que você deseja sacar"))
        if saque <= 500 :
            if quantidade_de_saques_disponiveis > 0:
                saldo -= saque
                extrato = "".join( f"""
                    saque no valor de R${saque}
                    totalizando um valor de R${saldo}""")
            else:
                print("Você já excedeu o limite máximo de saques do dia")
        else:
            print("Esse valor excede o limite de 500.00 reais do saque")    
            time.sleep(3)             
    elif operação ==3:
        print(f"Seu saldo é de {saldo}")
    elif operação ==4:
        print(f""" Seu extrato é de:
              {extrato}""")
    else:
        print("Essa operação não existe")
time.sleep(4)       
