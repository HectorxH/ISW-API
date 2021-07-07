from requests import get
from json import loads
import argparse

# Parseo de parametros para el codigo

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-u", "--url", help="specifies a url")

args = parser.parse_args()
verbose = args.verbose
URL = args.url or "http://18.221.241.253:8000"

# Print para el caso Verbose


def vprint(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)


# Comparaciones para tests

BD_capacitaciones = {
    '1': {"Nombre": "Capacitacion Impresora 1", "Descripcion": "descripcion", "Tipos de maquinas": "Impresora 3D", "Ayudantes": 1},
    '2': {"Nombre": "Capacitacion Impresora 2", "Descripcion": "descripcion", "Tipos de maquinas": "Impresora 3D", "Ayudantes": 3},
    '3': {"Nombre": "Capacitacion Torno 1", "Descripcion": "descripcion", "Tipos de maquinas": "Torno", "Ayudantes": 2},
    '4': {"Nombre": "Capacitacion Cortadora 1", "Descripcion": "descripcion", "Tipos de maquinas": "Cortadora laser", "Ayudantes": 4},
    '5': {"Nombre": "Capacitacion Impresora 3", "Descripcion": "descripcion", "Tipos de maquinas": "Impresora 3D", "Ayudantes": 4},
    '6': {"Nombre": "Capacitacion Cortadora 2", "Descripcion": "descripcion", "Tipos de maquinas": "Cortadora laser", "Ayudantes": 3}
}

BD_capacitados = {'1': [3, 4], '2': [], '3': [
    3, 7, 5], '4': [7], '5': [3, 5], '6': [1, 2, 3, 5]}

test_capacitados = [[3, 4], [], [3, 7, 5], [7]]

test_capacitaciones = [[6], [6], [1, 3, 5, 6], [1]]

BD_recursos = {
    '1': [{"id": 1, "Nombre": "recurso 1", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}, {"id": 2, "Nombre": "recurso 2", "Descripcion": "descripcion", "Formato": "ppt", "Link": "url_prueba.com"}, {"id": 3, "Nombre": "recurso 3", "Descripcion": "descripcion", "Formato": "mov", "Link": "url_prueba.com"}],
    '2': [{"id": 4, "Nombre": "recurso 4", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}, {"id": 5, "Nombre": "recurso 5", "Descripcion": "descripcion", "Formato": "mov", "Link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"id": 6, "Nombre": "recurso 6", "Descripcion": "descripcion", "Formato": "ppt", "Link": "url_prueba.com"}],
    '3': [{"id": 7, "Nombre": "recurso 7", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
    '4': [{"id": 8, "Nombre": "recurso 8", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
    '5': [{"id": 9, "Nombre": "recurso 9", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
    '6': [{"id": 10, "Nombre": "recurso 10", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
}

# Tests

vprint(f"Probando: [GET] {URL}/habilitacion/capacitaciones")
test1 = get(URL+"/habilitacion/capacitaciones")

content1 = loads(test1.text)

assert test1, (f"Error al realizar[GET] /habilitacion/capacitaciones.\n"
               "Status code={test1.status_code}")

vprint("Test 1/2 exitoso.")

assert content1 == BD_capacitaciones, (f"Error al realizar[GET] /habilitacion/capacitaciones.\n"
                                       "El contenido del response no es lo esperado.")

vprint("Test 2/2 exitoso.")


vprint(f"Probando: [GET] {URL}/habilitacion/capacitados")
test2 = get(URL+"/habilitacion/capacitados")

content2 = loads(test2.text)

assert test2, (f"Error al realizar[GET] /habilitacion/capacitados.\n"
               "Status code={test1.status_code}")

vprint("Test 1/2 exitoso.")

assert content2 == BD_capacitados, (f"Error al realizar [GET] /habilitacion/capacitados.\n"
                                    "El contenido del response no es lo esperado.")

vprint("Test 2/2 exitoso.")


vprint(f"Probando: [GET] {URL}/habilitacion/capacitados/<id_capacitacion>")
for i in range(1, 5):
    test3 = get(URL+f"/habilitacion/capacitados/{i}")

    content3 = loads(test3.text)

    assert test3, (f"Error al realizar [GET] /habilitacion/capacitados/{i}.\n"
                   "Status code = {test1.status_code}")

    vprint(f"Test {2*(i-1)+1}/8 exitoso.")

    assert content3 == test_capacitados[i-1], (f"Error al realizar [GET] /habilitacion/capacitados/{i}.\n"
                                               "El contenido del response no es lo esperado.")

    vprint(f"Test {2*(i-1)+2}/8 exitoso.")


vprint(f"Probando: [GET] {URL}/habilitacion/capacitaciones/<id_capacitado>")
for i in range(1, 5):
    test4 = get(URL+f"/habilitacion/capacitaciones/{i}")

    content4 = loads(test4.text)

    assert test4, (f"Error al realizar [GET] /habilitacion/capacitaciones/{i}.\n"
                   "Status code = {test1.status_code}")

    vprint(f"Test {2*(i-1)+1}/8 exitoso.")

    assert content4 == test_capacitaciones[i-1], (f"Error al realizar [GET] /habilitacion/capacitaciones/{i}.\n"
                                                  "El contenido del response no es lo esperado.")

    vprint(f"Test {2*(i-1)+2}/8 exitoso.")

vprint(f"Probando: [GET] {URL}/habilitacion/recursos/<id_capacitacion>")
for i in range(1, 5):
    test4 = get(URL+f"/habilitacion/recursos/{i}")

    content4 = loads(test4.text)

    assert test4, (f"Error al realizar [GET] /habilitacion/recursos/{i}.\n"
                   "Status code = {test1.status_code}")

    vprint(f"Test {2*(i-1)+1}/8 exitoso.")

    assert content4 == BD_recursos[str(i)], (f"Error al realizar [GET] /habilitacion/recursos/{i}.\n"
                                             "El contenido del response no es lo esperado.")

    vprint(f"Test {2*(i-1)+2}/8 exitoso.")

vprint(f"Probando: [GET] {URL}/habilitacion/capacitaciones/<id_capacitado>")
for i in range(1, 5):
    for j in range(1, 5):
        test6 = get(URL+f"/habilitacion/capacitado/{i}/{j}")

        content6 = loads(test6.text)

        assert test6, (f"Error al realizar [GET] /habilitacion/capacitado/{i}/{j}.\n"
                       "Status code = {test1.status_code}")

        vprint(f"Test {8*(i-1)+2*(j-1)+1}/32 exitoso.")

        assert content6 == (i in BD_capacitados[str(j)]), (f"Error al realizar [GET] /habilitacion/capacitado/{i}/{j}.\n"
                                                           "El contenido del response no es lo esperado.")

        vprint(f"Test {8*(i-1)+2*(j-1)+2}/32 exitoso.")
