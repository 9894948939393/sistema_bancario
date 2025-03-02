import pandas as pd
import time
saldo = 0 
deposito = 0 
saque = 0 
extrato = ""
valor_total_circulante=0
limite = 500
quantidade_de_saques_disponiveis = 3

# while True:
#     print("""Para acessar as operações clique em :
#           1 para depositar 
#           2 para sacar
#           3 para conferir o saldo atual
#           4 para verificar o extrato
#           5 para revisar limites
#           6 para sair
#           """)
#     time.sleep(2)
#     operação = int(input("Digite aqui a operação desejada"))
#     if operação == 1:
#         deposito = float(input("Digite o valor que você deseja depositar"))
#         saldo += deposito
#         extrato += f"""
#                     depósito no valor de R${deposito}
#                     totalizando um valor de {saldo}"""
#         print("Depósito realizado com sucesso")
#         valor_total_circulante += saldo
#         time.sleep(1)
#     elif operação ==2:
#         if quantidade_de_saques_disponiveis > 0 :
#             saque = float(input("Digite o valor que você deseja sacar"))
#             if saque <= limite:
#                 saldo -= saque
#                 quantidade_de_saques_disponiveis -= 1
#                 extrato += f"""
#                     saque no valor de R${saque}
#                     totalizando um valor de R${saldo}"""
#                 print("Saque realizado com sucesso")
#                 time.sleep(1)
#             else:
#                 print("Esse  valor exede seu limite de 500.00 reais do saque")
#                 time.sleep(2)
#         else:
#             print("Você já realizou todos os saques disponíveis do dia")    
#             time.sleep(2)             
#     elif operação ==3:
#         print(f"Seu saldo é de {saldo}")
#         time.sleep(2)
#     elif operação ==4:
#         print(f""" Seu extrato é de:
#               {extrato}""")
#         time.sleep(6)
#     elif operação == 5:
#         print(f"""Atualmente você pode fazer {quantidade_de_saques_disponiveis} saques de até {limite} reais
# Caso você queira aumentar a quantidade de saques digite 1 
# Caso queira aumetar o limite de saques digite 2 
# Caso queira sair digite outro número""")
#         time.sleep(2)
#         operação_limite = int(input("Digite a operação desejada"))
#         if operação_limite == 1:
#             print("Iniciando a avaliação de limites")
#             time.sleep(2)
#             print(f" A nova quantidade proposta é de {(quantidade_de_saques_disponiveis + valor_total_circulante//4000):.0}")
#             time.sleep(1)
#             print("""Caso queira aceitar o novo limite digite 1, 
# caso não, digite outro número""")
#             if int(input("Quer aceitar ou não")) == 1:
#                 print(" Seu novo limite foi estabelecido")
#                 quantidade_de_saques_disponiveis += valor_total_circulante//4000
#                 time.sleep(2)
#             else:
#                 print(" O seu limite se manteve o mesmo")
#                 time.sleep(2)
#         elif operação_limite == 2:
#             print("Iniciando a avaliação de limites")
#             time.sleep(2)
#             print(f" O novo limite proposto é de {(limite + valor_total_circulante // 400)} reais")
#             time.sleep(1)
#             print("""Caso queira aceitar o novo limite digite 1,
# caso não, digite outro número""")
#             if int(input("Quer aceitar ou não")) == 1:
#                 print(" Seu novo limite foi estabelecido")
#                 limite += valor_total_circulante // 400
#                 time.sleep(2)
#             else:
#                 print(" O seu limite se manteve o mesmo")
#                 time.sleep(2)
#         else:
#             print("Você saiu da área de limites")
#             time.sleep(2)
#     elif operação == 6:
#         print("Obrigada por usar nossa plataforma !")
#         break
#     else:
#         print("Essa operação não existe")
# time.sleep(4)       
