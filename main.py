# Solicitação de valor e cédulas para saque

# Solicita ao usuário o valor que deseja sacar
valor = int(input("Qual o valor que deseja sacar? "))

# Solicita ao usuário o valor máximo das cédulas (1, 2, 5, 10, 20, 50, 100)
cedulas = int(input("Valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100): "))

# Inicializa a variável para contar o número de cédulas utilizadas
total_ced = 0

# Exibe o valor sacado
print("O valor sacado foi de R${}".format(valor))

# Exibe a mensagem de cédulas que serão utilizadas
print("Cédulas: ")

# Loop para calcular as cédulas necessárias para o saque
while True:
    # Verifica se o valor é maior ou igual à cédula atual
    if valor >= 1 and valor >= cedulas:
        # Subtrai o valor da cédula e incrementa o contador de cédulas
        valor -= cedulas
        total_ced += 1
    else:
        # Exibe o número de cédulas de cada valor
        if total_ced > 0:
            print("{} de R${}".format(total_ced, cedulas))
        
        # Atualiza o valor da cédula para a próxima menor
        if cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        
        # Reinicia o contador de cédulas
        total_ced = 0
        
        # Verifica se o valor foi totalmente sacado
        if valor == 0:
            break
