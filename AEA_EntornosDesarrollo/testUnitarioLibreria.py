import unittest
import os
from Libreria import Libreria  # Asumiendo que tu código está en un archivo llamado libreria.py

class LibreriaTesteo(unittest.TestCase):
        def setUp(self):
            self.libreria = Libreria()
            self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
            self.libreria.anadir_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", 1985)
            self.test_file = 'test_libreria.json'

        def tearDown(self):
            if os.path.exists(self.test_file):
                os.remove(self.test_file)
        # Añadir libro
        def test_anadir_libro(self):
            resultado = self.libreria.anadir_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 1605)
            self.assertEqual(resultado, "Libro añadido")
            self.assertEqual(len(self.libreria.libros), 3) # Agregacion de un libro que la longitud debe ser de 3
        #Busqueda del libro
        def test_buscar_libro(self):
            resultado = self.libreria.buscar_libro("Cien años de soledad")
            self.assertEqual(len(resultado), 1)
            self.assertEqual(resultado[0]['autor'], "Gabriel García Márquez")
        #Busqueda por autor
        def test_buscar_por_autor(self):
            resultado = self.libreria.buscar_por_autor("Gabriel García Márquez")
            self.assertEqual(len(resultado), 2)
        #Eliminicacion del libro
        def test_eliminar_libro(self):
            resultado = self.libreria.eliminar_libro("Cien años de soledad")
            self.assertEqual(resultado, "Libro eliminado")
            self.assertEqual(len(self.libreria.libros), 1) # Se elimina un libro que su longitud debe ser de 1 
            resultado = self.libreria.eliminar_libro("Libro inexistente")
            self.assertEqual(resultado, "Libro no encontrado")
        #Funcion que ayuda guardar y cargar 
        def test_guardar_y_cargar_libros(self):
            self.libreria.guardar_libros(self.test_file)
            nueva_libreria = Libreria()
            resultado = nueva_libreria.cargar_libros(self.test_file)
            self.assertEqual(resultado, "Libros cargados")
            self.assertEqual(len(nueva_libreria.libros), 2)

if __name__ == '__main__':
        unittest.main()