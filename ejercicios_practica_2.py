# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    sumatoria = 0
    archivo = open(archivo, 'r')
    datos = list(csv.DictReader(archivo))

    for k in datos: #En este for recorre el archivo datos y recupera el valor de la clave "tornillos"
        sumatoria += int(k.get('tornillos')) #tranformando el valor en int para poder realizar la sumatoria del mismo

    archivo.close()
    print("La suma de las cantidades de tornillos es: ", sumatoria)

    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = open(archivo, 'r')
    datos = list(csv.DictReader(archivo))
    contador2 = 0
    contador3 = 0

    for k in datos:
        try:
            if k.get('ambientes') == '2':
                contador2 += 1
            elif k.get('ambientes') == '3':
                contador3 += 1
        except:
            if k.get('ambientes') == '' or k.get('ambientes') == ' ' or k.get('ambientes' == None):
                print("El dpto no especifica cantidad de ambientes")

    archivo.close()
    print("La cantidad de departamentos de 2 y 3 ambientes es: ", contador2, contador3, "respectivamente.")
'''En la función anterior uso try...except, pero a primera vista, al realizar la comparación sin transformar
el valor de k.get a int, sino que lo manejo como str durante todo el bucle, el programa no se rompe en ningún
momento, por lo que no hace uso del except. Lo dejo a consideración de los profesores.'''

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
