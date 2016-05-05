#--coding:utf-8--
import re

def password(p):

    if len(p) < 8 :
        return 'la contraseña no es segura'

    elif re.search(r"A-Z", p):
        return 'la contraseña no es segura'

    elif re.search(r"a-z", p):
        return 'la contraseña no es segura'

    elif p.isspace():
        return 'la contraceña no puede tener espacios'

    elif not p.isalnum():
        return 'la contraseña debe poseer un caracter especial'


    else:
        return True

contra = raw_input ('contraseña: ')
print password(contra)

