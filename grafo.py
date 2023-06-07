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
    def search_person_movie(self, nombre):
        nombre = nombre.lower()
        try:
            return self.graph[nombre]
        except:
            print(nombre,"no está en el grafo")

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
                if arista.peso == busqueda:
                    # Se suma 1 a las apariciones con el rol buscado
                    apariciones+=1
                    if apariciones>mayor_apariciones:
                       mayor_apariciones = apariciones
                       actor_director = clave
                       
        return actor_director,mayor_apariciones

    #  Conocer si todas las películas en las que ha trabajado una persona y su
    # relación con la misma
    def all_person_movies(self, actor_name):
        actor_name = actor_name.lower()
        if actor_name in self.graph:
            relaciones=[]
            for arista in self.graph[actor_name]:
                relaciones.append(f"{arista.peso} {arista.v2}")
            return relaciones
        else:
            return actor_name+" NO está en la lista"
                
                
    # Conocer el tipo de una persona, si existe en el grafo: actriz, director o escritor    
    def tipo_persona(self, nombre_persona):
        nombre_persona = nombre_persona.lower()

        if nombre_persona in self.graph:
            roles=[]
            for arista in self.graph[nombre_persona]:
                if arista.peso not in roles:
                    roles.append(arista.peso)
                if arista.peso == "directed_by":
                    return ["película"]
            return  roles
        else: 
            return nombre_persona+" NO está en la lista"
    
    def find_way(self, origin , destiny):   #BUSCAR CAMINO
        # Verificar si los vértices son válidos
        graph = self.graph
        origin = origin.lower()
        destiny = destiny.lower()

        if origin not in graph:
            print(origin,"No está en el grafo") 
            return None
        elif destiny not in graph:
            print(destiny, "No está en el grafo")
            return None

        # queue para realizar el BFS
        queue = [(origin,[origin])]
          # Tupla con el vértice y el camino hasta él
        while queue:
            actual_vertex,actual_way = queue.pop()
            # Si se encuentra el destiny, se retorna el camino
            if actual_vertex == destiny :

                return actual_way

            # Explorar los neighbors del vértice actual
            for neighbor in graph[actual_vertex]:
                if neighbor.v2 not in actual_way:  # Evitar ciclos
                    if neighbor.v2 == destiny:
                        actual_way = actual_way + [neighbor.v2]
                        # queue.append((neig
                        # 
                        # 
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        hbor.v2, actual_way + [neighbor.v2]))
                        return actual_way
                    queue.append((neighbor.v2, actual_way + [neighbor.v2]))


    # Lo que se necista es mirar si hay una relación entre ambos, es decir si actuan en la misma pelicula 
    # hay que recorrer el origen y mirar las peliculas 

        # Si no se encontró un camino, retorna None
        print("No path found between the given vertices.")
        return None

