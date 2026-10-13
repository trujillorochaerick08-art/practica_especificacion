''' 
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes.  
''' 
# PROBLEMA 
# El importe del recibido a partir del consumo del mes 

# ENTRADAS
# consumo : float, kWh, >= 0
# costo_hora : float, $, > 0

# SALIDAS
# importe_recibo : float, $, >= 0

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
 
# ALGORITMO 
# 1. Leer consumo  
# 2. Si consumo <= 150: 
#       importe_recibo = consumo * 1.00
# 3. En caso contrario, si consumo <= 280:
#       importe_recibo = consumo * 1.50
# 4. En caso contrario:
#       importe_recibo = consumo * 3.00
# 4. Mostrar resultado
 
# CASOS DE PRUEBA 
#caso 1: consumo = 100 -> importe_recibo = 100.00
#caso 2: consumo = 150 -> importe_recibo = 300.00
#caso 3: consumo = 200 -> importe_recibo = 300.00
#caso 4: consumo = 280 -> importe_recibo = 420.00
#caso 5: consumo = 300 -> importe_recibo = 900.00

 
# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerConsumo() -> consumo : lee el consumo del mes en kWh.
# calcularImporte(consumo) -> importe_recibo : calcula el importe del recibo a partir del consumo.
# mostrarResultado(importe_recibo) : muestra el resultado.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerConsumo():
    consumo = float(input("Ingrese el consumo del mes en kWh: "))
    return consumo

def calcularImporte(consumo):
    if consumo <= 150:
        importe_recibo = consumo * 1.00
    elif consumo <= 280:
        importe_recibo = consumo * 1.50
    else:
        importe_recibo = consumo * 3.00
    return importe_recibo

def mostrarResultado(importe_recibo):
    print("El importe del recibo es: ${:.2f}".format(importe_recibo))
