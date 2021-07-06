import hug

BD_capacitaciones = {}
BD_capacitados = {}
BD_recursos = {}


@hug.get('/habilitacion/capacitaciones')
def get_capacitaciones():
    return {"Hello World": 1}


@hug.get('/habilitacion/capacitados')
def get_todos_capacitados(id_capacitacion: hug.types.text):
    return BD_capacitados[id_capacitacion]


@hug.get('/habilitacion/capacitaciones/{id_capacitado}')
def get_un_capacitado(id_capacitado: hug.type.text):
    return {"Hello World": 1}


@hug.get('/habilitacion/recursos/{id_capcitacion}')
def get_recursos(id_capacitacion: hug.type.text):
    return BD_recursos[id_capacitacion]


@hug.get('/habilitacion/{id_persona}{id_capacitacion}')
def check_capacitacion(id_persona: hug.types.text, id_capacitacion: hug.types.text):
    return "😎"
