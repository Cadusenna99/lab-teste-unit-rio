from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Substitua pela sua chave secreta
jwt = JWTManager(app)

# Configuração do Swagger UI
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Rota principal
@app.route('/')
def home():
    return jsonify(message="API is running")

# Rota para obter itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=["item1", "item2", "item3"])

# Rota de login para gerar token JWT
@app.route('/login', methods=['POST'])
def login():
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token)

# Rota protegida, só acessível com token JWT válido
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1313)
