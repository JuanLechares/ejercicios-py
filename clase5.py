class Producto:
    def __init__(self, marca, precio, stock):
        self.marca=marca
        self.precio=precio
        self.stock=stock
    def getAtributos(self):
        pass

class Libro(Producto):
    def __init__(self, marca, precio, stock, volumen, editorial):
        super().__init__(marca, precio, stock)
        self.volumen=volumen
        self.editorial=editorial
    def getAtributos(self):
        print(f"[{self.marca}, {self.precio}, {self.stock}, {self.volumen}, {self.editorial}]")

class Pelicula(Producto):
    def __init__(self, marca, precio, stock, director, titulo):
        super().__init__(marca, precio, stock)
        self.director=director
        self.titulo=titulo

    def getAtributos(self):
        print(f"[{self.marca}, {self.precio}, {self.stock}, {self.director}, {self.titulo}]")

class Disco(Producto):
    def __init__(self, marca, precio, stock, album, artista):
        super().__init__(marca, precio, stock)
        self.album=album
        self.artista=artista
    def getAtributos(self):
        print(f"[{self.marca}, {self.precio}, {self.stock}, {self.album}, {self.artista}]")
    

libro1=Libro("marca", "1500", "12", "rubius", "titanic")
libro2=Libro("marca", "1700", "20", "Thomas Andrews", "titanic")
libro3=Libro("marca", "2700", "24", "Thomas Andrews", "titanic")
pelicula1=Pelicula("marca", "1900", "20", "Thomas Andrews", "titanic")
pelicula2=Pelicula("marca", "1900", "20", "Thomas Andrews", "titanic")
pelicula3=Pelicula("marca", "1900", "20", "Thomas Andrews", "titanic")
disco1=Disco("marca", "7000", "1200", "pepitom", "hola")
disco2=Disco("marca", "7000", "1200", "pepitom", "hola")
disco3=Disco("marca", "7000", "1200", "pepitom", "hola")

libro1.getAtributos()
libro2.getAtributos()
libro3.getAtributos()
pelicula1.getAtributos()
pelicula2.getAtributos()
pelicula3.getAtributos()
disco1.getAtributos()
disco2.getAtributos()
disco3.getAtributos()
        