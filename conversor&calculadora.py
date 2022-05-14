print("==========Conversor/Calculadora de Binarios==========")
print("Digite 1 para Converter")
print("Digite 2 para Calcular Binarios")
b = int(input("Digito:"))

if b == 1:
    print("==========Conversor==========")
    print("Inicie com numero decimal")
    a = int(input("Seu numero:"))

    print("Digite 1 para obter a resposta em BINARIO")
    print("Digite 2 para obter a resposta em OCTAL")
    print("Digite 3 para obter a resposta em HEXADECIMAL")
    digito = int(input("Digito:"))

    if digito == 1:
        b = bin(a).replace("0b", "")
        print(f"{a} convertido para binario é igual a {b}")
    elif digito == 2:
        b = oct(a).replace("0o", "")
        print(f"{a} convertido para octal é igual a {b}")
    elif digito == 3:
        b = hex(a).replace("0x", "")
        print(f"{a} convertido para octal é igual a {b}")
    else:
        print("Erro, tente novamente!")

if b == 2:
    print("==========Calculadora de Binarios==========")
    print("Inicie o numero em decimal!!")
    n1 = int(input("Digite o seu primeiro numero:"))
    n2 = int(input("Digite o seu segundo numero:"))


    print("Digite 1 para obter a resposta em BINARIO")
    print("Digite 2 para obter a resposta em OCTAL")
    print("Digite 3 para obter a resposta em HEXADECIMAL")
    x = int(input("Digito:"))

    
    print("Digite 1 para Somar")
    print("Digite 2 para Subtrair")
    print("Digite 3 para Dividir")
    print("Digite 4 para Multiplicar")
    o = int(input("Digito:"))

    if x == 1 and o == 1:
        c = bin(n1 + n2).replace("0b", "")
        print(c)
    if x == 1 and o == 2:
        c = bin(n1 - n2).replace("0b", "")
        print(c)
    if x == 1 and o == 3:
        c = bin(n1 / n2).replace("0b", "")
        print(c)
    if x == 1 and o == 4:
        c = bin(n1 * n2).replace("0b", "")
        print(c)
        
    if x == 2 and o == 1:
        m = oct(n1 + n2).replace("0o", "")
        print(m)
    if x == 2 and o == 2:
        m = oct(n1 - n2).replace("0o", "")
        print(m)
    if x == 2 and o == 3:
        m = oct(n1 / n2).replace("0o", "")
        print(m)
    if x == 2 and o == 4:
        m = oct(n1 * n2).replace("0o", "")
        print(m)

    if x == 3 and o == 1:
        n = oct(n1 + n2).replace("0x", "")
        print(n)
    if x == 3 and o == 2:
        n = oct(n1 - n2).replace("0x", "")
        print(n)
    if x == 3 and o == 3:
        n = oct(n1 / n2).replace("0x", "")
        print(n)
    if x == 3 and o == 4:
        n = oct(n1 * n2).replace("0x", "")
        print(n)

    else:
        print("Erro, tente novamente!")     