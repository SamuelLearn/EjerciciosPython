
def user (u):

    if len(u) < 6 :
        return 'invalido'

    elif len(u) > 12:
        return 'invalido'

    elif not u.isalnum():
        return 'el username debe solo contener caracteres alfanumericos'

    else:
        return True

usuario = raw_input ('nombre de usuario: ')
print user(usuario)

