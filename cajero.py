

saldo_disponible = 1000 ##Saldo Disponible en la Cuenta
saldo_disponible=int(saldo_disponible)
accion = 0
print("===================================\n\
BIENVENIDO A SU CAJERO AUTOMATICO\n\
===================================")

while True:

 accion = int(input("que desea hacer \n\
               1.-RETIRAR \n\
               2.-CONSIGNAR \n\
               3.-CONSULTAR SALDO \n\
               4.-SALIR \n\
               DIGITE AQUI SU ELECCION: "))


 if (accion ==1):
    retirar = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
    #print(retirar,"25")
    if (retirar <= saldo_disponible):
        print("RETIRO EXITOSO")
    elif(retirar > saldo_disponible):
        error=int((input("SALDO INSUFICIENTE\n\
              DESEA VERIFICAR SU SALDO?\n\
              1.-SI\n\
              2.-NO\n\
                     DIGITE AQUI SU ELECCION: ")))
        if(error == 1):
            print("SU SALDO DISPONIBLE ES", "$",saldo_disponible)
            
        else:
            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS =)")
    else:
       print("ERROR ACCION NO VALIDA")
 elif(accion == 2):
    consignar = int(input("INGRESE EL MONTO A CONSIGNAR: "))
    if(consignar > 0):
        accionconsig = int(input("ACCION REALIZADA CON EXITO\n\
                        DESEA VER SU NUEVO SALDO?\n\
                        1.-SI \n\
                        2.-NO\n\
                        DIGITE AQUI SU ELECCION: "))
        if (accionconsig == 1):
            saldo_disponible = saldo_disponible + consignar
            print("SU NUEVO SALDO ES", "$",saldo_disponible)
        else:
            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
 elif(accion == 3):
    print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)

 elif(accion == 4):
     print('=======================================')
     print('GRACIAS POR USAR NUESTROS SERVICIOS!\n\
           VUELVA PRONTO')
     print('=======================================')
     break
 else: 
    print("ACCION INCORRECTA, POR FAVOR VERIFIQUE SU ELECCION Y VUELVA A INTENTAR")

