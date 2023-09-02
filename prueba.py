
password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
elif (password != 'miClaveSegura'):
    print('Tu contraseña es muy corta e insegura.')
    print("Además, es incorrecta (por supuesto).")