from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    


# Clase para recetas vegetarianas
class recetaVegetariana(receta):
    pass



# Clase para recetas no vegetarianas
class recetaNoVegetariana(receta):
    pass



# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def mostrar(receta):
        print(f'{receta.nombre}')

        print("Ingredientes:")
        for ingrediente in receta.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in receta.pasos:
            print(f"{paso}")

    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        utilidades.mostrar(receta)
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for elemento in lista:
            print(f"* {elemento}")

# Función principal
def Main():
    receta1 = recetaVegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta2 = recetaNoVegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(receta1)
    utilidades.imprimir_receta(receta2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingrediente in receta1.ingredientes:
        print(f"* {ingrediente}")
    
    print("Ingredientes de Pollo al horno:")
    for ingrediente in receta2.ingredientes:
        print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    Main()
