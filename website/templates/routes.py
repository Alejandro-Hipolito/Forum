from flask import Flask, request, url_for, jsonify, Blueprint
from .models import User, Image, Post, Reply, Category, Subcategory
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_access_token, JWTManager
from flask_login import UserMixin
from website.templates import db
app = Flask(__name__)

api = Blueprint('api', __name__)


#-------------------- USER --------------------

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
    

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    
    serialized_users = [user.serialize() for user in users]
    return jsonify({'users': serialized_users})


@api.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    
    if user is None:
        return jsonify({'msg':f'None of the existing users have the id={id}'}), 401
    
    serialized_user = user.serialize()
    
    return jsonify(serialized_user), 200
    
    
@api.route('/user/<int:id>/modify', methods=['PUT'])
def edit_user(id):
#@jwt_required --- Future
    user = User.query.get(id) #Modify in the future, change id to JWT
    
    if user is None:
        return jsonify({'msg':f'None of the existing users have the id={id}'}), 401
    
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    #change of password have to be with more security, not here
    avatar = data.get('avatar')
    
    if username:
        user.username = username 
        
    if email:
        user.email = email
        
    if phone:
        user.phone = phone
        
    if avatar:
        user.avatar = avatar
        
    try:
        db.session.commit()
        return jsonify({'msg':'User updated successfully'}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': f'Error updating user: {str(e)}'}), 500
    
    
    


@api.route('/user/<int:id>', methods=['DELETE'])
#@jwt_required
def del_user(id):
    user = User.query.get(id) #User searched by their id
    
    if user is None:
        return jsonify({'msg':f'None of the existing users have the id={id}'}), 401
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'msg':f'The user with the id={id} ({user.username}) has been successfully deleted'}), 200




#-------------------- POST --------------------

@api.route('/create-post', methods=['POST'])
def create_post():
    data = request.get_json()

    title = data.get('title')
    description = data.get('description')
    created_by = data.get('user_id')
    images_data = data.get('images')
    replies_data = data.get('replies')

    if created_by is None:
        return jsonify({'msg': f'None of the existing users have the id={id} ({created_by})'})

    # Verificar si images_data y replies_data son None antes de iterar
    images = [Image(url=image_data['url']) for image_data in images_data] if images_data else []
    replies = [Reply(text=reply_data['text']) for reply_data in replies_data] if replies_data else []

    # Creación del post con objetos Image y Reply
    new_post = Post(
        title=title,
        description=description,
        user_id=created_by,
        images=images,
        replies=replies
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({'msg': 'The post has been created successfully'})


@api.route('/posts', methods=['GET'])
def get_posts():
    
    posts = Post.query.all()
    
    serialized_posts = [post.serialize() for post in posts]
    
    return jsonify({'posts':serialized_posts})


@api.route('/delete-post/<int:id>', methods=['DELETE'])
def delete_post(id):
    
    post = Post.query.get(id)
    
    if post is None:
        return jsonify({"msg":f'The post with the id={id} does not exist.'})
    
    db.session.delete(post)
    db.session.commit()
    
    return jsonify({'msg':f'The post with the id={id} "{post.title}" has been successfully deleted'})
    