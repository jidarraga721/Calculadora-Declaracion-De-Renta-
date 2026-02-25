import unittest 
import Logica_calculadora

class Test_calculadora(unittest.TestCase):
    def test_normal1(self): 
        ingreso_bruto = 5000000
        aportes_ley = 400000
        deducciones = 0 

        Renta_liquida, Beneficio_real, Limite_legal, Total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(Renta_liquida, 4600000)
        self.assertEqual(Beneficio_real, 1150000)
        self.assertEqual(Limite_legal, 1840000)
        self.assertEqual(Total, 3450000)

    def test_normal2(self): 
        ingreso_bruto = 8000000
        aportes_ley = 640000
        deducciones = 600000

        Renta_liquida, Beneficio_real, Limite_legal, Total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

        self.assertEqual(Renta_liquida, 7360000)
        self.assertEqual(Beneficio_real, 2290000)
        self.assertEqual(Limite_legal, 2944000)
        self.assertEqual(Total, 5070000)

    def test_normal3(self): 
        ingreso_bruto = 12000000
        aportes_ley = 960000
        deducciones = 500000

        Renta_liquida, Beneficio_real, Limite_legal, Total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
        self.assertEqual(Renta_liquida, 11040000)
        self.assertEqual(Beneficio_real, 3135000)
        self.assertEqual(Limite_legal, 4416000)
        self.assertEqual(Total, 7905000)

    def test_extra1(self): 
        ingreso_bruto = 1300000
        aportes_ley = 104000
        deducciones = 0

        Renta_liquida, Beneficio_real, Limite_legal, Total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
        self.assertEqual(Renta_liquida, 1196000)
        self.assertEqual(Beneficio_real, 299000)
        self.assertEqual(Limite_legal, 478400)
        self.assertEqual(Total, 897000)

    def test_extra2(self): 
        ingreso_bruto = 20000000
        aportes_ley = 1600000
        deducciones = 12000000

        Renta_liquida, Beneficio_real, Limite_legal, Total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
        self.assertEqual(Renta_liquida, 18400000)
        self.assertEqual(Beneficio_real, 13600000)
        self.assertEqual(Limite_legal, 7360000)
        self.assertEqual(Total, 11040000)
    
    def test_extra3(self): 
        ingreso_bruto = 3500000
        aportes_ley = 280000
        deducciones = 0

        Renta_liquida, Beneficio_real, Limite_legal, Total = Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
        self.assertEqual(Renta_liquida, 3220000)
        self.assertEqual(Beneficio_real, 805000)
        self.assertEqual(Limite_legal, 1288000)
        self.assertEqual(Total, 2415000)

    def test_error1(self):
        ingreso_bruto = -5000000
        aportes_ley = 400000
        deducciones = 0
    
        with self.assertRaises(Exception):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_error2(self):
        ingreso_bruto = 1000000
        aportes_ley = 1500000
        deducciones = 0
    
        with self.assertRaises(Exception):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_error3(self):
        ingreso_bruto = 0
        aportes_ley = 4000000
        deducciones = 250000
    
        with self.assertRaises(Exception):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)

    def test_error4(self):
        ingreso_bruto = 2000000
        aportes_ley = 160000
        deducciones = 50000000
    
        with self.assertRaises(Exception):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones)
    
    def test_error5(self):
        ingreso_bruto = 20000000
        aportes_ley = 0
        deducciones = 800000
    
        with self.assertRaises(Exception):
            Logica_calculadora.cal_entradas(ingreso_bruto, aportes_ley, deducciones) 


        

    
  
if __name__ == '__main__':
    unittest.main()
