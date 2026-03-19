import src.model.Logica_calculadora as Logica_calculadora
"""Script principal para la interacción con el usuario y el cálculo de declaración de renta."""

try:
    """Ejecuta la interfaz de consola para capturar datos y mostrar los resultados del cálculo tributario."""
    print("Este progrma permite caluclar la declaracion de renta")

    # Captura de datos de entrada desde la consola
    ingreso_bruto= int(input("Ingrese sus ingresos: "))
    aportes_ley= int(input("Ingrese sus aportes: "))
    deducciones= int(input("Ingrese sus deducciones: "))

    # Llamado a la lógica de cálculo (Se obtiene la tupla completa en una sola ejecución)
    renta_liquida, beneficio_real, limite_legal , total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
    
    # Desglose de resultados para el usuario
    print(f"la renta liquida tiene un valor de: {renta_liquida[0]}")
    print(f"El beneficio real tiene un valor de: {beneficio_real[1]}")
    print(f"El limite legal tiene un valor de: {limite_legal[2]}")
    print(f"El volor total de impuestos a pagar es: {total[3]}")         

except Exception as err:
    """Captura y muestra cualquier error de validación o ejecución ocurrido durante el proceso."""
    print(f"Error: {err}")                                                                                                                 


    #python -m src.view.Consola