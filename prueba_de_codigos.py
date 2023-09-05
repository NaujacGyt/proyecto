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
#sesion = 0
#contraseña = 0
passing = "NO"

saldo_disponible = 0

nombre = 0
sesion = input("INGRESE SU NUMERO DE CUENTA: ") 
contraseña = input("ingrese su contraseña:")

while True:
       #sesion = input("INGRESE SU NUMERO DE CUENTA: ")
                 
         if( passing == "NO"):
          
           for i in range(len(usuario)):
               if usuario[i] == sesion and usuario [i] == contraseña:
                     print(usuario[i][i],"bienvenido")
"""                     while True:
                        contraseña = input("ingrese su contraseña:")
                        for i in range(len(usuario)):
                            if usuario [i] [i] == contraseña:
                                print("==============================================")
                                print("BIENVENIDO SR(A)", " ", usuario [i][2])
                                print("==============================================")
                                passing = "YES"
                                sesion = usuario [0] [0]
                                nombre = usuario [0] [2]
                                saldo_disponible = usuario [0] [3]
                                break
        
    
                        else:
                             print("==============================================")
                             print("clave incorrecta vuelva a intentar")
                             print("==============================================")

           
               else:
                print("==============================================")
                print("ERROR CUENTA BANCARIA NO EXISTE",  )
                print("==============================================")"""