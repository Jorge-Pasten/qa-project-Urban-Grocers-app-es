import sender_stand_request
import data

# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

def get_new_user_token():
    user_body = get_user_body('Camila')
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    current_headers_kit = data.headers_kit.copy()
    current_headers_kit["Authorization"] = "Bearer "+ auth_token
    return current_headers_kit


def get_body_kit(name):
    current_body_kit = data.body_kit.copy()
    current_body_kit["name"] = name
    return current_body_kit


def positive_assert(name):
    headers_kit1 = get_new_user_token()
    body_kit1 = get_body_kit(name)
    kit_response = sender_stand_request.post_new_client_kit(headers_kit1,body_kit1)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201


def negative_assert_code_400(name):
    headers_kit1 = get_new_user_token()
    body_kit1 = get_body_kit(name)
    response = sender_stand_request.post_new_client_kit(headers_kit1,body_kit1)
    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

def negative_assert_no_name(name):
    headers_kit1 = get_new_user_token()
    body_kit1 = get_body_kit(name)
    body_kit1.pop("name")
    response = sender_stand_request.post_new_client_kit(headers_kit1,body_kit1)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("A Aaa")

def test_create_kit__has_number_in_name_get_success_response():
    positive_assert("123")

def test_create_kit_no_name_get_error_response():
    negative_assert_no_name("")

def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(1234)
