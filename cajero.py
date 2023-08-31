saldo_disponible = 1000 ##Saldo Disponible en la Cuenta
valor_a_retirar = input("ingrese la cantidad a retirar:")
  
if (valor_a_retirar <= saldo_disponible):
    print("retiro exitoso")
elif(valor_a_retirar > saldo_disponible):
    print(saldo insuficiente)
else:
    print(input("desea ver su saldo? Y or N :"))