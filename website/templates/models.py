from . import db 
from flask_login import UserMixin #Implements properties and methods of flask-login to make it easier
from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from flask_migrate import Migrate


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
    password = db.Column(db.String(150), nullable=False)
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
            "role": self.role.value if self.role else None,
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
    
    def __repr__(self):
        return f'<Image {self.id}>'
    
    def serialize(self):
        return{
            "id": self.id,
            "url": self.url,
            "user_id": self.user_id,
            "post_id": self.post_id
            
        }

    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(2500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    #------One to many relationships------
    images = db.relationship('Image', backref='post', cascade="all, delete-orphan") #cascade parameter = if a post is deleted, it's imgs and replies too
    replies = db.relationship('Reply', backref='post', cascade="all, delete-orphan") 
    
    
    def __repr__(self):
        return f'<Post {self.id}'
    
    def serialize(self):
        return{
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "category_id": self.category_id,
            # "images": self.images,
            "images": [image.serialize() for image in self.images],
            "replies": [reply.serialize() for reply in self.replies]
        }

        
    


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    
    def __repr__(self):
        return f'<Reply {self.id}'
    
    def serialize(self):
        return{
            "id": self.id,
            "text": self.text,
            "user_id": self.user_id,
            "post_id": self.post_id
        }
    
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    # parent_id = db.Column(db.Integer, db.ForeignKey())
    subcategory = db.relationship('Subcategory', backref='category')
    
    def __repr__(self):
        return f'<Category {self.id}'
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "subcategory": self.subcategory
        }
    
class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    def __repr__(self):
        return f'<Category {self.id}'
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "category_id": self.category_id
        }
