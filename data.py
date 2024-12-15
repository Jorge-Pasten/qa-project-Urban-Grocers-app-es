#Información que se envía en la solicitud
headers = {
    "Content-Type": "application/json"
} #Encabezado de solicitud POST

#Cuerpo de solicitud POST
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}


#Información que se envía en la solicitud crear kit
headers_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}

body_kit = {
    "name": "Mi conjunto",
    "card": {
        "id": 1,
        "name": "Para la situación"
    },
    "productsList": None,
    "id": 7,
    "productsCount": 0
}