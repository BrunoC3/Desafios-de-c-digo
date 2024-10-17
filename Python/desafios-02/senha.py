tentativas = 4

while tentativas > 0:
    senha = int(input('Qual é a senha de 4 digitos? '))
    if senha == 1234:
        print('Acesso Liberado!')
        break
    else:
        print(f'Você errou a senha e tem mais {tentativas - 1} tentativas')
        tentativas -= 1
