import leer as rd
import arista

class Graph:
    def __init__(self):
      self.graph = {} #lista de adyacencia
    
    # def add_vertex(self, label):                #AGREGAR NODO
    #   if label not in self.graph.keys():
    #     self.graph[label] = [] #nodo desconectado

    # def has_edge(self, v1, v2): 
    #     for arista in self.graph[v1]:
    #         if  arista.v2 == v2:       #TIENE ARISTAS
    #             return True
    #     return False

    # def add_edge(self, v1, v2, rol):       #AGREGAR ARISTA
    #   self.add_vertex(v1)
    #   self.add_vertex(v2)
    
    #   if(not self.has_edge(v1,v2)):
    #     self.graph[v1].append(arista.Arista(rol,v1,v2))

    def print_graph(self):
      print(self.graph)   #VISUALIZAR GRAFO

    # def delete_vertex(self, v1):
    #   pass

    def most_requested(self, actor=False):
        # Miramos en cuantas peliculas están
        busqueda = ""
        if actor:
           busqueda = "acts_in"
        else:
           busqueda = "directs"

        actor_director =""
        mayor_apariciones = 0

        for clave in self.graph:
            apariciones = 0
            # Se miran las aristas
            for arista in self.graph[clave]:
                # Si el valor de la arista el igual al rol que se está buscando
                if arista.valor == busqueda:
                    # Se suma 1 a las apariciones con el rol buscado
                    apariciones+=1
                    if apariciones>mayor_apariciones:
                       mayor_apariciones = apariciones
                       actor_director = clave
                       
        return actor_director,mayor_apariciones
    # Buscar a una persona o película por nombre
    #  Conocer si todas las películas en las que ha trabajado una persona y su
    # relación con la misma
    def all_actor_movies(self, actor_name):
        actor_name = actor_name.lower()
        if actor_name in self.graph:
            relaciones=[]
            for arista in self.graph[actor_name]:
                relaciones.append(f"{arista.valor} {arista.v2}")
            return relaciones
        else:
            return actor_name+" NO está en la lista"
                
                
    # Conocer el tipo de una persona, si existe en el grafo: actriz, director o escritor    
    def tipo_persona(self, nombre_persona):
        nombre_persona = nombre_persona.lower()

        if nombre_persona in self.graph:
            roles=[]
            for arista in self.graph[nombre_persona]:
                if arista.valor not in roles:
                    roles.append(arista.valor)
                if arista.valor == "directed_by":
                    return ["película"]
            return  roles
        else: 
            return nombre_persona+" NO está en la lista"
    
    def find_way(self, origin , destiny):   #BUSCAR CAMINO
        # Verificar si los vértices son válidos
        graph = self.graph
        origin = origin.lower()
        destiny = destiny.lower()

        if origin not in graph or destiny not in graph:
            return None

        # queue para realizar el BFS
        queue = []
        queue.append(origin)  # Tupla con el vértice y el camino hasta él
        way=[origin]
        while queue:
            actual_vertex = queue.pop()
            # Si se encuentra el destiny, se retorna el camino
            if actual_vertex == destiny:

                return way

            # Explorar los neighbors del vértice actual
            for neighbor in graph[actual_vertex]:
                if neighbor.v2 not in way:  # Evitar ciclos
                    queue.append(neighbor.v2)
                    way.append (neighbor.v2)

        # Si no se encontró un camino, retorna None
        print("No path found between the given vertices.")
        return None

# # Crear la matriz de adyacencia

s = rd.Excel()
lista_adyacencia =s.Leer('Peliculas.xlsx')
grafo = Graph()

grafo.graph = lista_adyacencia
# grafo.print_graph()
print(grafo.most_requested(True))
print(grafo.most_requested(False))
print(grafo.all_actor_movies("Mario puzo"))

print(grafo.tipo_persona("The Silence of the Lambs"))
print(grafo.find_way("George Lucas","brad pitt"))


