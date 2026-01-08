from flask import Blueprint, jsonify, request
from app.models.user import LoginPayload
from app.models.products import *
from pydantic import ValidationError
from app import db
from bson import ObjectId

main_bp = Blueprint('main_bp', __name__)


#RF: O sistema deve permitir que o usuario se autentique para obter um token
@main_bp.route('/login',methods=['POST'])
def login():
    try:
        raw_date = request.get_json()
        user_data = LoginPayload(**raw_date)
    except ValidationError as e:
        return jsonify({"error": e.errors*()}), 400
    except Exception as e:
        jsonify({"error": "Erro durante dos dados"}), 500

    if user_data.username == "admin" and user_data.password == "123":
        return jsonify({"message":f"Login Realizado"})
    else:
        return jsonify({"message":f"Credenciais Invalidas"})
    

#RF: O sistema deve permitir a listagem de todos os produtos
@main_bp.route('/products', methods = ['GET'])
def get_product():
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)

#RF: O sistema deve permitir criar um novo produto
@main_bp.route('/products', methods = ['POST'])
def create_product():
    return jsonify({'message':'Rota de criação de produtos'})

#RF: O sistema deve permitir a visualização de um unico produto
@main_bp.route('/product/<string:product_id>', methods = ['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({'error':f'Erro ao transformar o  {product_id} em objeto: {e}'})

    product = db.products.find_one({"_id":oid})

    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product_model)
    else:
        return jsonify({'error':'Produto não encontrado'})
    

#RF: O sistema deve permitir a atualização de um unico produdo
@main_bp.route('/products/<int:product_id>', methods = ['PUT'])
def update_product(product_id):
    return jsonify({f'message':'Está é a rota de atualização do produto {product_id}'})

#RF: O sistema deve permitir a declaração de um unico produto e produto existente
@main_bp.route('/products/<int:product_id>', methods = ['DELETE'])
def delete_product(product_id):
    return jsonify({f'message':'Está é a rota de deletação do produto {product_id}'})

#RF: O sistema deve permitir a importação de vendas atravez de um arquivo
@main_bp.route('/products/upload', methods = ['POST'])
def upload_product(product_id):
    return jsonify({f'message':'Está é a rota de upload do arquivo de vendas'})



@main_bp.route('/')
def index():
    return jsonify({'message':'Seja bem vindo'})


