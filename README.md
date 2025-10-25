# TP_INTEGRADOR-POO
### Objetivo
Este programa modela un carrito de compras** aplicando los **principios de la Programación Orientada a Objetos (POO)** en Python.  
Permite agregar, visualizar, eliminar productos y calcular el total a pagar, utilizando encapsulamiento, atributos, métodos y control de estado interno.


### Características del programa
- Clase principal: `Carrito`
- Atributo encapsulado: `__productos` (lista que almacena los artículos)
- Métodos:
  - `agregar_producto(nombre, precio)` → agrega productos al carrito.  
  - `ver_productos()` → muestra los productos cargados y el total.  
  - `eliminar_producto(nombre)` → quita un producto del carrito.  
  - `total()` → devuelve el monto total de la compra.
- Menú interactivo:** permite al usuario elegir acciones mediante consola.
- Validaciones:** evita precios negativos o nombres vacíos.


### Conceptos de POO aplicados
- Clase y Objeto: el carrito es una instancia creada a partir del plano `Carrito`.
- Encapsulamiento: el atributo `__productos` está protegido, solo se modifica por medio de métodos.
- Abstracción: el usuario interactúa mediante métodos simples sin conocer los detalles internos.
- Estado interno: los productos agregados se almacenan en la lista privada del objeto.


### Cómo ejecutar
1. Guardar el archivo `tp_integrador_poo.py`.
2. Abrir una terminal en la carpeta donde está el archivo.
3. Ejecutar:
   ```bash
   python tp_integrador_poo.py
