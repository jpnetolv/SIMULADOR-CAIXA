valor = int(input("Qual o valor que deseja sacar? "))
cedulas = int(input("Valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100): "))
total_ced = 0

print("O valor sacado foi de R${}" .format(valor))
print("Cédulas: ")

while True:
  if valor >= 1 and valor >= cedulas:
    valor -= cedulas
    total_ced += 1  
  else:
    if total_ced > 0:
      print("{} de R${}" .format(total_ced, cedulas))
    if cedulas == 100:
      cedulas = 50
    elif cedulas ==  50:
      cedulas = 20
    elif cedulas == 20:
      cedulas = 10
    elif cedulas == 10:
      cedulas = 5
    elif cedulas == 5:
      cedulas = 2
    elif cedulas == 2:
      cedulas = 1
    total_ced = 0
    if valor == 0:
      break