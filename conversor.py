print("Conversor de binarios")
a = int(input("Digite um numero inteiro:"))
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
