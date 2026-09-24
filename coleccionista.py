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

pieza = {
        "id": id_pieza,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

catalog.append(pieza)

categorias_set.add(category)
    print("-" * 40)

print("\n======================================================")
print("               RESUMEN DEL CATÁLOGO                   ")
print("======================================================")

for pieza in catalog:
    print(f"ID: {pieza['id']} | Nombre: {pieza['name']} | Categoría: {pieza['category']} | Precio: ${pieza['price']} | Estado: {pieza['status']}")
    print(f"Descripción: {pieza['description']}")
    print("-" * 50)

print(f"\nCantidad total de piezas: {len(catalog)}")
print(f"Categorías únicas ({len(categorias_set)} en total): {categorias_set}")