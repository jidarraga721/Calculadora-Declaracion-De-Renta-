def cal_entradas(ingreso_bruto, Aportes_ley,Deducciones):
    """
    Calcula los impustos a pagar de una declaracion de renta
    Ingreso_bruto: ingreso total que gan el usuario
    Aportes_ley: Descuentos obligatorios exigidos por el estado
    Deducciones: Gastos especificos que el usuario ya tiene o inversiones qeu hace para bajar legalmente la base de sus impuestos 
    """
    Renta_liquida = ingreso_bruto - Aportes_ley
    Beneficio_real = Deducciones + ((Renta_liquida- Deducciones)*0.25)
    Limite_legal = Renta_liquida *0.40

    if Beneficio_real > Limite_legal:
        Total = Renta_liquida - Limite_legal
        
    elif Beneficio_real <= Limite_legal:
        Total = Renta_liquida - Beneficio_real

    return Renta_liquida, Beneficio_real, Limite_legal, Total
