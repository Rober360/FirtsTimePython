n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
rest = n1 - n2
mult = n1 * n2
divi = n1 / n2

mensaje = f"""
Para los nuemeros {n1} y {n2},
la suma es :{suma},
la resta es: {rest},
la multiplicacion es: {mult}
la division es: {divi}"""

print(mensaje)
