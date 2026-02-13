# Calculadora de Impuestos Declaracion de renta 

 ###  Creadores

- Carolina florez Salazar 
- Samuel Parra Marin 
  
 La entrevista y la tabla de ecxel se encuentran en la carpeta llamada "Entrega 1"

  ### Persona entrevistada
- **Nombre:** Magnolia Salazar Agudelo 
- **Especialización :** Administracion y Contabilidad 
- **Fecha de la entrevista:** 07/02/2026


### Descripción del Proyecto
La función de esta aplicación es transformar la compleja legislación en un proceso de cálculo preciso y fácil de entender para cualquier trabajador. Su objetivo es procesar el ingreso bruto de un empleado y aplicarle en orden jerárquico todos los beneficios y límites legales que permite la DIAN.

### Funciones 
-  Depuración Automática (salud y pension)
-  Gestión de beneficios (Hijos o padres)
- Control de topes legales (40% del ingreso neto)
- Validación de datos (Como un asalariado no aprta a la salud)

Esta aplicación nos ayuda a tener una herramienta de "empoderamiento financiero y planeación tributaria". Esto quiere decir que convierte a un usuario en el propio dueño de su información tributaria, brindándole la seguridad de sus propios datos y confidencialidad.
 
### Entradas 
- **Ingreso Bruto**: Es el dinero total que el usuario gana antes de cualquier descuento. Es la cifra que aparece en el contrato de trabajo o el total de honorarios recibidos.
- **Aportes ley**: Son los descuentos obligatorios que el estado exige para seguridad social. Sin estos aportes, no se puede calcular la "Renta Líquida".
- **Deducciones**: Son gastos específicos que el usuario ya tiene o inversiones que hace para bajar legalmente la base de sus impuestos. Estas son opcionales pero clave para la optimización.

### Definición de Salidas y Cálculo
**Renta Líquida**: Es el dinero real que queda tras los descuentos obligatorios (salud, pensión, etc.).
- Renta Liquida = Ingreso Bruto - Aportes de ley

**Beneficio Real**: Suma las deducciones específicas (salud prepagada, dependientes, intereses de vivienda) y le añade la exención de ley (el 25% de renta exenta sobre el saldo).
- Beneficio Real = Deducciones + ((Renta LIquida - Deducciones) * 0,25)
  
**Límite Legal**: El techo máximo que la ley permite deducir (usualmente el 40%).
- Limite Legal = Renta LIquida * 0.40

Estas tres fórmulas constituyen el algoritmo de optimización de la aplicación. Son los pilares de cálculo que garantizan que el resultado final sea matemáticamente exacto y legalmente viable
- Resultado Total = Renta Liquida - Limite Legal

## Caso Especial 
Si el Beneficio real es mayor que el Limite legal eentonces:
- Resultado total = Renta Liquida - Limite legal

Si el Beneficio Real es menor o igual que el limite legal entonces:
- Resultado Total = Renta Liquida - Beneficio Real

