#cajero automatico con funcionalidades basicas

saldo_disponible = 1000 ##Saldo Disponible en la Cuenta
saldo_disponible=int(saldo_disponible)

usuario = [ ["45235", "1245", "Pepito Perez", 20000], ["78455", "3648", "Jaimito Cartero", 5000]            ]


accion = 0
print("===================================\n\
BIENVENIDO A SU CAJERO AUTOMATICO\n\
===================================")

while True:
 iniciosesu = input( "INGRESE SU NUMERO DE CUENTA: ")
 if (iniciosesu == usuario [0] [0] ):
    print("acceso correcto")
    iniciosesc = input("INGRESE SU CONTRASEÑA")
 else:
    print("error cuenta no existe")




 

 

 


 while True:

  accion = input("que desea hacer \n\
               1.-RETIRAR \n\
               2.-CONSIGNAR \n\
               3.-CONSULTAR SALDO \n\
               4.-SALIR \n\
               DIGITE AQUI SU ELECCION: ")


  if (accion =="1"):
    retirar = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
    #print(retirar,"25")
    if (retirar <= saldo_disponible):
       accionret = int(input("ACCION REALIZADA CON EXITO\n\
                        DESEA VER SU NUEVO SALDO?\n\
                        1.-SI \n\
                        2.-NO\n\
                        DIGITE AQUI SU ELECCION: "))
       if (accionret == 1):
                saldo_disponible = saldo_disponible - retirar
                print("==============================================")
                print("SU NUEVO SALDO ES", "$",saldo_disponible,)
                print("==============================================")
       else:
            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")

        #print("RETIRO EXITOSO")
    elif(retirar > saldo_disponible):
        error=int((input("SALDO INSUFICIENTE\n\
              DESEA VERIFICAR SU SALDO?\n\
              1.-SI\n\
              2.-NO\n\
                     DIGITE AQUI SU ELECCION: ")))
        if(error == 1):
            print("==============================================")
            print("SU SALDO DISPONIBLE ES", "$",saldo_disponible)
            print("==============================================")

        else:
            print("==============================================")
            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS =)")
            print("==============================================")
    else:
       print("==============================================")
       print("ERROR ACCION NO VALIDA")
       print("==============================================")
  elif(accion == "2"):
    consignar = int(input("INGRESE EL MONTO A CONSIGNAR: "))
    if(consignar > 0):
        accionconsig = int(input("ACCION REALIZADA CON EXITO\n\
                        DESEA VER SU NUEVO SALDO?\n\
                        1.-SI \n\
                        2.-NO\n\
                        DIGITE AQUI SU ELECCION: "))
        if (accionconsig == 1):
            saldo_disponible = saldo_disponible + consignar
            print("==============================================")
            print("SU NUEVO SALDO ES", "$",saldo_disponible,)
            print("==============================================")
        else:
            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
  elif(accion == "3"):
    print("==============================================")
    print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)
    print("==============================================")

  elif(accion == "4"):
     print('=======================================')
     print('GRACIAS POR USAR NUESTROS SERVICIOS!\n\
           VUELVA PRONTO')
     print('=======================================')
     break
  else: 
    print("==========================================================================")
    print("  ACCION INCORRECTA, POR FAVOR VERIFIQUE SU ELECCION Y VUELVA A INTENTAR")
    print("==========================================================================")
