''' 
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó.  
''' 
# PROBLEMA  
# La calificación final de una materia y si el alumno aprobó.


# ENTRADAS
# nombre_variable : tipo, unidad, rango válido.
# parcial1 : float, puntos, [0, 100]
# parcial2 : float, puntos, [0, 100]
# parcial3 : float, puntos, [0, 100]
# SALIDAS
# nombre_variable : tipo, unidad, formato en que se muestra.
# calificacion_final : float, puntos, [0, 100], 1 decimal
# aprobo : bool, , {True, False}

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
 
# ALGORITMO 
# 1. Leer parcial1, parcial2, parcial3
# 2. Si parcial1 < 50 o parcial2 < 50 o parcial3 < 50: 
#       calificacion_final = 0
#       aprobo = False
# 3. En caso contrario: 
#       calificacion_final = parcial1 * 0.3 + parcial2 * 0.3 + parcial3 * 0.4
#       aprobo = calificacion_final >= 70
# 4. Mostrar calificacion_final y aprobo

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# 80, 70, 90 -> 74.0, True
# 70, 70, 70 -> 70.0, True
# 100, 100, 40 -> 0.0, False
# 69, 70, 70 -> 78.0, True
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerParciales() -> (parcial1, parcial2, parcial3) : lee las calificaciones de los tres parciales.
# calcularCalificacionFinal(parcial1, parcial2, parcial3) -> (calificacion_final, aprobo) : calcula la calificación final y si el alumno aprobó.
# mostrarResultado(calificacion_final, aprobo) : muestra la calificación final y si el alumno aprobó.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerParciales():
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
    return (parcial1, parcial2, parcial3)

def calcularCalificacionFinal(parcial1, parcial2, parcial3):
    if parcial1 < 50 or parcial2 < 50 or parcial3 < 50:
        calificacion_final = 0
        aprobo = False
    else:
        calificacion_final = parcial1 * 0.3 + parcial2 * 0.3 + parcial3 * 0.4
        aprobo = calificacion_final >= 70
    return (calificacion_final, aprobo)

def mostrarResultado(calificacion_final, aprobo):
    print("La calificación final es: {:.1f}".format(calificacion_final))
    print("¿Aprobó? {}".format("Sí" if aprobo else "No"))
