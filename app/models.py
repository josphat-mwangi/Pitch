from . import db,login_manager
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(150)
    )
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(10),nullable=False)
    # pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    # comments = db.relationship('Comment', backref='user', lazy="dynamic")
    pass_secure = db.Column(db.String(255))
    # profile_pic_path = db.Column(db.String(),nullable=False,default='default.jpg')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()    




    def __repr__(self):
        return f"User '({self.username}','{self.email}')"

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.String(1000))
    # category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # comment = db.relationship('Comment', backref='pitches', lazy='dynamic')
    # upvote = db.relationship('Upvote', backref='pitches', lazy='dynamic')
    # downvote = db.relationship('Downvote', backref='pitches', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_pitches(cls):
        return Pitch.query.all()

    def __repr__(self):
       return f"Pitch '({self.title}','{self.data}','{self.upvote}','{self.downvote}')"
        



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __repr__(self):
        return f"Comment '({self.username}', '{self.email}', '{self.image_file}')"

   


class Upvotes(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes = Upvotes.query.filter_by(pitch_id=id).all()

        return upvotes


class Downvotes(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        downvotes = Downvotes.query.filter_by(pitch_id=id).all()

        return downvotes

class Category(db.Model):
    __tablename__='categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))
    # pitches = db.relationship('Pitch', backref='parent_category', lazy='dynamic')

    def save_category(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()

        return categories



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)




