from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({'message':'Seja bem vindo'})

@main_bp.route('/products')
def get_product():
    return jsonify({'message':'Está é a rota de lsitagem de produtos'})

@main_bp.route('/login',methods=['POST'])
def login():
    return jsonify({'message':'Está é a rota de lsitagem de logins'})