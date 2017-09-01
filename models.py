from app import db, bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

"""class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '{}-{}'.format(self.title, self.description)"""


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String, nullable=False)
    album = db.Column(db.String, nullable=False)
    cover = db.Column(db.String, nullable=True)
    header = db.Column(db.String, nullable=True)
    paragraph_1 = db.Column(db.String, nullable=True)
    paragraph_2 = db.Column(db.String, nullable=True)
    paragraph_3 = db.Column(db.String, nullable=True)
    paragraph_4 = db.Column(db.String, nullable=True)
    paragraph_5 = db.Column(db.String, nullable=True)
    paragraph_6 = db.Column(db.String, nullable=True)
    listen = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)
    rate = db.Column(db.String, nullable=True)
    language = db.Column(db.String, nullable=True)
    artist_link = db.Column(db.String, nullable=True)
    album_link = db.Column(db.String, nullable=True)

    def __init__(self, artist=None, album=None, cover=None, header=None, paragraph_1=None, paragraph_2=None, 
    paragraph_3=None, paragraph_4=None, paragraph_5=None, paragraph_6=None, listen=None, date=None, 
    rate=None, language='PL', artist_link=None, album_link=None):
        self.artist = artist
        self.album = album
        self.cover = cover
        self.header = header
        self.paragraph_1 = paragraph_1
        self.paragraph_2 = paragraph_2
        self.paragraph_3 = paragraph_3
        self.paragraph_4 = paragraph_4
        self.paragraph_5 = paragraph_5
        self.paragraph_6 = paragraph_6
        self.listen = listen
        self.date = date
        self.rate = rate
        self.language = language
        self.artist_link = artist_link
        self.album_link = album_link
        
    
    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.artist, self.album, self.cover, self.header, self.paragraph_1, 
            self.paragraph_2, self.paragraph_3, self.paragraph_4, self.paragraph_5, self.paragraph_6, 
            self.listen, self.date, self.rate, self.language, self.artist_link, self.album_link)

class Post(db.Model):
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)    
    paragraph_1 = db.Column(db.String, nullable=True)
    paragraph_2 = db.Column(db.String, nullable=True)
    paragraph_3 = db.Column(db.String, nullable=True)
    paragraph_4 = db.Column(db.String, nullable=True)
    paragraph_5 = db.Column(db.String, nullable=True)
    paragraph_6 = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)
    language = db.Column(db.String, nullable=True)
    title_link = db.Column(db.String, nullable=True)
    

    def __init__(self, title=None, paragraph_1=None, paragraph_2=None, 
    paragraph_3=None, paragraph_4=None, paragraph_5=None, paragraph_6=None, date=None, 
    language='PL', title_link=None):
        self.title = title
        self.paragraph_1 = paragraph_1
        self.paragraph_2 = paragraph_2
        self.paragraph_3 = paragraph_3
        self.paragraph_4 = paragraph_4
        self.paragraph_5 = paragraph_5
        self.paragraph_6 = paragraph_6        
        self.date = date        
        self.language = language
        self.title_link = title_link
        
        
    
    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.title, self.paragraph_1, 
            self.paragraph_2, self.paragraph_3, self.paragraph_4, self.paragraph_5, self.paragraph_6, 
            self.date, self.language, self.title_link)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)    

    def __init__(self, name, password):
        self.name = name
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name {}'.format(self.name)