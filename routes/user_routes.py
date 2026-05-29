from flask import Blueprint, request, jsonify
from db.crud import get_all_users, get_user_by_id, add_to_user

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')

@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    user = add_to_user(name=name, email=email)
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201