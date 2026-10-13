''' 
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total.  
''' 
# PROBLEMA 
# Se calcula el total a pagar en una compra considerando descuentos e IVA.
 
# ENTRADAS 
# nombre_variable : tipo, unidad, rango válido.
# compra : float, pesos, [0, ∞)

# SALIDAS
# nombre_variable : tipo, unidad, formato en que se muestra.
# subtotal : float, pesos, [0, ∞), 2 decimales
# descuento : float, pesos, [0, ∞), 2 decimales
# iva : float, pesos, [0, ∞), 2 decimales
# total : float, pesos, [0, ∞), 2 decimales

# REGLAS Y SUPUESTOS
# - Valores fijos del problema (tarifas, porcentajes, topes).
# - Límites exactos de cada condición.
# - Regla de redondeo.
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió.

# ALGORITMO
# 1. Leer compra
# 2. Si compra >= 5000: 
#       subtotal = compra * 0.8
# 3. En caso contrario: 
#       subtotal = compra * 0.9
# 4. iva = subtotal * 0.16
#    total = subtotal + iva
# 5. Mostrar subtotal, descuento, iva y total

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# 500 -> 450.0, 50.0, 64.0, 514.0
# 900 -> 810.0, 90.0, 115.2, 925.2
# 1000 -> 800.0, 200.0, 96.0, 896.0
# 5000 -> 4000.0, 1000.0, 640.0, 4640.0

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerCompra() -> compra : lee el monto de la compra.
# calcularTotal(compra) -> (subtotal, descuento, iva, total) : calcula el total a pagar en una compra considerando descuentos e IVA.
# mostrarTicket(subtotal, descuento, iva, total) : muestra el ticket con subtotal, descuento, IVA y total.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerCompra():
    compra = float(input("Ingrese el monto de la compra: "))
    return compra

def calcularTotal(compra):
    if compra >= 5000:
        subtotal = compra * 0.8
        descuento = compra * 0.2
    else:
        subtotal = compra * 0.9
        descuento = compra * 0.1
    iva = subtotal * 0.16
    total = subtotal + iva
    return (subtotal, descuento, iva, total)

def mostrarTicket(subtotal, descuento, iva, total):
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Descuento: ${:.2f}".format(descuento))
    print("IVA: ${:.2f}".format(iva))
    print("Total: ${:.2f}".format(total))
