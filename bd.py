BD_capacitaciones = {
    1: {"Nombre": "Capacitacion Impresora 1", "Descripcion": "descripcion", "Tipos de maquinas": "Impresora 3D", "Ayudantes": 1},
    2: {"Nombre": "Capacitacion Impresora 2", "Descripcion": "descripcion", "Tipos de maquinas": "Impresora 3D", "Ayudantes": 3},
    3: {"Nombre": "Capacitacion Torno 1", "Descripcion": "descripcion", "Tipos de maquinas": "Torno", "Ayudantes": 2},
    4: {"Nombre": "Capacitacion Cortadora 1", "Descripcion": "descripcion", "Tipos de maquinas": "Cortadora laser", "Ayudantes": 4},
    5: {"Nombre": "Capacitacion Impresora 3", "Descripcion": "descripcion", "Tipos de maquinas": "Impresora 3D", "Ayudantes": 4},
    6: {"Nombre": "Capacitacion Cortadora 2", "Descripcion": "descripcion", "Tipos de maquinas": "Cortadora laser", "Ayudantes": 3}
}

BD_capacitados = {1: set([3, 4]), 2: set([]), 3: ([
    3, 7, 5]), 4: set([7]), 5: set([3, 5]), 6: set([1, 2, 3, 5])}

BD_recursos = {
    1: [{"id": 1, "Nombre": "recurso 1", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}, {"id": 2, "Nombre": "recurso 2", "Descripcion": "descripcion", "Formato": "ppt", "Link": "url_prueba.com"}, {"id": 3, "Nombre": "recurso 3", "Descripcion": "descripcion", "Formato": "mov", "Link": "url_prueba.com"}],
    2: [{"id": 4, "Nombre": "recurso 4", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}, {"id": 5, "Nombre": "recurso 5", "Descripcion": "descripcion", "Formato": "mov", "Link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"id": 6, "Nombre": "recurso 6", "Descripcion": "descripcion", "Formato": "ppt", "Link": "url_prueba.com"}],
    3: [{"id": 7, "Nombre": "recurso 7", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
    4: [{"id": 8, "Nombre": "recurso 8", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
    5: [{"id": 9, "Nombre": "recurso 9", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
    6: [{"id": 10, "Nombre": "recurso 10", "Descripcion": "descripcion", "Formato": "pdf", "Link": "url_prueba.com"}],
}
