from . import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(150)
    )
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(10),nullable=False)
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy="dynamic")
    pass_secure = db.Column(db.String(255))
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f"User '({self.username}','{self.email}','{self.image_file}')"

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.relationship('Comment', backref='pitches', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='pitches', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='pitches', lazy='dynamic')

    def __repr__(self):
       return f"Pitch '({self.title}','{self.data}','{self.upvote}','{self.downvote}')"
        



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Comment '({self.username}', '{self.email}', '{self.image_file}')"

   


class Upvotes(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

   
    



class Downvotes(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))


@login_manager.user_loader
def load_user(user_id):
    return.User.query.get(user_id)




