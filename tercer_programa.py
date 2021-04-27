#1. Crear un nuevo repositorio
#2. Tomar de base el la tarea de la clase 2
#3. Si es menor de edad, vamos a venderle juguetes
#3.1: preguntarle si es electrónico, color, camina
#4. Si es mayor de edad, vamos a venderle ropa
#4.1: preguntarle si es camisa o pantalon, color y el talle
#5. Si es jubilado vamos a venderle pasajes
#5.1 Preguntarle si quiere viajar a Federación, Cataratas o Santa Teresita
#Mostrar por pantalla los datos de la persona y el producto seleccionado


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
            print(
            "El valor ingresado no es un número, por favor ingrese un número")

    def menor_de_edad():
        print('Seleccione el juguete a comprar:')
        electronico = input('Es electronico?')
        color = input('De qué color?')
        camina = input('El juguete camina?')
        return f'menor. El juguete es electronico: {electronico}, es de color: {color} y camina: {camina}'

    def adulto():
        print('Seleccione la ropa a comprar:')
        tipo = ['camisa', 'pantalon']
        seleccion = input(f'Desea comprar {tipo[0]} o {tipo[1]}?')
        color = input('Elija el color: ')
        talle = input('Ingrese su talle: ')
        return f'adulto. La ropa elegida es {seleccion}, el color es {color} y el talle es {talle}'

    def jubilado():
        lugar = ['Federacion', 'Cataratas', 'Santa Teresita' ]
        print(f'Seleccione a donde quiere viajar: {lugar[0]}, {lugar[1]}, {lugar[2]}')
        destino = input('Elija su destino: ')
        return f'jubilado. El destino elegido es {destino}'

    def edad_calculator():
        if edad < 18:
            return menor_de_edad()
        elif edad >= 18 and edad <= 64:
            return adulto()
        elif edad >= 65 and edad <= 120:
            return jubilado()


    print(f'Su nombre es {nombre} {apellido} y usted es {edad_calculator()}')
