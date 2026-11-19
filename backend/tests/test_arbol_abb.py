
import unittest
from datetime import date

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

    def test_buscar_vencidos(self):
        self.arbol = ArbolABB()

        vencido = Elemento(
            1, "Tarea vencida", "Descripción",
            "tarea", "2026-11-10", "Alta",
            [], "", "Pendiente"
        )

        vigente = Elemento(
            2, "Tarea vigente", "Descripción",
            "tarea", "2026-12-10", "Media",
            [], "", "Pendiente"
        )

        completado = Elemento(
            3, "Tarea completada", "Descripción",
            "tarea", "2026-11-10", "Alta",
            [], "", "Completada"
        )

        cancelado = Elemento(
            4, "Tarea cancelada", "Descripción",
            "tarea", "2026-11-10", "Alta",
            [], "", "Cancelada"
        )

        for elemento in [vencido, vigente, completado, cancelado]:
            self.arbol.insertar(elemento)

        resultado = self.arbol.buscar_vencidos(date(2026, 11, 19))

        self.assertEqual([e.id for e in resultado], [1])

    def test_buscar_por_etiqueta(self):
        self.arbol = ArbolABB()

        elemento1 = Elemento(
            1, "Tarea 1", "Descripción",
            "tarea", "2026-12-10", "Alta",
            ["Universidad", "Urgente"], "", "Pendiente"
        )

        elemento2 = Elemento(
            2, "Tarea 2", "Descripción",
            "tarea", "2026-12-10", "Media",
            ["Trabajo"], "", "Pendiente"
        )

        self.arbol.insertar(elemento1)
        self.arbol.insertar(elemento2)

        resultado = self.arbol.buscar_por_etiqueta("universidad")

        self.assertEqual([e.id for e in resultado], [1])

    def test_buscar_etiqueta_sin_resultados(self):
        resultado = self.arbol.buscar_por_etiqueta("Deportes")

        self.assertEqual(resultado, [])

    def test_buscar_vencidos_sin_resultados(self):
        resultado = self.arbol.buscar_vencidos(date(2026, 11, 19))

        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()
