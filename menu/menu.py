from ejercicios.ejercicio1_luz import leerConsumo, calcularImporte, mostrarResultado
from ejercicios.ejercicio2_calificacion import leerParciales, calcularCalificacionFinal, mostrarResultado
from ejercicios.ejercicio3_compra import leerCompra, calcularTotal, mostrarTicket
from ejercicios.ejercicio4_estacionamiento import leerTiempoEstancia, calcularImporte, mostrarResultado
 
def menu_principal(): 
    while True: 
        print("Seleccione un ejercicio:") 
        print("1. Ejercicio 1 - Luz") 
        print("2. Ejercicio 2 - Calificación") 
        print("3. Ejercicio 3 - Compra") 
        print("4. Ejercicio 4 - Estacionamiento") 
        print("5. Salir") 
        opcion = input("Ingrese el número del ejercicio a ejecutar: ") 
 
        if opcion == "1": 
            consumo=leerConsumo()
            importe_recibo=calcularImporte(consumo)
            mostrarResultado(importe_recibo)
        elif opcion == "2": 
            parcial1, parcial2, parcial3 = leerParciales()
            calificacion_final, aprobo = calcularCalificacionFinal(parcial1, parcial2, parcial3)
            mostrarResultado(calificacion_final, aprobo)
             
        elif opcion == "3": 
            compra = leerCompra()
            total = calcularTotal(compra)
            mostrarTicket(*total)
        elif opcion == "4": 
            tiempo_estancia = leerTiempoEstancia()
            importe = calcularImporte(tiempo_estancia)
            mostrarResultado(importe)
        elif opcion == "5": 
            print("Saliendo del programa.") 
            break 
        else: 
            print("Opción inválida. Por favor, intente de nuevo.")
     
 
 

