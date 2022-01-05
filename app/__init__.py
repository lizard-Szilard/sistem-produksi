from flask import Flask
from app.pesanan import pesanan_blueprint
from app.material import material_blueprint
from app.customer import customer_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pesanan_blueprint)
    app.register_blueprint(material_blueprint)
    app.register_blueprint(customer_blueprint)

    return app
