from functools import wraps
from flask import request, jsonify, current_app
import jwt

def token_required(f):
    @wraps
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Autorization"]
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"Message":f"Token malformado"})
        if not token:
            return jsonify({"error":f"Token não encontrado"}), 401

        try:
           data = jwt.decode(token, current_app.config["SECRET_KEY"],algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error":f"Token Expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error":f"Token invalido"}), 401

        return f(data, *args, **kwargs)

    return decorated
