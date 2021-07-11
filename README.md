# API Experimental ISW225-SJ27

## About
API experimental de Habilitaciones, con el endpoint público en AWS

#### Intregantes
- Anastasiia Fedorova  201873505-1  
<anastasiia.fedorova@sansano.usm.cl>
- Héctor Larrañaga 201873623-6  
<hector.larranaga@sansano.usm.cl>

Proyecto de ramo *Ingeniería de Software: INF 225* <br/>
Universidad Técnica Santa María <br/>
2021-1

### Instrucciones de uso:
La API posee el enpoint público en AWS. La documentación de la API se encuentra [en Read The Docs](https://isw-api.readthedocs.io/es/main/)

#### Métodos implementados:
Método GET /habilitacion/capacitaciones - método que se encarga de entregar todas las capacitaciones existentes en el sistema  
```curl
curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitaciones'
```
Método GET /habilitacion/capacitados - método que permite obtener todos los ids de las personas capacitadas para una capacitación de id consultado
```curl
curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitados'
```
Método GET /habilitacion/capacitados/{id_capacitacion} - método que permite obtener las personas capacitadas para la capacitación de id=X.
```curl
curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitados/3'
``` 

Método GET /habilitacion/capacitaciones/{id_capacitado} - método que permite obtener todas las capacitaciones realizadas por una persona de id consultado. Recibe el id como parámetro. Un ejemplo de request para id=3 sería:
```curl
curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitaciones/3'
```

Método GET /habilitacion/recursos/{id_capacitacion} - método que permite obtener todos los recursos asociados a una capacitación de id consultado
```curl
curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/recursos/2
```

Método GET /habilitacion/capacitado/{id_persona}/{id_capacitacion} - método que permite revisar si una persona de id=X ha realizado la capacitación de id=Y. Por ejemplo, para revisar si la persona con id=3 tiene capacitación deid=2podemos hacer el siguiente request:
```curl
curl --location --request GET 'ec2-18-221-241-253.us-east-2.compute.amazonaws.com:8000/habilitacion/capacitado/3/2'
```