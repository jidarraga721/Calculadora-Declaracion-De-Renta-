import unittest 
import Logica_calculadora

class Test_calculadora(unittest.TestCase):
    def test_normal1(self): 
        ingreso_bruto = 5000000
        aportes_ley = 400000
        deducciones = 0 

        Renta_liquida, Beneficio_real, Limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(Renta_liquida, 4600000)
        self.assertEqual(Beneficio_real, 1150000)
        self.assertEqual(Limite_legal, 1840000)
        self.assertEqual(total, 3450000)

    def test_normal2(self): 
        ingreso_bruto = 8000000
        aportes_ley = 640000
        deducciones = 600000

        Renta_liquida, Beneficio_real, Limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(Renta_liquida, 7360000)
        self.assertEqual(Beneficio_real, 2290000)
        self.assertEqual(Limite_legal, 2944000)
        self.assertEqual(total, 5070000)

    def test_normal3(self): 
        ingreso_bruto = 12000000
        aportes_ley = 960000
        deducciones = 500000

        Renta_liquida, Beneficio_real, Limite_legal, total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(Renta_liquida, 11040000)
        self.assertEqual(Beneficio_real, 3135000)
        self.assertEqual(Limite_legal, 4416000)
        self.assertEqual(total, 7905000)



  
if __name__ == '__main__':
    unittest.main()
