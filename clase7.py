class Fabrica:
    def __init__(self):
        self.listSucursales=[]

    def agregarSucursal(self, sucursal):
        self.listSucursales.append(sucursal)

    def listarInstrumentos(self):
        for sucursal in self.listSucursales:
            for instrumentos in sucursal.obtenerListaInstrumento():
                print(instrumentos.id, instrumentos.precio, instrumentos.tipo)

    def instrumentosPorTipo(self, tipo):
        for sucursal in self.listSucursales:
            for instrumentos in sucursal.obtenerListaInstrumento():
                if(instrumentos.tipo == tipo):
                    print(instrumentos.id, instrumentos.precio, instrumentos.tipo)


class Sucursal:
    def __init__(self, nombre):
        self.nombre=nombre
        self.Instrumentos=[]

    def agregarInstrumento(self, instrumento):
        self.Instrumentos.append(instrumento)
    
    def obtenerListaInstrumento(self):
        return self.Instrumentos

class Instrumento:
    def __init__(self, id, precio, tipo):
        self.id=id
        self.precio=precio
        self.tipo=tipo

class TipoInstrumento:
    CAT1="Percusion"
    CAT2="Viento"
    CAT3="Cuerda"



fabrica = Fabrica()
sucursal = Sucursal("dia")
instrumento = Instrumento("1","1700", TipoInstrumento.CAT3)
instrumento2 = Instrumento("2","2700", TipoInstrumento.CAT1)
instrumento3 = Instrumento("3","2000", TipoInstrumento.CAT2)

fabrica.agregarSucursal(sucursal)
sucursal.agregarInstrumento(instrumento)
sucursal.agregarInstrumento(instrumento2)
sucursal.agregarInstrumento(instrumento3)

fabrica.listarInstrumentos()
fabrica.instrumentosPorTipo(TipoInstrumento.CAT1)
fabrica.instrumentosPorTipo(TipoInstrumento.CAT2)

