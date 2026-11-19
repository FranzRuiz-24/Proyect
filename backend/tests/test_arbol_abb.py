
import unittest

from backend.estructuras.elemento import Elemento
from backend.estructuras.arbol_abb import ArbolABB


class TestArbolABB(unittest.TestCase):

    def crear_elemento(self, id):
        return Elemento(
            id, f"Elemento {id}", "Descripción",
            "tarea", "2026-12-10", "Alta",
            [], "", "Pendiente"
        )

    def setUp(self):
        self.arbol = ArbolABB()

        for id in [50, 30, 70, 20, 40, 60, 80]:
            self.arbol.insertar(self.crear_elemento(id))

    def test_insertar_y_contar(self):
        self.assertEqual(self.arbol.contar_elementos(), 7)

    def test_buscar(self):
        resultado = self.arbol.buscar(40)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.id, 40)

    def test_buscar_inexistente(self):
        self.assertIsNone(self.arbol.buscar(100))

    def test_rechazar_id_duplicado(self):
        with self.assertRaises(ValueError):
            self.arbol.insertar(self.crear_elemento(50))

    def test_recorrido_inorden(self):
        ids = [e.id for e in self.arbol.recorrido_inorden()]
        self.assertEqual(ids, [20, 30, 40, 50, 60, 70, 80])

    def test_recorrido_preorden(self):
        ids = [e.id for e in self.arbol.recorrido_preorden()]
        self.assertEqual(ids, [50, 30, 20, 40, 70, 60, 80])

    def test_recorrido_postorden(self):
        ids = [e.id for e in self.arbol.recorrido_postorden()]
        self.assertEqual(ids, [20, 40, 30, 60, 80, 70, 50])

    def test_eliminar(self):
        self.arbol.eliminar(20)
        self.assertIsNone(self.arbol.buscar(20))
        self.assertEqual(self.arbol.contar_elementos(), 6)

    def test_altura(self):
        self.assertEqual(self.arbol.altura(), 3)


if __name__ == "__main__":
    unittest.main()
