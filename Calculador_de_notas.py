##Marco Cardenas ##
print("****************************************")
print("************  VALIDADOR  ***************")
print("************  DE  NOTAS  ***************")
print("****************************************")

nombre=input("Hola, por favor ingresa tu nombre: \n")
#Se asigna un bucle while para el ingreso de datos.
while True: 
    try: #El try es para controlar la posibilidad de un error tras el mal ingreso de los datos en consola
        calificacion = float(input("Ingrese una calificacion de (0 a 100)\n"))
        if 0 <= calificacion <= 100:
            break   
        else:
            print("La calificacion debe estar entre 0 - 100")
    except ValueError:
        print("Entrada no válida. Ingrese un número.") 

# Condicionales para determinar estado
if calificacion >= 90: #Si es mayor a 90
    print("Felicidades, has aprobado con exito!!!😁")
elif calificacion >= 60: #Si es mayor o igual a 60
    print("Aprobado.🙂")
else: #En caso de que la nota sea menor a 60 automaticamente sale de las condiciones.
    print("Lastimosamente has reprobado.😥")

# Ingreso de calificaciones para hacer una lista 
entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
calificaciones = [ float(x.strip()) for x in entrada.split(',')] #Se le hacess una asignacion a la variable 'calificaciones'

# Ingreso del valor específico para comparación
valor_comparar = float(input("Ingrese un valor para comparar: "))
suma = 0
for nota in calificaciones: # Cálculo del promedio con un ciclo for
    suma += nota
promedio = suma / len(calificaciones)
print(f"El promedio de tus notas es: {promedio:.2f}")

# Verificación y conteo de una calificación específica usando for, break y continue
valor_buscar = float(input(f"{nombre}, ingresa una calificación específica a buscar: "))
encontrado = False
contador_especifico = 0

for nota in calificaciones: #Con un bucle for para encontrar las califiaciones que deseamos
    if nota != valor_buscar:
        continue
    if not encontrado:
        print(f"La calificación {valor_buscar} está en la lista.")
        encontrado = True
        # Solo mostrar este mensaje una vez, luego seguir contando
    contador_especifico += 1
#Condicionales para hacer la busqueda del valor de la nota y cuantas veces se repetió
if contador_especifico > 0:
    print(f"La calificación {valor_buscar} aparece {contador_especifico} veces.😄")
else:
    print(f"La calificación {valor_buscar} no aparece en la lista.😟")

print("Muchas gracias!!")



