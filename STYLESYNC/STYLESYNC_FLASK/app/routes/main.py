import jwt
import csv
import os
import io

from app.models.user import LoginPayload
from app.models.products import *
from app.models.sale import Sale

from app.decorators import token_required

from app import db
from bson import ObjectId
from pydantic import ValidationError
from datetime import datetime, timedelta, timezone
from flask import Blueprint, jsonify, request, current_app

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
        token = jwt.encode(
            {
                "user_id": user_data.username,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )

        return jsonify({"access_token": token}), 200
    
    return jsonify({"message":f"Credenciais Invalidas"})
    
#RF: O sistema deve permitir a listagem de todos os produtos
@main_bp.route('/products', methods = ['GET'])
def get_product():
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)

#RF: O sistema deve permitir criar um novo produto
@main_bp.route('/products', methods = ['POST'])
@token_required
def create_product(token):
    try:
        product = Product(**request.get_json())
    except ValidationError as e:
        return jsonify({'error':e.errors()})

    result = db.products.insert_one(product.model_dump())

    return jsonify({'message':'Rota de criação de produtos',
                    "id": str(result.inserted_id)}),201

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
@main_bp.route('/products/<string:product_id>', methods = ['PUT'])
@token_required
def update_product(token, product_id):
    try:
        oid = ObjectId(product_id)
        udate_data = UpdateProduct(request.get_json())
    except ValidationError as e:
        return jsonify({'error':e.errors()})

    update_result = db.products.update_one(
        {"_id": oid},
        {"$set": udate_data.model_dump(exclude_unset=True)}
    )

    if update_result.matched_count == 0:
        return jsonify({'error':'Produto não encontrado'}),404

    db.products.find_one({"_id": oid})
    return jsonify(ProductDBModel(**update_product).model_dump(by_alias=True, exclude=None))

#RF: O sistema deve permitir a declaração de um unico produto e produto existente
@main_bp.route('/products/<string:product_id>', methods = ['DELETE'])
@token_required
def delete_product(token, product_id):
    try: 
        oid = ObjectId(product_id)
    except Exception:
        return jsonify({'error':'id do produto invalida'}), 400

    delete_product = db.products.delete_one({"_id": oid})

    if delete_product.deleted_count == 0:
         return jsonify({'error':'Produto não foi encontrado'}), 404

    return "", 204

#RF: O sistema deve permitir a importação de vendas atravez de um arquivo
@main_bp.route('/products/upload', methods = ['POST'])
@token_required
def upload_product(token):
    if "file" not in request.files:
        return jsonify({f'error':'Nenhum arquivo foi enviado'}), 400

    file =  request.files["file"]

    if file.filename == "":
        return jsonify({f'error':'Nenhum arquivo foi selecionado'}), 400

    if file and file.filename.endswith(".csv"):
        csv_strean = io.StringIO(file.stream.read().decode("UTF-8"),newline=None)
        csv_reader = csv.DictReader(csv_strean)

        sales_to_insert = []
        error = []

        for row_num, row in enumerate(csv_reader, 1):
            try:
                sale_data = sale(**row)

                sales_to_insert.append(sale_data.model_dump())
            except ValidationError as e:
                error.append(f"Linhas {row_num} com dados invalidos")
            except Exception as e:
                error.append(f"LinhA {row_num} com erro nos dados")

        if sales_to_insert:
            try:
                db.sales.insert_many(sales_to_insert)
            except Exception as e:
                return jsonify({'error':f"{e}"})
            return jsonify({
                    "message": "Upload realizado com sucesso",
                    "vendas importadas": len(sales_to_insert),
                    "erros encontrados": error
            }),200

    return jsonify({f'message':'Está é a rota de upload do arquivo de vendas'})

@main_bp.route('/')
def index():
    return jsonify({'message':'Seja bem vindo'})


