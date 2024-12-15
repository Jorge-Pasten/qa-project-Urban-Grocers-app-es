# Proyecto Urban Grocers


## Descripción
El proyecto realiza pruebas positivas y negativas en la aplicación urban grocers especificamente en el campo "name" cuando se crea un kit de productos.

---

## Instrucciones

- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.

---

### Lista de comprobación

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