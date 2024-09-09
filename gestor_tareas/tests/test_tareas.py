import unittest
from datetime import date
from gestor import AgreTar, ElimTar, ModTar, MostTar, tars, cates, etiqs, Tar, TarConFechLim

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        tars.clear()
        cates.clear()
        etiqs.clear()

    def TestAgTar(self):
        AgreTar()
        self.assertEqual(len(tars), 1)
        self.assertIn('Trabajo', cates)
        self.assertIn('urgente', etiqs)

    def TestElimTar(self):
        AgreTar()
        ElimTar()
        self.assertEqual(len(tars), 0)

    def TestModTar(self):
        AgreTar()
        ModTar()
        self.assertEqual(tars[0]['nombre'], 'Tarea Actualizada 1')

    def TestMostTar(self):
        AgreTar()
        MostTar()
        self.assertEqual(len(tars), 1)

    def TestClasTar(self):
        tar = Tar("Tarea 1", "Trabajo", (2023, 10, 1), {"urgente"})
        self.assertEqual(str(tar), "Nombre: Tarea 1, Categoría: Trabajo, Fecha de Vencimiento: 2023-10-01, Etiquetas: {'urgente'}")

    def TestClasTarConFechLim(self):
        tar = TarConFechLim("Tarea 1", "Trabajo", (2023, 10, 1), {"urgente"}, (2023, 10, 5))
        self.assertEqual(str(tar), "Nombre: Tarea 1, Categoría: Trabajo, Fecha de Vencimiento: 2023-10-01, Etiquetas: {'urgente'}, Fecha Límite: 2023-10-05")

if __name__ == '__main':
    unittest.main()