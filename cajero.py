saldo_disponible = 1000 ##Saldo Disponible en la Cuenta

accion = input("que desea hacer 1.-retirar 2.-consignar 3.-Consultar Saldo : ")

#valor_a_consignar = input("ingrese la cantidad a consignar sin puntos ni espacios")    

#valor_a_retirar = input("ingrese la cantidad a retirar:")

accion1 = int(accion) 

valor_retiro1 = 0
valor_retiro = int(valor_retiro1)

if (accion1 == 1):
    valor_retiro1 = print(input("ingrese la cantidad a retirar:"))
print(valor_retiro)

"""        if (valor_retiro => saldo_disponible):
        print(input("saldo insuficiente para realizar el retiro,\n\
            desea ver su saldo? Y or N :"))
        else:
        print("retiro exitoso")
        
        print(input("desea ver su saldo restante? Y or N:"))

elif (accion1 == 2):
    print (input("ingrese la cantidad a consignar sin puntos ni espacios"))

elif (accion1 == 3):
    print ("$",saldo_disponible, "<----- este es su saldo disponible.")

elif (accion1 >= 4):
    print("Error digite uno de los numeros indicados en el menu principal.", accion)

#valor_a_consignar = input("ingrese la cantidad a consignar sin puntos ni espacios")    

#valor_a_retirar = input("ingrese la cantidad a retirar:")
#cantidad = int(valor_a_retirar) 
#if (cantidad <= saldo_disponible):
   # print("retiro exitoso")
#elif(cantidad > saldo_disponible):
   # print("saldo insuficiente")"""
