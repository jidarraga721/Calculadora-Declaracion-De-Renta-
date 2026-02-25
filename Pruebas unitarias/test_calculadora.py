class ingreso_invalido( Exception):
    pass

class Aportes_fuera_rango( Exception):
    pass

class ingreso_0( Exception):
    pass


class Deduccion_fuera_rango( Exception):
    pass


class Aportes_obligatorios( Exception):
    pass

def cal_entradas(ingreso_bruto, Aportes_ley,Deducciones):
    """
    Calcula los impustos a pagar de una declaracion de renta
    Ingreso_bruto: ingreso total que gan el usuario
    Aportes_ley: Descuentos obligatorios exigidos por el estado
    Deducciones: Gastos especificos que el usuario ya tiene o inversiones qeu hace para bajar legalmente la base de sus impuestos 
    """

    if ingreso_bruto < 0:
        raise ingreso_invalido("El valor del ingreso Bruto debe ser mayor que cero")
    
    if Aportes_ley > ingreso_bruto:
        raise Aportes_fuera_rango("Los aportes de ley no pueden ser mayores al ingreso bruto")
    
    if ingreso_bruto == 0:
        raise ingreso_0("El valor del ingreso Bruto debe ser mayor que cero")
    
    if Deducciones > (ingreso_bruto-Aportes_ley):
        raise Deduccion_fuera_rango("Las deducciones estan fuera de rango")
    
    if ingreso_bruto > 0 and Aportes_ley == 0:
        raise Aportes_obligatorios("Aportes de ley obligatorios faltantes")
    
    Renta_liquida = ingreso_bruto - Aportes_ley
    Beneficio_real = Deducciones + ((Renta_liquida- Deducciones)*0.25)
    Limite_legal = Renta_liquida *0.40

    if Beneficio_real > Limite_legal:
        Total = Renta_liquida - Limite_legal
        
    elif Beneficio_real <= Limite_legal:
        Total = Renta_liquida - Beneficio_real

    return Renta_liquida, Beneficio_real, Limite_legal, Total
