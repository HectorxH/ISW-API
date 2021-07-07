.. ISW-API documentation master file, created by
   sphinx-quickstart on Tue Jul  6 20:11:54 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

API v1
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Métodos
--------------------------------

GET habilitacion/capacitados
+++++++++++++
.. http:get:: habilitacion/capacitados
    Obtiene los ids de personas capacitadas en cada habilitación
    Retorna un JSON con listas de personas capacitadas asociadas a los ids de las capacitaciones disponibles.  
   
    **Request de ejemplo**:

    .. tabs::

        .. code-tab:: bash

            $ curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitados'
   
    **Ejemplo de respuesta**:
    
    .. sourcecode:: json

        {
           "1": [3, 4],
           "2": [],
           "3": [3, 7, 5],
           "4": [7],
           "5": [3, 5],
           "6": [1, 2, 3, 5]
        }

GET habilitacion/capacitados
+++++++++++++
.. http:get:: /habilitacion/{id_persona}{id_capacitacion}
   :param id_personas: post's unique id
   :type id_persona: int
   :param id_capacitacion: post's unique id
   :type id_capacitacion: int
   
    Método que permite revisar si una persona de `id = id_persona` ha realizado la capacitación de `id = id_capacitacion`.
    Retorna un booleano correspondiente al valor de evaluación de si la persona realizó la capacitación o no.  
    
    **Request de ejemplo**:

    .. tabs::

        .. code-tab:: bash

            $ curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitado/3/2'

    **Ejemplo de respuesta**:

    .. sourcecode:: json

        false
   
    



