from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from middlewares.validation_data import required_params
from my_class.HttpResponse import HttpResponse

response = HttpResponse()

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST"])
@required_params({"password":str, "username":str})
def login():

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != "jose@gmail.com" or password != "test":
        return response.res_error("Nombre de usuario o contraseña incorrectos", 401, None)

    additional_claims = {"id": "10", "role": "admin"}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return response.res_success("Login", 200, {"access_token": access_token})

@auth_bp.route("/logout", methods=["GET"])
@jwt_required()
def logout():
    return jsonify({
        "message": "Logout route"
    }), 200
