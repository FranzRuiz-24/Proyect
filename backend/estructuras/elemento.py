class Elemento:

    def __init__(self, id, nombre, descripcion, tipo,
                 fecha_vencimiento, prioridad, etiquetas, notas, estado):

        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad
        self.etiquetas = etiquetas
        self.notas = notas
        self.estado = estado