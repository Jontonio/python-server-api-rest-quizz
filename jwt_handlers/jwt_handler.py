from flask_jwt_extended import JWTManager
from my_class.HttpResponse import HttpResponse

jwt = JWTManager()

response = HttpResponse()

@jwt.expired_token_loader
def expired_token_callback(expired_token):
    return response.res_success("Token expirado", 401, None)

@jwt.invalid_token_loader
def invalid_token_callback(invalid_token):
    return response.res_success("Token inválido", 401, None)

@jwt.unauthorized_loader
def unauthorized_callback(unauthorized_message):
    return response.res_success("Acceso denegado, se necesita un token", 401, None)
