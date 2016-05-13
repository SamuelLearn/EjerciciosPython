from validar import validar_usuario
from validar_password import password

usuario=raw_input ('ingrese el usuario: ')

clave=raw_input ('ingrese la clave: ')

if validar_usuario(usuario) == True and password(clave) == True:
    print 'datos correctos'

else:
    print 'datos incorrectos'

