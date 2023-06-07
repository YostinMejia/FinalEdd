import grafo as gr
import leer as rd

def IniciarApp(path):

    info_excel = rd.Excel()
    lista_adyacencia =info_excel.Leer(path)
    grafo = gr.Graph()
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
            actor_director = int(input("Ingrese el número del rol q desea buscar \n1) actor \n2)director\n->"))
            print(grafo.most_requested((actor_director==2)))
        elif opcion == 5:
            nombre = input("Ingrese el nombre de la persona->")
            print(grafo.all_person_movies(nombre))
        elif opcion == 6:
            grafo.print_graph()
        else:
            break
        
        print(" \n ")

IniciarApp('Peliculas.xlsx')