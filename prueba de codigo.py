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

#sesion = 0
#contraseña = 0
passing = "NO"
saldo_disponible = 20000
nombre = 0
sesion= 0
contraseña = 0
posi = 0
#contraseña = input("ingrese su contraseña:")
sesioninicial = True
ingreso = True





actionver = True
while actionver:
    montotransf = int(input("INGRESE LA CANTIDAD QUE DESEA TRANSFERIR: "))

    if (montotransf <= saldo_disponible):
        print("==============================================")
        acciontransferir = input("INGRESE EL NUMERO DE CUENTA AL QUE DESEA TRANSFERIR:")
        cuenta_a_trasnferir = False
        
        for i in range(len(usuario)):

            if usuario[i][0] == acciontransferir:
                cuenta_a_trasnferir = True                     
                while True:
                    usuario2 = [i] [0]
                    print (usuario2)
                    actionver = False
                    break
                    
                
                    #if usuario [i] [0] == acciontransferir:
                            #print("==============================================")
                            #print("BIENVENIDO SR(A)", " ", usuario [i][2])
                            #print("==============================================")
                            #passing = "YES"
                            #sesion = usuario [i] [0]
                            #nombre = usuario [i] [2]
                            #saldo_disponible = usuario [i] [3]
                            #posi = i
                            #break
    elif(cuenta_a_trasnferir == False):
        print("==============================================")
        print("ERROR CUENTA BANCARIA NO EXISTE",  )
        print("==============================================")
    else:
        print("error no posee esa cantidad de dinero en su cuenta")
        validacion = int(input("desea ver su saldo disponible\n\
                            1.-SI\n\
                            2.-NO\n\
                            ingrese aqui su opcion: "))
        if validacion == 1:
            print("==============================================")
            print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)
            print("==============================================")
            actionver = False
            
            