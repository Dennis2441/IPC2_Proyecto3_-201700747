class NodeS:
    def __init__(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado,tipo):
        self.Carnet = carnet
        self.DPI = dpi
        self.Nombre = nombre
        self.Carrera = carrera
        self.Password = password
        self.Creditos = creditos
        self.Edad = edad
        self.Correo = correo
        self.Descripcion = descripcion
        self.Materia = materia
        self.Fecha = fecha
        self.Hora = hora
        self.Estado = estado
        self.tipo=tipo
        self.Next = None
        self.Previous = None