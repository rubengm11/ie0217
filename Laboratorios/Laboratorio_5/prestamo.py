import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Prestamo:
    def __init__(self, monto_prestamo, tasa_interes_anual, cuotas):
        # Inicializacion de los atributos de la clase
        self.monto_prestamo = monto_prestamo
        self.tasa_interes_anual = tasa_interes_anual
        self.cuotas = cuotas
        self.amortizacion = self.calcular_amortizacion()

    def calcular_amortizacion(self):
        try:
            # Calculo mensual de la tasa de interes
            tasa_interes_mensual = self.tasa_interes_anual / 12 / 100
            # Calculo de la cuota mensual
            cuota_mensual = (tasa_interes_mensual * self.monto_prestamo)/ (1 - (1 + tasa_interes_mensual)**-self.cuotas)

            saldo_restante = self.monto_prestamo
            amortizacion = []
            for cuota in range(1, self.cuotas + 1):
                # Calculo de intereses y amortizacion para cada cuota
                interes_pendiente = saldo_restante * tasa_interes_mensual
                amortizacion_prinicipal = cuota_mensual - interes_pendiente

                saldo_restante -= amortizacion_prinicipal
                # Registro de informacion en la lista amortizacion
                amortizacion.append({'Cuota': cuota, 'Interes': interes_pendiente, 'Amortizacion': amortizacion_prinicipal, 'Saldo restante':saldo_restante})
            return amortizacion
        except ZeroDivisionError:
            # Manejo de excepcion para evitar division por cero
            print("Error : la cantidad de cuotas no puede ser 0")
            return []

    def generar_reporte(self, archivo_salida):
        try:
            # Creacion de un DataFrame con la informacion de amortizacion y escritura a un archivo CSV
            df = pd.DataFrame(self.amortizacion)
            df.to_csv(archivo_salida, index = False)
            print(f'Reporte generado con exito: {archivo_salida}')
        except Exception as e:
            # Manejo de excepcion para posibles errores al generar el reporte
            print(f'Ocurrio un error al generar el reporte: {str(e)}')

    def graficar_amortizacion(self):
        # Creacion de un grafico de barras para visualizar amortizacion e intereses por cuota
        df = pd.DataFrame(self.amortizacion)
        data = np.array([df['Interes'],df['Amortizacion']])
        plt.bar(df['Cuota'],data[0], label='Interes')
        plt.bar(df['Cuota'],data[1], bottom=data[0], label='Amortizacion')
        plt.xlabel('Numero de cuota')
        plt.ylabel('Monto (S)')
        plt.title('Amortizacion e intereses por cuota')
        plt.legend()
        plt.show()

def main():
    while True:
        try:
            # Solicitar al usuario el monto, tasa de interes y cantidad de cuotas
            monto = float(input("Ingrese el monto (numero positivo): "))
            tasa_interes = float(input("Ingrese la tasa de interes (numero positivo): "))
            cuotas = int(input("Ingrese la cantidad de cuotas (entero positivo): "))

            # Validar que los datos ingresados son positivos
            if monto <= 0 or tasa_interes < 0 or cuotas <= 0:
                raise ValueError("Error: Los datos ingresados deben ser numeros positivos para monto e interes, y entero positivo para cuotas.")
            
            # Instanciar la clase Prestamo
            prestamo1 = Prestamo(monto, tasa_interes, cuotas)
            
            # Generar un reporte en un archivo CSV
            prestamo1.generar_reporte("reporte.csv")
                
            # Imprimir informacion sobre el prestamo
            print(f"Informacion del prestamo:\nMonto: {monto}\nTasa de interes: {tasa_interes}\nCantidad de cuotas: {cuotas}")

            # Graficar la amortizacion
            prestamo1.graficar_amortizacion()
            break

        except ValueError:
            # Manejo de excepciones para asegurar la entrada de datos
            print("Por favor, ingrese numeros positivos para el monto y la tasa de interes, y un entero positivo para la cantidad de cuotas.")    

if __name__ == "__main__":
    main()
