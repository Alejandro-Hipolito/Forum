from flask import Flask, request, url_for, jsonify, Blueprint
from .models import User, Image, Post, Reply, Category, Subcategory
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_access_token, JWTManager
from flask_login import UserMixin
from website.templates import db
app = Flask(__name__)

api = Blueprint('api', __name__)


@api.route('/signup', methods=['POST'])
def signup():
    
    #Request the data
    data = request.get_json()
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    #Verify if the user already exists by the username/email
    email_comprobation = User.query.filter_by(email=email).first()
    if email_comprobation:
        return jsonify({'message' : 'This email has already been used'})
    
    username_comprobation = User.query.filter_by(username=username).first()
    if username_comprobation:
        return jsonify({'msg':'This username has already been used'})
    
    #Create the user
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'msg':'User registered successfully'}), 201
    

