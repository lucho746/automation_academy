'''
1. Crear un nuevo repositorio
2. Tomar de base el programa de la clase pasada
3. Vamos a modificar el programa para que solo tome como válidos números entre 1 y 120
 (si pone un número entre -inf y 0 o 121 a inf debe volver a preguntar)
3. Al inicio del programa preguntar cuantas personas registrar
4. Hacer que el programa que se hizo se ejecute esas n veces que se pusieron en el punto 3
5. Subir el programa al repositorio creado.
'''

while True:
    try:
        personas = int(input('¿Cuántas personas se van a registrar?: '))
        break
    except ValueError:
        print("El valor ingresado no es un número, por favor ingrese un número")

for i in range(personas):
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    while True:
        try:
            edad = int(input('Ingrese su edad: '))
            if edad >=1 and edad <=120:
                break
            else:
                print("Por favor ingrese una edad entre 1 y 120")
        except ValueError:
            print("El valor ingresado no es un número, por favor ingrese un número")


    def edad_calculator():
        if edad < 18:
            return('menor')
        elif edad >= 18 and edad <= 64:
            return('mayor')
        elif edad >= 65 and edad <= 120:
            return('jubilado')

    print(f'Su nombre es {nombre} {apellido} y usted es {edad_calculator()}')
