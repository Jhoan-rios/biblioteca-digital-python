from datetime import datetime


class Prestamo:
    """Representa el préstamo de un libro a un usuario."""

    def __init__(
        self,
        id_prestamo: str,
        id_libro: str,
        id_usuario: str,
        fecha_salida: datetime | None = None
    ) -> None:
        """
        Inicializa un nuevo préstamo.
        """
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.fecha_salida = fecha_salida if fecha_salida is not None else datetime.now()
        self.fecha_devolucion = None

    def marcar_devuelto(self) -> None:
        """
        Registra la devolución del préstamo.
        """
        self.fecha_devolucion = datetime.now()