from uuid import uuid4
from json import load, decoder, dump


#INICIALIZANDO LISTA DE DICCIONARIOS
registro_alumnos = {
    'alumnos_registrados' : []
}

registro_docentes = {
    'docentes_registrados' : []
}


#INICIO DE LA CLASE ALUMNO
class Alumno(): 

    #CONSTRUCTOR DE LA CLASE ALUMNO
    def __init__(self, nombres, notas = []):
        self.nombres  = nombres
        self.notas  = notas

    #INTERFAZ CON EL USUARIO 
    def IntAlumno(self):
        print ("Bienvenido al sistema de registro escolar")
        respuesta = input ("Quiere registrar un nuevo alumno (Si / No): ")
        if respuesta == "Si":
            estudiante = input("Ingrese el nombre del estudiante: ")
            cant_notas = int(input("¿Cuantas notas se van a registrar?: "))
            notas= []
            for item in range(cant_notas):
                nota = float(input(f"Ingrese nota: {item +1 }: "))
                notas.append(nota)
        else:
            print("digitar SI O NO")
        
        self.registrar_alumno(estudiante,notas)

    def registrar_alumno(self, nombres, notas = []):
        alumno = Alumno(nombres, notas) 

        promedio = sum(notas)/len(notas)
        notaMaxima = max(notas)
        notaMinima = min(notas)

        #CREACION DEL DICCIONARIO 
        registro = {
            "id" : str(uuid4()), 
            "nombres" : alumno.nombres,
            "Notas" : alumno.notas,
            "Promedio": float(promedio),
            "Nota_maxima" : float(notaMaxima),
            "Nota_minima" : float(notaMinima)
        }
        
        self.almacenar_reg_alumno(registro)
    
    def almacenar_reg_alumno(self,data):
        registro_alumnos['alumnos_registrados'].append(data)
        alumnos = registro_alumnos['alumnos_registrados']
        archivo = open("registro_alumnos.json", "w")
        dump(alumnos, archivo, indent=4)
        archivo.close()

    def cargar_alumnos(self):
        try:
            archivo = open("registro_alumnos.json", "r")
            registro_alumnos["alumnos_registrados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n No Creando registro de alumnos...")
            archivo = open ("registro_alumnos.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print ("\n No hay alumnos registros, registre ahora")

    def listar_alumnos(self):
        try:
            archivo = open("registro_alumnos.json", "r")
            print(archivo.read())
        except Exception as ex:
            print("error")
        else:
            archivo.close()


#INICIO DE LA CLASE DOCENTE

class Docente:
    #CONSTRUCTOR
    def __init__(self, nombre,edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def intDocente(self):
        print ("Bienvenido al sistema de registro escolar")
        respuesta = input ("Quiere registrar algun docente?(Si /No): ")
        if respuesta == "Si":
            docente = input("Ingrese el nombre del docente: ")
            edad = int(input("Ingrese la edad del docente: "))
            dni = input("Ingrese el DNI del docente: ")
        else:
            print("digitar SI O NO")

        self.registrar_docente(docente, edad, dni)    

    def registrar_docente(self, nombre, edad, dni):
        docente = Docente(nombre, edad, dni)

        registro = {
            "id" : str(uuid4()), 
            "nombres" : docente.nombre,
            "edad" : docente.edad,
            "dni" : docente.dni
        }
        self.guardar_docente(registro)

    def guardar_docente(self, registro):
        registro_docentes['docentes_registrados'].append(registro)
        docentes = registro_docentes['docentes_registrados']
        archivo = open("registro_docentes.json", "w")
        dump(docentes, archivo, indent=4)
        archivo.close()

    def cargar_docente(self):
        try:
            archivo = open("registro_docentes.json", "r")
            registro_docentes["docentes_registrados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n No Creando registro de Docentes...")
            archivo = open("registro_docentes.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print ("\n No hay docentes registrados, registre ahora")

    def listar_docentes(self):
        try:
            archivo = open("registro_docentes.json", "r")
            print(archivo.read())
        except Exception as ex:
            print(f"ocurrió un error al leer el archivo -- {str(ex)} ")
        else:
            archivo.close()


########### CLASE A PARTE $#########

##LA PRIMERA INTERFAZ A EJECUTAR EN EL SISTEMA - (SEGUNDO EN EJECUTARSE)
class inicio(Alumno,Docente):

    def interfaz(self):
        print("Bienvenido al Sistema escolar")
        print('''
            Elegir una opcion:
            1) Registrar a un alumno
            2) Registrar a un docente
            3) listar alumnos registrados
            4) listar docentes registrados
        ''')
        respuesta = input(">>")
        if respuesta == "1":
            self.cargar_alumnos()
            self.IntAlumno()

        elif respuesta == "2":
            self.cargar_docente
            self.intDocente()
        elif respuesta == "3":
            print("#########################")
            print("Lista de Alumnos registrados")
            self.listar_alumnos()
        elif respuesta == "4":
            print("#########################")
            print("Lista de Docentes registrados")
            self.listar_docentes()
        else:
            print("Ingrese una opcion valida")



#CLASE MAIN (ESTA CLASE SE INICIA AL EJECUTAR EL ARCHIVO PYTHON)
class Start(inicio): 
    def __init__(self):
        try:
            #LLAMA AL METODO DE LA CLASE INICIO 
            self.interfaz()
        except KeyboardInterrupt:
            print ('\n Se interrumpio la aplicacion')
Start()


