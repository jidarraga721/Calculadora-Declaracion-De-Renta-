import Logica_calculadora
try:
    print("Este progrma permite caluclar la declaracion de renta")
    ingreso_bruto= int(input("Ingrese sus ingresos"))
    Aportes_ley= int(input("Ingrese sus Aportes"))
    Deducciones= int(input("Ingrese sus deducciones"))


    Renta_liquida=Logica_calculadora.cal_entradas(ingreso_bruto, Aportes_ley, Deducciones)
    Beneficio_real=Logica_calculadora.cal_entradas(ingreso_bruto, Aportes_ley, Deducciones)
    Limite_legal=Logica_calculadora.cal_entradas(ingreso_bruto, Aportes_ley, Deducciones)
    Total=Logica_calculadora.cal_entradas(ingreso_bruto, Aportes_ley, Deducciones)

    print(f"la renta liquida tiene un valor de: {Renta_liquida[0]}")
    print(f"El beneficio real tiene un valor de: {Beneficio_real[1]}")
    print(f"El limite legal tiene un valor de: {Limite_legal[2]}")
    print(f"El volor total de impuestos a pagar es:  {Total[3]}")         

except Exception as err:
    print(f"Error: {err}")                                                                                                                 
