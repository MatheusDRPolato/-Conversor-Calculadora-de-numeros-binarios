#Conversor/Calculadora de numeros binarios

#INCIO
print("==========Conversor/Calculadora de Binarios==========")
print("Digite 1 para Converter")
print("Digite 2 para Calcular Binarios")
b = int(input("Digito:"))

#VARIAVEL DE DECIMAL
if b == 1:
    print("==========Conversor==========")
    print("Inicie com numero decimal")
    a = int(input("Seu numero:"))

#VARIAVEL DE DIGITO
    print("Digite 1 para obter a resposta em BINARIO")
    print("Digite 2 para obter a resposta em OCTAL")
    print("Digite 3 para obter a resposta em HEXADECIMAL")
    digito = int(input("Digito:"))

#CONVERSÃO DE BINARIO,OCTAL,HEXA
    if digito == 1:
        b = bin(a).replace("0b", "")
        print(f"{a} convertido para binario é igual a {b}")
    elif digito == 2:
        b = oct(a).replace("0o", "")
        print(f"{a} convertido para octal é igual a {b}")
    elif digito == 3:
        b = hex(a).replace("0x", "")
        print(f"{a} convertido para hexadecimal é igual a {b}")
    else:
        print("Erro, tente novamente!")

#CALCULADORA DE BINARIOS
#VARIAVEL DO NUMERO 1,2 EM DECIMAL
if b == 2:
    print("==========Calculadora de Binarios==========")
    print("Inicie o numero em decimal!!")
    n1 = int(input("Digite o seu primeiro numero:"))
    n2 = int(input("Digite o seu segundo numero:"))

#VARIAVEL PARA DIGITO , ESCOLHER ENTRE BINARIO,OCTAL,HEXADECIMAL
    print("Digite 1 para obter a resposta em BINARIO")
    print("Digite 2 para obter a resposta em OCTAL")
    print("Digite 3 para obter a resposta em HEXADECIMAL")
    x = int(input("Digito:"))

#VARIAVEL PARA DIGITO , ESCOLHER SE DESEJA SOMAR,SUBTRAIR,DIVIDIR,MULTIPLICAR
    print("Digite 1 para Somar")
    print("Digite 2 para Subtrair")
    print("Digite 3 para Dividir")
    print("Digite 4 para Multiplicar")
    o = int(input("Digito:"))

#VARIAVEL DE CONTAS /BIN-BINARIO/HEX-HEXADECIMAL/OCT-OCTAL/ VOCE INTRODUZ O NUMERO EM DECIMAL E O PROPRIO PYTHON CONVERTE PARA A BASE DESEJADA
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
#Codigo feito no dia 14/05/2022 , pelo estudante de Ciencias da Computação - 1ºSemestre - UNICSUL ©Matheus Dos Reis Polato 
