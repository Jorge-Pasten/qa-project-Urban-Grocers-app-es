# Urban Grosers - Pruebas Automatizadas con Pytest


## Descripción
Este proyecto forma parte del séptimo sprint en el proceso de QA Engineer de TripleTen para la aplicación de pedidos de comida Urban Grosers. La tarea principal consiste en automatizar las pruebas de la funcionalidad de creación de kits de productos mediante pytest. Se implementaron tanto pruebas positivas como negativas basadas en una lista de comprobación previamente definida.

El objetivo es garantizar que el campo name en la solicitud de creación de un kit de productos funcione correctamente bajo diferentes escenarios, asegurando que la API maneje adecuadamente los valores válidos e inválidos.

## Tecnologías Utilizadas
- Python (para la automatización de pruebas)
- Pytest (framework de pruebas)
- Requests (para el envío de solicitudes HTTP)
- Git y GitHub (para control de versiones y almacenamiento del código)

## Estructura del Proyecto
```
qa-project-Urban-Grosers-app-es/
│-- configuration.py         # Configuración de la URL del servidor y rutas de solicitud.
│-- data.py                  # Datos de prueba reutilizables
│-- sender_stand_request.py   # Funciones para enviar solicitudes a la API
│-- create_kit_name_test.py   # Archivo con las pruebas automatizadas
│-- .gitignore                # Archivos y carpetas a ignorar en Git
│-- README.md                 # Documentación del proyecto
```


## Casos de Prueba Implementados
Los casos de prueba se basan en la siguiente lista de comprobación:

| №    | Description                                                                               | ER: | 
|------|-------------------------------------------------------------------------------------------|-| 
| 1    | **El número permitido de caracteres (1):** kit_body = { "name": "a"}                      |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 2    | **El número permitido de caracteres (511):** kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 3    | **El número de caracteres es menor que la cantidad permitida (0):** kit_body = { "name": "" }	 |Código de respuesta: 400|
| 4    | **El número de caracteres es mayor que la cantidad permitida (512):** <br/>kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } |Código de respuesta: 400|
| 5    | **Se permiten caracteres especiales:** kit_body = { "name": ""№%@"," }	                   |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 6    | **Se permiten espacios:** kit_body = { "name": " A Aaa " }	                               |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 7    | **Se permiten números:** kit_body = { "name": "123" }	                                    |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 8    | **El parámetro no se pasa en la solicitud:** kit_body = { }	                              |Código de respuesta: 400|
| 9    | **Se ha pasado un tipo de parámetro diferente (número):** kit_body = { "name": 123 }	     |Código de respuesta: 400|


## Instalación y Ejecución de las Pruebas
### 1️⃣ Clonar el repositorio
```bash
git clone git@github.com:tu_usuario/qa-project-Urban-Grosers-app-es.git
cd qa-project-Urban-Grosers-app-es
```

### 2️⃣ Instalar dependencias
Se recomienda utilizar un entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scriptsctivate
pip install -r requirements.txt
```

### 3️⃣ Configurar la URL del servidor
Actualizar el archivo `configuration.py` con la URL obtenida al iniciar el servidor de Urban Grosers.

### 4️⃣ Ejecutar pruebas con pytest
```bash
pytest -v
```

## Autor
Proyecto realizado por **Jorge Luis Pasten Peña** como parte del proceso de aprendizaje en QA Engineer de TripleTen.
