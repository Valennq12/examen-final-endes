from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    


# Clase para recetas vegetarianas
class recetaVegetariana(receta):
    lista_recetas = []



# Clase para recetas no vegetarianas
class recetaNoVegetariana(receta):
    lista_recetas = []



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

    @staticmethod
    def crear_receta():
        nombre_receta = input('Nombre receta: ')
        ingrediente = 'si'
        lista_ingredientes = []
        while ingrediente != 'no':
            ingrediente = input('Dime un ingrediente. SI NO QUIERES AÑADIR MÁS ESCRIBE NO: ').lower()
            lista_ingredientes.append(ingrediente)
            
        paso = 'si'
        lista_pasos = []
        while paso != 'no':
            paso = input('Dime un ingrediente. SI NO QUIERES AÑADIR MÁS ESCRIBE NO: ').lower()
            lista_pasos.append(paso)

        return nombre_receta,lista_ingredientes,lista_pasos


            



# Función principal
def Main():
    
   pass


# Ejecutar el programa
if __name__ == "__main__":
    Main()
