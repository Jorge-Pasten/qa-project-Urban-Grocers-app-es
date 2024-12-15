import configuration
import requests
import data


#Función que crea usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


#Función que crea un kit
def post_new_client_kit(headers_kit, body_kit):
    # inserta la dirección URL completa
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body_kit, #inserta el cuerpo de solicitud
                         headers=headers_kit)  #inserta los encabezados