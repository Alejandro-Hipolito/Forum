from . import db 
from flask_login import UserMixin #Implements properties and methods of flask-login to make it easier
from flask_sqlalchemy import SQLAlchemy
from enum import Enum


class UserRole(Enum):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
    MOD = 'Mod'
    SUPERUSER = 'Superuser'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.Integer)
    password = db.Column(db.String(150))
    is_active = db.Column(db.Boolean, default=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.BASIC)

    #avatar = db.Column(db.String(400))

    #------Foreign Keys------
    avatar = db.Column(db.Integer, db.ForeignKey('image.id'))
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

def __repr__(self):
    return f'<User {self.email}>'

def serialize(self): #Return the object serialized in dict/JSON 
    return{
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "phone": self.phone,
        "is_active": self.is_active,
        "role": self.role,
        "avatar": self.avatar
    }

    
    
    

# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(2500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #------One to many relationships------
    images = db.relationship('Image', backref='post') #
    replies = db.relationship('Reply', backref='post') 
    


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    # parent_id = db.Column(db.Integer, db.ForeignKey())
    
class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
