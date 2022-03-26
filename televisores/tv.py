class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        TV._numTV = TV._numTV + 1

    # Setters
    def setMarca(self, marca):
        self._marca = marca

    def setControl(self, control):
        self._control = control

    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        if (0 <= volumen) and (volumen <= 7) and self._estado:
            self._volumen = volumen

    def setCanal(self, canal):
        if (1 <= canal) and (canal <= 120) and self._estado:
            self._canal = canal

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    # Getters
    def getMarca(self):
        return self._marca

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    def getEstado(self):
        return self._estado

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    # Methods
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        self.setCanal(self._canal + 1)

    def canalDown(self):
        self.setCanal(self._canal - 1)

    def volumenUp(self):
        self.setVolumen(self._volumen + 1)

    def volumenDown(self):
        self.setVolumen(self._volumen - 1)
