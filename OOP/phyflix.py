class Contenido:
    
    nombre = None
    genero = None
    año = 0

class Episodio:
    nroEpisodio = 0
    titulo = None
    duracion = 0
    def reproducir(self):
        print("Reproduciendo " +  self.titulo)

class Websodio(Episodio):
    url = None

class Temporada:
    numeroTemporada = 0
    episodios = []

    
class Serie(Contenido):
    temporadas = []

class Pelicula(Contenido):
    ganoOscar = False

class NetflixService:
    catalogoSeries = []
    catalogoPeliculas = []


breakingB = Serie()

breakingB.nombre = "Breaking Bad"
breakingB.año = 2008
breakingB.genero = "Drama"
            
t5 = Temporada()
t5.nroTemporada = 5

ep = Episodio()

ep.nroEpisodio = 7
ep.titulo = "Say my name"
ep.duracion = 43
            
t5.episodios.append(ep)

ep.reproducir()
