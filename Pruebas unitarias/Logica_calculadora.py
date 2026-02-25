def cal_entradas(ingreso_bruto, Aportes_ley,Deducciones):
    """
    Calcula los impustos a pagar de una declaracion de renta
    Ingreso_bruto: ingreso total que gan el usuario
    Aportes_ley: Descuentos obligatorios exigidos por el estado
    Deducciones: Gastos especificos que el usuario ya tiene o inversiones qeu hace para bajar legalmente la base de sus impuestos 
    """

    if ingreso_bruto < 0:
        raise Exception("El valor del ingreso Bruto debe ser mayor que cero")
    
    if ingreso_bruto == 0:
        raise Exception("Debe tener ingresos")
    
    if Aportes_ley < 0:
        raise Exception("El valor de los aportes debe ser mayor que cero")
    
    if Deducciones < 0:
        raise Exception("El valor de las deducciones debe ser mayor que cero")
    
    if Deducciones > (ingreso_bruto-Aportes_ley):
        raise Exception("Las deducciones estan fuera de rango")
    
    if Aportes_ley > ingreso_bruto:
        raise Exception("Los aportes de ley no pueden ser mayores al ingreso bruto")
    
    if ingreso_bruto > 0 and Aportes_ley == 0:
        raise Exception("Aportes de ley obligatorios faltantes")
    
    Renta_liquida = ingreso_bruto - Aportes_ley
    Beneficio_real = Deducciones + ((Renta_liquida- Deducciones)*0.25)
    Limite_legal = Renta_liquida *0.40

    if Beneficio_real > Limite_legal:
        Total = Renta_liquida - Limite_legal
        
    elif Beneficio_real <= Limite_legal:
        Total = Renta_liquida - Beneficio_real

    return Renta_liquida, Beneficio_real, Limite_legal, Total
