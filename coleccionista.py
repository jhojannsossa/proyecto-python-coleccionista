print("======================================================")
print("  Bienvenido al Catálogo de Piezas Coleccionables  ")
print("======================================================")

catalog = []
categorias_set = set()

cantidad_piezas = 10

print(f"\nA continuación registrarás {cantidad_piezas} piezas:\n")

for i in range(cantidad_piezas):
    print(f"--- Registrando pieza {i + 1} de {cantidad_piezas} ---")

    id_pieza = input("Identificador único: ")
    name = input("Nombre de la pieza: ")
    category = input("Categoría: ")
    price = float(input("Precio (número decimal): "))
    status = input("Estado (disponible / reservada / vendida): ")
    description = input("Descripción (debe incluir 'usada' o 'certificada'): ")
