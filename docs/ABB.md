
# Documentación del Árbol Binario de Búsqueda (ABB)

## 1. Descripción
TaskFlow utiliza un Árbol Binario de Búsqueda (ABB) para organizar elementos mediante sus identificadores (ID).

Cada nodo almacena un elemento y referencias a sus hijos izquierdo y derecho.

## 2. Funcionamiento
- Los IDs menores se ubican a la izquierda.
- Los IDs mayores se ubican a la derecha.
- No se permiten IDs duplicados.

## 3. Operaciones principales
- Insertar: agrega un elemento.
- Buscar: localiza un elemento por su ID.
- Eliminar: retira un elemento conservando las propiedades del árbol.
- Preorden: raíz, izquierda y derecha.
- Inorden: izquierda, raíz y derecha.
- Postorden: izquierda, derecha y raíz.
- Altura: calcula la altura del árbol.
- Conteo: determina cuántos elementos contiene.

## 4. Complejidad algorítmica

| Operación | Promedio | Peor caso |
|---|---|---|
| Inserción | O(log n) | O(n) |
| Búsqueda | O(log n) | O(n) |
| Eliminación | O(log n) | O(n) |
| Recorridos | O(n) | O(n) |
| Altura | O(n) | O(n) |
| Conteo | O(n) | O(n) |

## 5. Pruebas
La implementación cuenta con 9 pruebas unitarias para verificar las operaciones del ABB.

## 6. Conclusión
El ABB permite organizar y consultar los elementos de TaskFlow mediante sus identificadores.
