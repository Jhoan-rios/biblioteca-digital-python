"""  
Módulo que define la clase Libro.

TODO (Principiantes - Paso 1):
- Definir la clase Libro con los atributos indicados.
- Implementar el método __str__ para mostrar la información del libro.
"""


class Libro:
    """Entidad que representa un libro en el catálogo."""

    def __init__(self, id_libro: str, titulo: str, autor: str, anio: int, genero: str) -> None:

        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.prestado = False

    def __str__(self) -> str:

        """ Devuelve una representación en texto del libro"""

    estado = "Prestado" if self.prestado else "Disponible"
    return f"{self.id_libro}: {self.titulo}: {self.autor}: {self.anio}: {self.genero} -- {estado}"
