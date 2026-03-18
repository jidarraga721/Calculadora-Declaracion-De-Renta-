class IngresoInvalido(Exception):
    pass
"""Se dispara cuando el ingreso es cero o negativo."""

class AportesInvalidos(Exception):
    pass
"""Se dispara cuando los aportes de ley superan los ingresos."""

class IngresoCero(Exception):
    pass
"""Se dispara cuando las deducciones superan la renta líquida."""

class DeduccionFueraRango(Exception):
    pass
"""Se dispara si un asalariado con ingresos no registra aportes de ley."""

class AportesObligatorios(Exception):
    pass
"""Se dispara si un asalariado con ingresos no registra aportes de ley."""


def cal_entradas(ingreso_bruto, aportes_ley,deducciones):
    """
    Esta función valida los montos de entrada y aplica la lógica de beneficios 
    tributarios, considerando el límite legal del 40% sobre la renta líquida.
    Ingreso_bruto: ingreso total que gana el usuario
    Aportes_ley: Descuentos obligatorios exigidos por el estado
    Deducciones: Gastos especificos que el usuario ya tiene o inversiones que hace para reducir legalmente la base de sus impuestos 
    """

    if ingreso_bruto < 0:
        raise IngresoInvalido("El valor del ingreso bruto debe ser mayor que cero")
    
    if aportes_ley > ingreso_bruto:
        raise AportesInvalidos("Los aportes de ley no pueden ser mayores al ingreso bruto")
    
    if ingreso_bruto == 0:
        raise IngresoCero("El usuario debe de tener ingresos")
    
    if deducciones > (ingreso_bruto-aportes_ley):
        raise DeduccionFueraRango("Las deducciones estan fuera de rango")
    
    if ingreso_bruto > 0 and aportes_ley == 0:
        raise AportesObligatorios("Aportes de ley obligatorios faltantes, todo asalariado debe aportar a salud y pension ")
    

    # Lógica de cálculo original
    renta_liquida = ingreso_bruto - aportes_ley
    beneficio_real = deducciones + ((renta_liquida- deducciones)*0.25)
    limite_legal = renta_liquida *0.40

    if beneficio_real > limite_legal:
        total = renta_liquida - limite_legal
        
    elif beneficio_real <= limite_legal:
        total = renta_liquida - beneficio_real

    return renta_liquida, beneficio_real, limite_legal, total
