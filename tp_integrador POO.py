class Carrito:
    def __init__(self):
        self.__productos = []  # atributo encapsulado (lista de productos)

    def agregar_producto(self, nombre, precio):
        if nombre.strip() == "" or precio <= 0:
            print("Error: datos inválidos.")
            return
        self.__productos.append({"nombre": nombre, "precio": precio})
        print(f" Producto '{nombre}' agregado al carrito.")

    def ver_productos(self):
        if not self.__productos:
            print(" El carrito está vacío.")
        else:
            print("\n📦 Productos en el carrito:")
            for i, p in enumerate(self.__productos, 1):
                print(f"{i}. {p['nombre']} - ${p['precio']}")
            print(f" Total: ${self.total()}")

    def eliminar_producto(self, nombre):
        for p in self.__productos:
            if p["nombre"].lower() == nombre.lower():
                self.__productos.remove(p)
                print(f" Producto '{nombre}' eliminado.")
                return
        print(" Producto no encontrado.")

    def total(self):
        return sum(p["precio"] for p in self.__productos)


# ---- MENÚ PRINCIPAL ----
def menu():
    carrito = Carrito()

    while True:
        print("\n=== MENÚ CARRITO DE COMPRAS ===")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Eliminar producto")
        print("4. Ver total")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: $"))
                carrito.agregar_producto(nombre, precio)
            except ValueError:
                print(" Precio inválido.")
        elif opcion == "2":
            carrito.ver_productos()
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            carrito.eliminar_producto(nombre)
        elif opcion == "4":
            print(f" Total a pagar: ${carrito.total()}")
        elif opcion == "5":
            print(" Gracias por usar el carrito. ¡Hasta luego!")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
