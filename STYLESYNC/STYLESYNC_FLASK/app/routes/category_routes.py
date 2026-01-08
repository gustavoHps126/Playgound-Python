from flask import Blueprint, jsonify, request

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/category', methods = ["GET"])
def get_category():
    return jsonify({f'message':'Está é a rota de adição de categoria'})