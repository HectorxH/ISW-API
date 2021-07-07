.. ISW-API documentation master file, created by
   sphinx-quickstart on Tue Jul  6 20:11:54 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentación de API para el ramo ISW-INF225
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Métodos
~~~~~~~~

+++++++++++++

.. http:get:: habilitacion/capacitados

    Obtener ids de personas capacitadas en cada habilitación

    **Example request**:

    .. tabs::

        .. code-tab:: bash

            $ curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitados'

    **Example response**:

    .. sourcecode:: json

        {
           "1": [3, 4],
           "2": [],
           "3": [3, 7, 5],
           "4": [7],
           "5": [3, 5],
           "6": [1, 2, 3, 5]
        }

    :None

    



