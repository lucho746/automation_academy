'''
Hacer un programa en el que:
1-Se pregunte por el nombre de la persona
2-Se pregunte por el apellido de la persona
3-Se pregunte por la edad de la persona.
El formato de salida debe ser:
"Su nombre es: " + nombre + apellido + "y usted es " {condición de edad}
La condición de edad es:
1. Si es menor de 18 escribir menor
2. Si tiene entre 18 y 65 escribir mayor
3. Si tiene entre 65 y 120 escribir jubilado
4. Si tiene más escribir cadaver
'''

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
while True:
    try:
        edad = int(input('Ingrese su edad: '))
        break
    except ValueError:
        print("No es un numero")

def edad_calculator():
    if edad < 18:
        return('menor')
    elif edad >= 18 and edad <= 64:
        return('mayor')
    elif edad >= 65 and edad <= 120:
        return('jubilado')
    else:
        return('cadaver')

print(f'Su nombre es {nombre} {apellido} y usted es {edad_calculator()}')
