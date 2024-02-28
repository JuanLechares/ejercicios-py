class Fabrica:
    def __init__(self):
        self.listSucursales=[]

    def agregarSucursal(self, sucursal):
        self.listSucursales.append(sucursal)

    def listarInstrumentos(self):
        for sucursal in self.listSucursales:
            for instrumento in sucursal.obtenerListaInstrumento():
                print(instrumento.id, instrumento.precio, instrumento.tipo)

    def instrumentosPorTipo(self, tipo):
        for sucursal in self.listSucursales:
            for instrumento in sucursal.obtenerListaInstrumento():
                if(instrumento.tipo == tipo):
                    print(instrumento.id, instrumento.precio, instrumento.tipo)

    def borrarInstrumento(self, instrumentoId):
        for sucursal in self.listSucursales:
            for instrumento in sucursal.obtenerListaInstrumento():
                if(instrumento.id == instrumentoId):
                   sucursal.obtenerListaInstrumento().remove(instrumento)
    
    def porcInstrumentoPorTipo(self, nombreSucursal):
        for sucursal in self.listSucursales:
            if(sucursal.nombre == nombreSucursal):
                cat1=0
                cat2=0
                cat3=0
                for instrumento in sucursal.obtenerListaInstrumento():
                    if(instrumento.tipo == TipoInstrumento.CAT1):
                        cat1+=1
                    elif(instrumento.tipo == TipoInstrumento.CAT2):
                        cat2+=1
                    elif(instrumento.tipo == TipoInstrumento.CAT3):
                        cat3+=1
                print(sucursal.nombre)
                print(TipoInstrumento.CAT1, ( cat1 * 100) / (len(sucursal.obtenerListaInstrumento()) ), "%")
                print(TipoInstrumento.CAT2, (cat2 * 100) / (len(sucursal.obtenerListaInstrumento())  ), "%")
                print(TipoInstrumento.CAT3,(cat3 * 100) / (len(sucursal.obtenerListaInstrumento())  ), "%") 
                   
            



class Sucursal:
    def __init__(self, nombre):
        self.nombre=nombre
        self.instrumentos=[]

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)
    
    def obtenerListaInstrumento(self):
        return self.instrumentos

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
print("--------------")
fabrica.instrumentosPorTipo(TipoInstrumento.CAT1)
print("--------------")
fabrica.borrarInstrumento("1")
fabrica.listarInstrumentos()

print("--------------")
fabrica.porcInstrumentoPorTipo("dia")
