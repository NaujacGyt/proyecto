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

usuario.append([])
usuario[3].append("11203")
usuario[3].append("1234")
usuario[3].append("Mariana Pajon")
usuario[3].append(20000)

usuario.append([])
usuario[4].append("21565")
usuario[4].append("7895")
usuario[4].append("Cristobal Colon")
usuario[4].append(20000)
#usuario = [ ["45235", "1245", "Pepito Perez", 20000], ["78455", "3648", "Jaimito Cartero", 5000]            ]
action = 0
print("===================================\n\
BIENVENIDO A SU CAJERO AUTOMATICO\n\
===================================")
#sesion = 0
#contraseña = 0
passing = "NO"
saldo_disponible = 0
nombre = 0
sesion= 0
contraseña = 0
posi = 0
#contraseña = input("ingrese su contraseña:")
sesioninicial = True
while sesioninicial:
         
       #sesion = input("INGRESE SU NUMERO DE CUENTA: ")
                 
         if( passing == "NO"):
           sesion = input("INGRESE SU NUMERO DE CUENTA: ")
           existecuenta = False

           for i in range(len(usuario)):
                               
               if usuario[i][0] == sesion:
                     existecuenta = True                     
                     while True:
                        contraseña = input("ingrese su contraseña:")
                        #for i in range(len(usuario)):
                        if usuario [i] [1] == contraseña:
                                print("==============================================")
                                print("BIENVENIDO SR(A)", " ", usuario [i][2])
                                print("==============================================")
                                passing = "YES"
                                sesion = usuario [i] [0]
                                nombre = usuario [i] [2]
                                saldo_disponible = usuario [i] [3]
                                posi = i
                                break
        
    
                        else:
                             print("==============================================")
                             print("clave incorrecta vuelva a intentar")
                             print("==============================================")

               
               
                  
           if( existecuenta == False):
             print("==============================================")
             print("ERROR CUENTA BANCARIA NO EXISTE",  )
             print("==============================================")
                  
                 
         else:#(passing== "YES"):
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
                     saldo_disponible = saldo_disponible - retirar
                     print("============================================")
                     print("         ACCION REALIZADA CON ÉXITO         ")
                     print("============================================")
                     actionret = int(input("DESEA VER SU NUEVO SALDO?\n\
                            1.-SI \n\
                            2.-NO\n\
                            DIGITE AQUI SU ELECCION: "))
                     
                     if (actionret == 1):
                          
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
                
                 consignar = input("INGRESE EL MONTO A CONSIGNAR: ")
                 
                 if (consignar == int):
                     print("123")

                 elif(consignar > 0):
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
                 usuario[posi] [3] = saldo_disponible

                 
                 print('=======================================')
                 print("GRACIAS POR USAR NUESTROS SERVICIOS")
                 print("VUELVA PRONTO SR(A)", nombre )
                 print('=======================================')
                 passing = "NO"
             else:
                 print("==========================================================================")
                 print("  ACCION INCORRECTA, POR FAVOR VERIFIQUE SU ELECCION Y VUELVA A INTENTAR")
                 print("==========================================================================")  
         
          
                
       
