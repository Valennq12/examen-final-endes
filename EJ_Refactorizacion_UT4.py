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
    def mostrar(lista_recetas):
        for receta in lista_recetas:
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
            if ingrediente != 'no':
                ingrediente = input('Dime un INGREDIENTE. SI NO QUIERES AÑADIR MÁS ESCRIBE NO: ').lower()
                lista_ingredientes.append(ingrediente)
            else:
                break
            
            
            
        paso = 'si'
        lista_pasos = []
        while paso != 'no':
            if paso != 'no':
                paso = input('Dime un PASO. SI NO QUIERES AÑADIR MÁS ESCRIBE NO: ').lower()
                lista_pasos.append(paso)
            else:
                break

        return nombre_receta,lista_ingredientes,lista_pasos

# Función principal
def Main():
    print('VAMOS A CREAR UNA RECETA')
    while True:
        opcion = input('RECETA VEGETARIANA (SI|NO)?: ').lower()
        
        if opcion == 'si':
            nombre_receta,lista_ingredientes,lista_pasos = utilidades.crear_receta()
            receta = recetaVegetariana(nombre_receta,lista_ingredientes,lista_pasos)
            recetaVegetariana.lista_recetas.append(receta)
            print()
            

        elif opcion == 'no':
            nombre_receta,lista_ingredientes,lista_pasos = utilidades.crear_receta()
            receta = recetaNoVegetariana(nombre_receta,lista_ingredientes,lista_pasos)
            recetaNoVegetariana.lista_recetas.append(receta)
            print()
            
        elif opcion != 'si' or opcion != 'no':
            print('No se ha especificado el tipo de receta. OPCIONES: SI O NO')
            break
        
        print()
        print('RECETAS VEGETARIANAS')
        utilidades.mostrar(recetaVegetariana.lista_recetas)
        print('RECETAS NO VEGETARIANAS')
        print()
        utilidades.mostrar(recetaNoVegetariana.lista_recetas)
        print()
        
    


# Ejecutar el programa
if __name__ == "__main__":
    Main()
