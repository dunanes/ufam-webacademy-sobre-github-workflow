import re

print('\n**** insira um CPF completo (apenas números) ***\n')
print('\n**** insira um CPF completo (apenas números) ***\n')
print('\n**** insira um CPF completo (apenas números) ***\n')
print('\n**** insira um CPF completo (apenas números) ***\n')
print('\n**** insira um CPF completo (apenas números) ***\n')
print('\n**** insira um CPF completo (apenas números) ***\n')
print('\n**** insira um CPF completo (apenas números) ***\n')

valorvalorvalor = input('Digite o CPF: ') # receber entrada do CPF
entrada = re.findall("\d", valorvalorvalor) # remover caracteres NÃO numéricos

# validar quantidade de caracteres digitados
if len(valorvalorvalor) > 14 or len(entrada) < 11 or len(entrada) > 11:
    print('CPF INVÁLIDO')

# verificar se todos os dígitos são iguais
else:
    valid = 0
    for dig in range(0, 11):
        valid += int(entrada[dig])
        dig += 1
    if int(entrada[0]) == valid / 11:
        print("CPF INVÁLIDO")

    # rotina de cálculos do dígito verificador do CPF
    else:
        # verificação do 10º dígito verificador
        soma = 0
        count = 10
        for i in range(0, len(entrada)-2):
            soma = soma + (int(entrada[i])*count)
            i+=1
            count-=1
        dg1 = 11-(soma%11)
        if dg1 >= 10:
            dg1 = 0

        # verificação do 11º dígito verificador
        soma = 0
        count = 10
        for j in range(1, len(entrada)-1):
            soma = soma + (int(entrada[j])*count)
            j+=1
            count-=1
        dg2 = 11-(soma%11)
        if dg2 >= 10:
            dg2 = 0

        # mensagem ao usuário
        if int(entrada[9]) != dg1 or int(entrada[10]) != dg2:
            print("CPF NAO TA CERTO")
        else:
            print('*** CPF VÁLIDO ***')