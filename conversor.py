print("==========Conversor/Calculadora de Binarios==========")
print("Digite 1 para Converter Binario")
print("Digite 2 para Calcular Binarios")
b = int(input("Digito:"))
if b == 1:
    print("==========Conversor==========")
    a = int(input("Seu numero é Decimal/Binario/Hexadecimal/Octal?"))
    digito = int(input("Digito 1 - Binario / Digito 2- Octal / Digit0 3 - Hexadecimal"))
    if digito == 1:
        b = bin(a)
        print(f"{a} convertido para binario é igual a {b}")
    elif digito == 2:
        b = oct(a)
        print(f"{a} convertido para octal é igual a {b}")
    elif digito == 3:
        b = hex(a)
        print(f"{a} convertido para octal é igual a {b}")
    else:
        print("Erro, tente novamente!")




