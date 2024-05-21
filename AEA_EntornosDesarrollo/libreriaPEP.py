import json


class Libreria:
    """
    Clase para gestionar una biblioteca de libros.

    Atributos:
        libros (list): Lista de diccionarios que representan los libros de la biblioteca.

    Métodos:
        __init__(self): Constructor de la clase.
        anadir_libro(self, titulo, autor, genero, anio): Añade un nuevo libro a la biblioteca.
        buscar_libro(self, titulo): Busca un libro por su título.
        buscar_por_autor(self, autor): Busca libros por el nombre del autor.
        eliminar_libro(self, titulo): Elimina un libro de la biblioteca por su título.
        guardar_libros(self, archivo): Guarda la biblioteca en un archivo JSON.
        cargar_libros(self, archivo): Carga la biblioteca desde un archivo JSON.
    """

    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un nuevo libro a la biblioteca.

        Argumentos:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.

        Devuelve:
            str: Mensaje de confirmación.
        """
        self.libros.append({"titulo": titulo, "autor": autor, "genero": genero, "anio": anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Argumentos:
            titulo (str): Título del libro a buscar.

        Devuelve:
            list: Lista de diccionarios que representan los libros encontrados.
        """
        return [libro for libro in self.libros if libro["titulo"].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por el nombre del autor.

        Argumentos:
            autor (str): Nombre del autor a buscar.

        Devuelve:
            list: Lista de diccionarios que representan los libros encontrados.
        """
        return [libro for libro in self.libros if autor.lower() in libro["autor"].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la biblioteca por su título.

        Argumentos:
            titulo (str): Título del libro a eliminar.

        Devuelve:
            str: Mensaje de confirmación o error.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro["titulo"].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la biblioteca en un archivo JSON.

        Argumentos:
            archivo (str): Ruta del archivo JSON donde se guardará la biblioteca.

        Devuelve:
            str: Mensaje de confirmación.
        """
        with open(archivo, "w") as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la biblioteca desde un archivo JSON.

        Argumentos:
            archivo (str): Ruta del archivo JSON donde se encuentra la biblioteca.

        Devuelve:
            str: Mensaje de confirmación o error.
        """
        try:
            with open(archivo, "r") as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))
