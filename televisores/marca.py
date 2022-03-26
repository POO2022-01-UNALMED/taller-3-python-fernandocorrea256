class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    # Getters
    def getNombre(self):
        return self._nombre

    # Setters
    def setNombre(self, nombre):
        self._nombre = nombre