import hug
from bd import *


@hug.get('/habilitacion/capacitaciones')
def get_capacitaciones():
    return BD_capacitaciones


@hug.get('/habilitacion/capacitados')
def get_todos_capacitados_todos_de_veras():
    return BD_capacitados


@hug.get('/habilitacion/capacitados/{id_capacitacion}')
def get_todos_capacitados(id_capacitacion: hug.types.number):
    return BD_capacitados[id_capacitacion]


@hug.get('/habilitacion/capacitaciones/{id_capacitado}')
def get_un_capacitado(id_capacitado: hug.types.number):
    capacitaciones = []
    for id_capacitacion in BD_capacitados:
        if id_capacitado in BD_capacitados[id_capacitacion]:
            capacitaciones.append(id_capacitacion)
    return capacitaciones


@hug.get('/habilitacion/recursos/{id_capcitacion}')
def get_recursos(id_capacitacion: hug.types.number):
    return BD_recursos[id_capacitacion]


@hug.get('/habilitacion/capacitado/{id_persona}/{id_capacitacion}')
def check_capacitacion(id_persona: hug.types.number, id_capacitacion: hug.types.number):
    return id_persona in BD_capacitados[id_capacitacion]
