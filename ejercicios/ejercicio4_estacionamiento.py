''' 
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción. 
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y 
muestra el importe a cobrar. 
''' 
# PROBLEMA 
# Se calcula el importe a cobrar por el tiempo de estancia en el estacionamiento.

# ENTRADAS
# nombre_variable : tipo, unidad, rango válido.
# tiempo_estancia : float, minutos, [0, ∞)


# SALIDAS
# nombre_variable : tipo, unidad, formato en que se muestra.
# importe : float, pesos, [0, 150], 2 decimales


# REGLAS Y SUPUESTOS
# - Valores fijos del problema (tarifas, porcentajes, topes).
# - Límites exactos de cada condición.
# - Regla de redondeo.
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió.

# ALGORITMO
# 1. Leer tiempo_estancia
# 2. Si tiempo_estancia <= 60: 
#       importe = 20
# 3. En caso contrario: 
#       importe = 20 + (tiempo_estancia - 60) / 60 * 15
# 4. Mostrar importe

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# 45 -> 20.0
# 60 -> 20.0
# 61 -> 32.5
# 150 -> 50.0
# 600 -> 150.0

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerTiempoEstancia() -> tiempo_estancia : lee el tiempo de estancia en minutos.
# calcularImporte(tiempo_estancia) -> importe : calcula el importe a cobrar.
# mostrarResultado(importe) : muestra el importe a cobrar.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerTiempoEstancia():
    tiempo_estancia = float(input("Ingrese el tiempo de estancia en minutos: "))
    return tiempo_estancia

def calcularImporte(tiempo_estancia):
    if tiempo_estancia <= 60:
        importe = 20
    else:
        importe = 20 + (tiempo_estancia - 60) / 60 * 15
    return importe

def mostrarResultado(importe):
    print("El importe a cobrar es: ${:.2f}".format(importe))
