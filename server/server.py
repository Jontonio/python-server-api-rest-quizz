import os
from flask import Flask
from dotenv import load_dotenv
from routes.auth import auth_bp
from routes.institution import instituion_bp
from jwt_handlers.jwt_handler import jwt

load_dotenv()

app = Flask(__name__)

app_contex_version = '/api/v1'

# Configura el secret token JWT
app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')

jwt.init_app(app)

# Registrando los Blueprints
app.register_blueprint(auth_bp, url_prefix=app_contex_version+'/auth')
app.register_blueprint(instituion_bp, url_prefix=app_contex_version+'/institution')

