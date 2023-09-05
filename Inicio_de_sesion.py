#saldo_disponible = 1000 ##Saldo Disponible en la Cuenta
#saldo_disponible=int(saldo_disponible)

usuario = [[]]
usuario[0].append("123456")
usuario[0].append("1245")
usuario[0].append("Pepito Perez")
usuario[0].append(20000)

usuario.append([])
usuario[1].append("12345")
usuario[1].append("2356")
usuario[1].append("Andres Florez")
usuario[1].append(20000)

usuario.append([])
usuario[2].append("45678")
usuario[2].append("8956")
usuario[2].append("Jaimito Cartero")
usuario[2].append(20000)
#usuario = [ ["45235", "1245", "Pepito Perez", 20000], ["78455", "3648", "Jaimito Cartero", 5000]            ]


accion = 0
print("===================================\n\
BIENVENIDO A SU CAJERO AUTOMATICO\n\
===================================")
sesion = 0
contraseña = 0
passing = 0

saldo_disponible = 0

nombre = 0

while True:
       #sesion = input("INGRESE SU NUMERO DE CUENTA: ")
       while True:
          
         if( passing== 0):
           sesion = input("INGRESE SU NUMERO DE CUENTA: ") 
           if (sesion == usuario [0] [0] ):
              while True: 
                 contraseña = input("ingrese su contraseña:")
                 if(contraseña == usuario [0] [1]):
                      print("==============================================")
                      print("BIENVENIDO SR(A)", " ", usuario [0][2])
                      print("==============================================")
                      passing = "ok"
                      sesion = usuario [0] [0]
                      nombre = usuario [0] [2]
                      saldo_disponible = usuario [0] [3]
                      break
                 else:
                     print("==============================================")
                     print("clave incorrecta vuelva a intentar")
                     print("==============================================")
           elif (sesion == usuario [1] [0] ):
              while True: 
                 contraseña = input("ingrese su contraseña:")
                 if(contraseña == usuario [1] [1]):
                      print("==============================================")
                      print("BIENVENIDO SR(A)", " ", usuario [1][2])
                      print("==============================================")
                      passing = "ok"
                      sesion = usuario [1] [0]
                      break
                 else:
                     print("==============================================")
                     print("clave incorrecta vuelva a intentar")
                     print("==============================================")
           elif (sesion == usuario [2] [0] ):
              while True: 
                 contraseña = input("ingrese su contraseña:")
                 if(contraseña == usuario [2] [1]):
                      print("==============================================")
                      print("BIENVENIDO SR(A)", " ", usuario [2][2])
                      print("==============================================")
                      passing = "ok"
                      sesion = usuario [2] [0]
                      break
                 else:
                     print("==============================================")
                     print("clave incorrecta vuelva a intentar")
                     print("==============================================")

           
           else:
               print("==============================================")
               print("ERROR CUENTA BANCARIA NO EXISTE",  )
               print("==============================================")
               break
               
        #numero de sesion
        
         elif(passing== "ok"):
             action = input("QUE ACCION DESEA REALIZAR? \n\
                1.-RETIRAR \n\
                2.-CONSIGNAR \n\
                3.-TRANSFERIR FONDOS\n\
                4.-CONSULTAR SALDO \n\
                5.-SALIR \n\
                DIGITE AQUI SU ELECCION: ")
          
             if (action =="1"):
                 retirar = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
                 if (retirar <= saldo_disponible):
                     actionret = int(input("ACCION REALIZADA CON EXITO\n\
                             DESEA VER SU NUEVO SALDO?\n\
                            1.-SI \n\
                            2.-NO\n\
                            DIGITE AQUI SU ELECCION: "))
                     
                     if (actionret == 1):
                          saldo_disponible = saldo_disponible - retirar
                          print("==============================================")
                          print("SU NUEVO SALDO ES", "$",saldo_disponible,)
                          print("==============================================")
                     else:
                         print("==============================================")
                         print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                         print("==============================================")

                 elif(retirar > saldo_disponible):
                     print("==============================================")
                     print("SALDO INSUFICIENTE")
                     print("==============================================")
                     error=int((input("DESEA VERIFICAR SU SALDO?\n\
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
                     print("          ERROR ACCION NO VALIDA              ")
                     print("==============================================")
                
             elif(action == "2"):
                
                 consignar = int(input("INGRESE EL MONTO A CONSIGNAR: "))
                 if(consignar > 0):
                     saldo_disponible = saldo_disponible + consignar
                     print("==============================================")
                     print("        ACCION REALIZADA CON EXITO            ")
                     print("==============================================")
                     accionconsig = int(input("DESEA VER SU NUEVO SALDO?\n\
                         1.-SI \n\
                         2.-NO\n\
                         DIGITE AQUI SU ELECCION: "))
                     if (accionconsig == 1):
                         print("==============================================")
                         print("SU NUEVO SALDO ES", "$",saldo_disponible,)
                         print("==============================================")
                     else:
                         print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                 else:
                     print("==============================================")
                     print("          ERROR ACCION NO VALIDA              ")
                     print("==============================================")

             elif(action == "3"):
                print("==============================================")
                print("   ACCION NO DISPONIBLE POR EL MOMENTO        ")
                print("==============================================")
             elif(action == "4"):
                 print("==============================================")
                 print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)
                 print("==============================================")
             elif(action == "5"):
                 print('=======================================')
                 print("GRACIAS POR USAR NUESTROS SERVICIOS")
                 print("VUELVA PRONTO")
                 print('=======================================')
                 break
         else: 
             print("==========================================================================")
             print("  ACCION INCORRECTA, POR FAVOR VERIFIQUE SU ELECCION Y VUELVA A INTENTAR")
             print("==========================================================================")
           
          
                
       
