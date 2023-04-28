def validate_email(s):
    letras_minusculas = ch[(x) for x in range(ord('a'), ord('z') + 1)]
    simbolos_permitidos= [i for i in string if i not in letras_minusculas]

    if (simbolos_permitidos == ['@','.']):
        return True
    else:
        return False