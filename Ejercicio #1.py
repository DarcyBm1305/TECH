S = input("Ingrese un carácter alfanumérico: ")
Numero_par = []  # Lista para almacenar los caracteres numéricos pares
Numero_impar = []  # Lista para almacenar los caracteres numéricos impares
mayusculas = []  # Lista para almacenar las letras mayúsculas
minusculas = []  # Lista para almacenar las letras minúsculas
tamaño_Vector = len(S)  # Obtiene la longitud de la cadena ingresada
if 0 <= tamaño_Vector <= 1000:  # Verifica que la longitud esté en el rango válido
    for n in S:
        if n.isdigit():  # Verifica si el caracter es numérico
            if int(n) % 2 == 0:
             Numero_par.append(n) #Verifica si el caracter es numérico es par
            else:
               Numero_impar.append(n) #Verifica si el caracter es numérico es par
        elif n.isupper():  # Verifica si el caracter es una letra mayúscula
            mayusculas.append(n)  # Agrega el caracter a la lista de mayúsculas
        elif n.islower():  # Verifica si el caracter es una letra minúscula
            minusculas.append(n)  # Agrega el caracter a la lista de minúsculas
    resultado = "".join(sorted(minusculas) + sorted(mayusculas) + sorted(Numero_impar) + sorted(Numero_par))  # Concatena los resultados
    print(resultado)  # Imprime el resultado final
else:
    print("Caracter completo no admitido, Siga intentando :)")  # Imprime un mensaje de error si la longitud es inválida
