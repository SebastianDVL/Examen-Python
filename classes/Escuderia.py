class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__motor = None
        self.__piloto = None
        self.__costoAnual = None

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def motor(self):
        return self.__motor
    
    @property
    def piloto(self):
        return self.__piloto
    
    @property
    def costoAnual(self):
        return self.__costoAnual
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    
    @motor.setter
    def motor(self, value):
        self.__motor = value

    @piloto.setter
    def piloto(self, value):
        self.__piloto = value

    @costoAnual.setter
    def costoAnual(self, value):
        if(value < 0):
            self.__costoAnual =None
            print("Costo Erroneo")
        else:
            self.__costoAnual = value

    def pintarEscuderia(self):
        print("nombre escuderia: " + self.nombre)  
        print("motor: " + self.motor)
        print("piloto: " + self.piloto)
        print("costo anual: " + str(self.costoAnual))