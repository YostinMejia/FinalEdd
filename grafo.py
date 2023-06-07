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
            if actual_vertex == destiny:

                return actual_way

            # Explorar los neighbors del vértice actual
            for neighbor in graph[actual_vertex]:
                if neighbor.v2 not in actual_way:  # Evitar ciclos
                    queue.append((neighbor.v2, actual_way + [neighbor.peso+"-->",neighbor.v2]))

        # Si no se encontró un camino, retorna None
        print("No path found between the given vertices.")
        return None

# # Crear la matriz de adyacencia

def IniciarApp(path):

    info_excel = rd.Excel()
    lista_adyacencia =info_excel.Leer(path)
    grafo = Graph()
    grafo.graph = lista_adyacencia

    
    while True:
        print("Opciones disponibles\n1) Buscar a una persona o película por nombre"+
              "\n2) Conocer el tipo de una persona,si existe en el grafo: actriz, director o escritor"+
              "\n3) Conocer la relación directa o indirecta de dos nodos v1 y v2.Por ejemplo, v1 es el director de una película donde actuó v2 o el escritor v1 escribió la película v2. "+
              "\n4) Conocer el actor que ha actuado en más películas o Conocer el director que más películas ha dirigido"+
              "\n5) Conocer si todas las películas en las que ha trabajado una persona y su relación con la misma"+
              "\n6) Mostrar la lista de adyacencia"+
              "\nIngrese otro número para terminar el ciclo")
        
        opcion = int(input("\nIngrese el número de la opción se desea realizar ->"))
        if opcion == 1:
            nombre = input("Ingrese el nombre de la persona o pelicula que de desea buscar: ")
            print(grafo.search_person_movie(nombre))
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la persona o pelicula que de desea buscar: ")
            print(grafo.tipo_persona(nombre))
        elif opcion == 3:
            v1 = input("V1 Nombre del origen->")
            v2 = input("V2 Nombre del destino->")
            print(grafo.find_way(v1,v2))
        elif opcion == 4 :
            actor_director = int(input("Ingrese el número del rol q desea buscar \n1) actor \n2)director"))
            print(grafo.most_requested((actor_director==2)))
        elif opcion == 5:
            nombre = input("Ingrese el nombre de la persona")
            print(grafo.all_person_movies(nombre))
        elif opcion == 6:
            grafo.print_graph()
        else:
            break

IniciarApp('Peliculas.xlsx')

