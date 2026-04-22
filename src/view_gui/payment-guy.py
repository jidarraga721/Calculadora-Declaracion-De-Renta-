from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")
#Importacion arreglada
from src.model.Logica_calculadora import Impuestos, CalculadoraImpuestos

class RentaApp(App):
    def build(self):

        self.title = "Calculadora del valor de la renta"
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        contenedor.add_widget(Label(text="Ingreso Bruto"))
        self.ingreso = TextInput(font_size=30)
        contenedor.add_widget(self.ingreso)

        contenedor.add_widget(Label(text="Aportes de Ley"))
        self.aportes = TextInput(font_size=30)
        contenedor.add_widget(self.aportes)

        contenedor.add_widget(Label(text="Deducciones"))
        self.deducciones = TextInput(font_size=30)
        contenedor.add_widget(self.deducciones)

        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        calcular = Button(text="Calcular", font_size=40)
        contenedor.add_widget(calcular)

        # EXACTAMENTE igual que el ejemplo
        calcular.bind(on_press=self.calcular_renta)

        return contenedor

    # 🔹 MISMA estructura que el ejemplo
    def calcular_renta(self, value):
        try:
            self.validar()

            datos = Impuestos(
                ingreso_bruto=float(self.ingreso.text),
                aportes_ley=float(self.aportes.text),
                deducciones=float(self.deducciones.text)
            )

            renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)

            self.resultado.text = str(round(total, 2))

        except ValueError:
            self.resultado.text = "El valor ingresado no es válido"

        except Exception as err:
            self.mostrar_error(err)

    # 🔹 EXACTAMENTE igual que tu ejemplo
    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)

        contenido.add_widget(Label(text=str(err)))

        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)

        popup = Popup(title="Error", content=contenido)

        cerrar.bind(on_press=popup.dismiss)

        popup.open()

    # 🔹 MISMA lógica de validación del ejemplo
    def validar(self):

        if not (self.ingreso.text.replace('.', '', 1).isdigit()):
            raise Exception("El ingreso bruto debe ser un número válido")

        if not (self.aportes.text.replace('.', '', 1).isdigit()):
            raise Exception("Los aportes deben ser un número válido")

        if not (self.deducciones.text.replace('.', '', 1).isdigit()):
            raise Exception("Las deducciones deben ser un número válido")


if __name__ == "__main__":
    RentaApp().run()