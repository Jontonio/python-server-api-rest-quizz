from flask import Blueprint
from my_class.HttpResponse import HttpResponse

response = HttpResponse()

instituion_bp = Blueprint('institution', __name__)

@instituion_bp.route("/", methods=['GET'])
def index():
    return response.res_success("Institution index - GET", 200, None)

@instituion_bp.route("/<id>", methods=['GET'])
def show(id):
    return response.res_success("Institution show - GET", 200, None)

@instituion_bp.route("/", methods=['POST'])
def store():
    return response.res_success("Institution store - POST", 201, None)

@instituion_bp.route("/<id>", methods=['PATCH'])
def update(id):
    return response.res_success("Institution update - PATCH", 200, None)

@instituion_bp.route("/<id>", methods=['DELETE'])
def destroy(id):
    return response.res_success("Institution update - DELETE", 200, None)
