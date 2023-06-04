import openpyxl

import arista 

def minus(data):
    return str(data).lower()

class Excel :

    def AgregarRol(self, lista_adyacencia, v1 ,v2, rol=None ):
        # Si la persona existe en la lista de adyacencia se le agrega las peliculas que ha dirigido
        edge =arista.Arista(rol,v1,v2)

        if (v1 in lista_adyacencia):
            # Al director le agregamos la pelicula que dirigio
            lista_adyacencia[v1].append(edge)
        else:
            # Le asignamos todos los roles posibles, para posteriormente llenarlos
            lista_adyacencia[v1]=[edge]
        
        
    def Leer(self,path):

        # Load the workbook
        wb = openpyxl.load_workbook(path)

        # Select the active worksheet
        ws = wb.active

        lista_adyacencia ={}

        datos = list(ws.values) 

        for fila in range(1,len(datos)):

                list_actores = list(map(lambda x: minus(x),datos[fila][3].split(",")))
                list_escritores = list(map(lambda x: minus(x),datos[fila][2].split(",")))

                titulo = minus(datos[fila][0])
                persona = minus(datos[fila][1])
                
                # Si la persona existe en la lista de adyacencia se le agrega las peliculas que ha dirigido
                self.AgregarRol( lista_adyacencia,persona,titulo,"directs")
        
                # Clave pelicula valor Directores de la pelicula
                self.AgregarRol(lista_adyacencia,titulo,persona,"directed_by")

                # Se crea la pelicula para añadir posteriormente los actores                

                for j in range( max(len(list_actores),len(list_escritores)) ):

                    if  j < len(list_actores) :

                        actor = list_actores[j]
                        # Clave el nombre del actor y valor las películas en las q actúo 
                        self.AgregarRol(lista_adyacencia,actor,titulo,"acts_in")

                        # Se agrega en personas que actuaron en el titulo
                        self.AgregarRol(lista_adyacencia,titulo,actor,"acted_by")

                    if  j < len(list_escritores) :

                        escritor = list_escritores[j]
                        # Clave nombre del escritor y valor película en la q escribio
                        self.AgregarRol(lista_adyacencia,escritor,titulo,"writes")


        return lista_adyacencia


# d={}

# d["a"] =[]

# print(d)