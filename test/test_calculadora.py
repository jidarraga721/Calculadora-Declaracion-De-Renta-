import unittest 
import sys
sys.path.append( 'src')
from model import Logica_calculadora

class TestCalculadora(unittest.TestCase):
    """Conjunto de pruebas unitarias para la lógica de cálculo de renta."""

    def test_normal_uno(self): 
        ingreso_bruto = 5000000
        aportes_ley = 400000
        deducciones = 0 

        renta_liquida, beneficio_real, limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(renta_liquida, 4600000)
        self.assertEqual(beneficio_real, 1150000)
        self.assertEqual(limite_legal, 1840000)
        self.assertEqual(total, 3450000)

    def test_normal_dos(self): 

        ingreso_bruto = 8000000
        aportes_ley = 640000
        deducciones = 600000

        renta_liquida, beneficio_real, limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(renta_liquida, 7360000)
        self.assertEqual(beneficio_real, 2290000)
        self.assertEqual(limite_legal, 2944000)
        self.assertEqual(total, 5070000)

    def test_normal_tres(self): 
        ingreso_bruto = 12000000
        aportes_ley = 960000
        deducciones = 500000

        renta_liquida, beneficio_real, limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
        
        self.assertEqual(renta_liquida, 11040000)
        self.assertEqual(beneficio_real, 3135000)
        self.assertEqual(limite_legal, 4416000)
        self.assertEqual(total, 7905000)

    def test_extra_uno(self): 
        ingreso_bruto = 1300000
        aportes_ley = 104000
        deducciones = 0

        renta_liquida, beneficio_real, limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(renta_liquida, 1196000)
        self.assertEqual(beneficio_real, 299000)
        self.assertEqual(limite_legal, 478400)
        self.assertEqual(total, 897000)

    def test_extra_dos(self): 
        ingreso_bruto = 20000000
        aportes_ley = 1600000
        deducciones = 12000000

        renta_liquida, beneficio_real, limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(renta_liquida, 18400000)
        self.assertEqual(beneficio_real, 13600000)
        self.assertEqual(limite_legal, 7360000)
        self.assertEqual(total, 11040000)
    
    def test_extra_tres(self): 
        ingreso_bruto = 3500000
        aportes_ley = 280000
        deducciones = 0

        renta_liquida, beneficio_real, limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(renta_liquida, 3220000)
        self.assertEqual(beneficio_real, 805000)
        self.assertEqual(limite_legal, 1288000)
        self.assertEqual(total, 2415000)

    def test_ingreso_negativo(self):
        """Asegura que se lance IngresoInvalido si el sueldo es menor a cero."""
        ingreso_bruto = -50000000 
        aportes_ley = 400000
        deducciones = 0

        with self.assertRaises(Logica_calculadora.IngresoInvalido):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_aporte_ilogico(self):
        """Asegura que los aportes de ley no puedan ser superiores al ingreso bruto."""
        ingreso_bruto = 1000000
        aportes_ley = 1500000 
        deducciones = 0

        with self.assertRaises(Logica_calculadora.AportesInvalidos):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_ingreso_cero(self):
        """Valida que no se procesen declaraciones con ingreso bruto de cero."""
        ingreso_bruto = 0 
        aportes_ley = 0
        deducciones = 0
    
        with self.assertRaises(Logica_calculadora.IngresoCero):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_deducciones_mayores(self):
        """Valida que las deducciones no superen el dinero disponible tras aportes."""
        ingreso_bruto = 2000000
        aportes_ley = 160000
        deducciones = 50000000

        with self.assertRaises(Logica_calculadora.DeduccionFueraRango):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_aportes_oblogatorios(self):
        """Verifica la obligatoriedad de aportes de ley para asalariados con ingresos."""
        ingreso_bruto = 4000000
        aportes_ley = 0
        deducciones = 0
    
        with self.assertRaises(Logica_calculadora.AportesObligatorios):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones) 

if __name__ == "__main__":
    unittest.main()