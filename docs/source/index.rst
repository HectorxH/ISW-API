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
Projects
~~~~~~~~

Projects list
+++++++++++++

.. http:get:: /api/v3/projects/

    Retrieve a list of all the projects for the current logged in user.

    **Example request**:

    .. tabs::

        .. code-tab:: bash

            $ curl -H "Authorization: Token <token>" https://readthedocs.org/api/v3/projects/

        .. code-tab:: python

            import requests
            URL = 'https://readthedocs.org/api/v3/projects/'
            TOKEN = '<token>'
            HEADERS = {'Authorization': f'token {TOKEN}'}
            response = requests.get(URL, headers=HEADERS)
            print(response.json())

    **Example response**:

    .. sourcecode:: json

        {
            "count": 25,
            "next": "/api/v3/projects/?limit=10&offset=10",
            "previous": null,
            "results": [{
                "id": 12345,
                "name": "Pip",
                "slug": "pip",
                "created": "2010-10-23T18:12:31+00:00",
                "modified": "2018-12-11T07:21:11+00:00",
                "language": {
                    "code": "en",
                    "name": "English"
                },
                "programming_language": {
                    "code": "py",
                    "name": "Python"
                },
                "repository": {
                    "url": "https://github.com/pypa/pip",
                    "type": "git"
                },
                "default_version": "stable",
                "default_branch": "master",
                "subproject_of": null,
                "translation_of": null,
                "urls": {
                    "documentation": "http://pip.pypa.io/en/stable/",
                    "home": "https://pip.pypa.io/"
                },
                "tags": [
                    "disutils",
                    "easy_install",
                    "egg",
                    "setuptools",
                    "virtualenv"
                ],
                "users": [
                    {
                        "username": "dstufft"
                    }
                ],
                "active_versions": {
                    "stable": "{VERSION}",
                    "latest": "{VERSION}",
                    "19.0.2": "{VERSION}"
                },
                "_links": {
                    "_self": "/api/v3/projects/pip/",
                    "versions": "/api/v3/projects/pip/versions/",
                    "builds": "/api/v3/projects/pip/builds/",
                    "subprojects": "/api/v3/projects/pip/subprojects/",
                    "superproject": "/api/v3/projects/pip/superproject/",
                    "redirects": "/api/v3/projects/pip/redirects/",
                    "translations": "/api/v3/projects/pip/translations/"
                }
            }]
        }

    :query string language: language code as ``en``, ``es``, ``ru``, etc.
    :query string programming_language: programming language code as ``py``, ``js``, etc.

    The ``results`` in response is an array of project data,
    which is same as :http:get:`/api/v3/projects/(string:project_slug)/`.

    .. note::

       .. FIXME: we can't use :query string: here because it doesn't render properly

      :doc:`Read the Docs for Business </commercial/index>`, also accepts

      :Query Parameters:

         * **expand** (*string*) -- with ``organization`` and ``teams``.

   

GET habilitacion/capacitados
+++++++++++++
.. http:get:: /habilitacion/{id_persona}{id_capacitacion}

    étodo que permite revisar si una persona de `id = id_persona` ha realizado la capacitación de `id = id_capacitacion`
    **Request de ejemplo**:

    .. tabs::

        .. code-tab:: bash

            $ curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitado/3/2'

    **Ejemplo de respuesta**:

    .. sourcecode:: json

        false
   
    



