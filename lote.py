import os

class Lote:
    def __init__(self, frente, fondo, tipo_terreno):
        self.frente = frente
        self.fondo = fondo
        self.area = frente * fondo
        self.tipo_terreno = tipo_terreno
        self.calcular_valor()

    def calcular_valor(self):
        if self.tipo_terreno == "urbano":
            self.valor_metro_cuadrado = 25000
            self.permiso_construccion = 0.45
        elif self.tipo_terreno == "comercial":
            self.valor_metro_cuadrado = 60000
            self.permiso_construccion = 0.75
        elif self.tipo_terreno == "campestre":
            self.valor_metro_cuadrado = 35000
            self.permiso_construccion = 0.15
        else:
            print("Tipo de terreno no válido")
            return None

        self.valor_terreno = self.area * self.valor_metro_cuadrado
        self.costo_permiso = self.area * self.permiso_construccion
        self.valor_total = self.valor_terreno + self.costo_permiso

class Terrenos:
    def __init__(self):
        self.lotes = []

    def agregar_lote(self, frente, fondo, tipo_terreno):
        lote = Lote(frente, fondo, tipo_terreno)
        self.lotes.append(lote)

    def mostrar_lotes(self, tipo_terreno=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        if tipo_terreno:
            print(f"Lotes de tipo {tipo_terreno}:")
            for lote in self.lotes:
                if lote.tipo_terreno == tipo_terreno:
                    print(f"Área: {lote.area} metros cuadrados - Valor total: ${lote.valor_total}")
        else:
            print("Seleccione el tipo de lotes a mostrar:")
            print("1. Mostrar lotes urbanos")
            print("2. Mostrar lotes comerciales")
            print("3. Mostrar lotes campestres")
            opcion_lotes = input("Ingrese su opción: ")

            if opcion_lotes == "1":
                self.mostrar_lotes("urbano")
            elif opcion_lotes == "2":
                self.mostrar_lotes("comercial")
            elif opcion_lotes == "3":
                self.mostrar_lotes("campestre")
            else:
                print("Opción no válida.")
                return

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    terrenos = Terrenos()

    while True:
        print("Menu:")
        print("1. Agregar un nuevo lote")
        print("2. Mostrar lotes")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            tipo_lote = input("Seleccione el tipo de lote (1: Urbano, 2: Comercial, 3: Campestre): ")
            frente = float(input("Ingrese la medida del frente del lote en metros: "))
            fondo = float(input("Ingrese la medida del fondo del lote en metros: "))

            if tipo_lote == "1":
                tipo_terreno = "urbano"
            elif tipo_lote == "2":
                tipo_terreno = "comercial"
            elif tipo_lote == "3":
                tipo_terreno = "campestre"
            else:
                print("Opción no válida.")
                continue

            terrenos.agregar_lote(frente, fondo, tipo_terreno)
            input("Presione Enter para volver al menú...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "2":
            terrenos.mostrar_lotes()
            input("Presione Enter para volver al menú...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
