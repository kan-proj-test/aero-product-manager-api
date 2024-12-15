# main.py

from flask import Flask
from src.api.routes import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

def lambda_handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run()