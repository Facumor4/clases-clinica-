from datetime import date 
class Entidad():
    def Agregar(self):
        print(f"{self.__class__.__name__} agregado correctamente")
    
    def Modificar(self):
        print(f"{self.__class__.__name__} modificado correctamente")
    
    def Eliminar(self):
        print(f"{self.__class__.__name__} eliminado correctamente")
        
    def ListaDeConsulta(self):
        print(f"Listado: \n{self.__class__.__name__}")
    
class Paciente(Entidad):
    def __init__(self, id: str, nombre: str, edad: int, genero: str, email: str, telefono: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def ListaDeConsulta(self):
        pass

class Quimico(Entidad):
    def __init__(self, id: str, nombre: str, direccion: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
    
    def EntregaMedicamentos(self):
        pass
 
class Laboratorio(Entidad):
    def __init__(self, id: str, nombre: str, direccion: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
    
    def RecolectarPrueba(self):
        pass
    
    def GenerarInformeLaboral(self):
        pass
    
class Descripcion(Entidad, Quimico, Laboratorio):
    def __init__(self, idPrescripcion: int, Diagnostico: str, NombreMedicina: str, PotenciaMedicamento: int, 
                FrecuenciaMedicamento: int, Observaciones: str, PruebaLaboratorio: str, LaboratorioInstrucciones: str, 
                PreincripcionesEntregar: str, SolicitudeslaboratorioRealizadas: str, MontolaFactura: float):
        self.idPrescripcion = idPrescripcion
        self.Diagnostico = Diagnostico
        self.NombreMedicina = NombreMedicina
        self.PotenciaMedicamento = PotenciaMedicamento
        self.FrecuenciaMedicamento = FrecuenciaMedicamento
        self.Observaciones = Observaciones
        self.PruebaLaboratorio = PruebaLaboratorio
        self.LaboratorioInstrucciones = LaboratorioInstrucciones
        self.PreincripcionesEntregar = PreincripcionesEntregar
        self.SolicitudeslaboratorioRealizadas = SolicitudeslaboratorioRealizadas
        self.MontolaFactura = MontolaFactura
        
    def GenerarFactura(self):
        pass    
          
class Doctores(Descripcion, Entidad):
    def __init__(self, id: str, nombre: str, edad: int, genero: str, calificacion: str, experiencia: str, numeroRegistro: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.calificacion = calificacion
        self.experiencia = experiencia
        self.numeroRegistro = numeroRegistro
    
class Consultas(Paciente, Doctores, Entidad):
    def __init__(self, en_linea_o_cita: str, fecha_solicitud: date, cadena_sintomas: str, estado_solicitud: str):
        self.en_linea_o_cita = en_linea_o_cita
        self.fecha_solicitud = fecha_solicitud
        self.cadena_sintomas = cadena_sintomas
        self.estado_solicitud = estado_solicitud
        

class Especialista(Consultas, Descripcion, Entidad):
    def __init__(self, ssd: str, nombre: str, descripcion: str):
        self.ssd = ssd
        self.nombre = nombre
        self.descripcion = descripcion
        