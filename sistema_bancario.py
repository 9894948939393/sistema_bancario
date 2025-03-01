import time
saldo = 0 
deposito = 0 
saque = 0 
extrato = ""
quantidade_de_saques_disponiveis = 3
while True:
    print("""Para acessar as operações clique em :
          1 para depositar 
          2 para sacar
          3 para conferir o saldo atual
          4 para verificar o extrato
          5 para sair
          """)
    time.sleep(2)
    operação = int(input("Digite aqui a operação desejada"))
    if operação == 1:
        deposito = float(input("Digite o valor que você deseja depositar"))
        saldo += deposito
        extrato += f"""
                    depósito no valor de R${deposito}
                    totalizando um valor de {saldo}"""
        print("Depósito realizado com sucesso")
        time.sleep(1)
    elif operação ==2:
        if quantidade_de_saques_disponiveis > 0 :
            saque = float(input("Digite o valor que você deseja sacar"))
            if saque <= 500:
                saldo -= saque
                quantidade_de_saques_disponiveis -= 1
                extrato += f"""
                    saque no valor de R${saque}
                    totalizando um valor de R${saldo}"""
                print("Saque realizado com sucesso")
                time.sleep(1)
            else:
                print("Esse  valor exede seu limite de 500.00 reais do saque")
                time.sleep(2)
        else:
            print("Você já realizou todos os saques disponíveis do dia")    
            time.sleep(2)             
    elif operação ==3:
        print(f"Seu saldo é de {saldo}")
        time.sleep(2)
    elif operação ==4:
        print(f""" Seu extrato é de:
              {extrato}""")
        time.sleep(6)
    elif operação == 5:
        print("Obrigada por usar nossa plataforma !")
        break
    else:
        print("Essa operação não existe")
time.sleep(4)       
