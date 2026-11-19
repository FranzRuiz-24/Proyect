
from .nodo import Nodo


class ArbolABB:

    def __init__(self):
        self.raiz = None

    def insertar(self, elemento):
        nuevo = Nodo(elemento)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:
            if elemento.id < actual.elemento.id:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda

            elif elemento.id > actual.elemento.id:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha

            else:
                raise ValueError("Ya existe un elemento con ese ID")

    def buscar(self, id):
        actual = self.raiz

        while actual is not None:
            if id == actual.elemento.id:
                return actual.elemento
            elif id < actual.elemento.id:
                actual = actual.izquierda
            else:
                actual = actual.derecha

        return None

    def eliminar(self, id):
        self.raiz = self._eliminar_recursivo(self.raiz, id)

    def _eliminar_recursivo(self, nodo, id):
        if nodo is None:
            return None

        if id < nodo.elemento.id:
            nodo.izquierda = self._eliminar_recursivo(
                nodo.izquierda, id
            )

        elif id > nodo.elemento.id:
            nodo.derecha = self._eliminar_recursivo(
                nodo.derecha, id
            )

        else:
            if nodo.izquierda is None:
                return nodo.derecha

            if nodo.derecha is None:
                return nodo.izquierda

            sucesor = nodo.derecha

            while sucesor.izquierda is not None:
                sucesor = sucesor.izquierda

            nodo.elemento = sucesor.elemento

            nodo.derecha = self._eliminar_recursivo(
                nodo.derecha, sucesor.elemento.id
            )

        return nodo

    def recorrido_inorden(self):
        elementos = []
        self._inorden_recursivo(self.raiz, elementos)
        return elementos

    def _inorden_recursivo(self, nodo, elementos):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda, elementos)
            elementos.append(nodo.elemento)
            self._inorden_recursivo(nodo.derecha, elementos)

    def recorrido_preorden(self):
        elementos = []
        self._preorden_recursivo(self.raiz, elementos)
        return elementos

    def _preorden_recursivo(self, nodo, elementos):
        if nodo is not None:
            elementos.append(nodo.elemento)
            self._preorden_recursivo(nodo.izquierda, elementos)
            self._preorden_recursivo(nodo.derecha, elementos)

    def recorrido_postorden(self):
        elementos = []
        self._postorden_recursivo(self.raiz, elementos)
        return elementos

    def _postorden_recursivo(self, nodo, elementos):
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierda, elementos)
            self._postorden_recursivo(nodo.derecha, elementos)
            elementos.append(nodo.elemento)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0

        izquierda = self._altura_recursiva(nodo.izquierda)
        derecha = self._altura_recursiva(nodo.derecha)

        return 1 + max(izquierda, derecha)

    def contar_elementos(self):
        return self._contar_recursivo(self.raiz)

    def _contar_recursivo(self, nodo):
        if nodo is None:
            return 0

        return (
            1
            + self._contar_recursivo(nodo.izquierda)
            + self._contar_recursivo(nodo.derecha)
        )
