from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask_sqlalchemy import SQLAlchemy
import os
from functools import wraps
from datetime import datetime
from pytz import timezone
import re


app = Flask(__name__)

#config
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

poland = timezone('Europe/Warsaw')

from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods=['GET'])
def index():
    date = str(datetime.now(poland))[:-22]
    css = url_for('static', filename='button.css')
    posts = db.session.query(Post).all()
    posts = posts[-3:][::-1]
    return render_template('index.html', posts=posts, css=css, date=date)
    result = Post.query.order_by("id desc")
    id_1 = result.first().id
    title_1 = Post.query.filter_by(id=id_1).first().title
    cut_1 = Post.query.filter_by(id=id_1).first().paragraph_1[0:50] + "..."
    title_link_1 = Post.query.filter_by(id=id_1).first().title_link
    
    id_2 = id_1 - 1
    title_2 = Post.query.filter_by(id=id_2).first().title
    cut_2 = Post.query.filter_by(id=id_2).first().paragraph_1[0:50] + "..."
    title_link_2 = Post.query.filter_by(id=id_2).first().title_link

    id_3 = id_2 - 1
    title_3 = Post.query.filter_by(id=id_3).first().title
    cut_3 = Post.query.filter_by(id=id_3).first().paragraph_1[0:50] + "..."
    title_link_3 = Post.query.filter_by(id=id_3).first().title_link
    css = url_for('static', filename='button.css')
    db.session.commit()
    db.session.close()
    return render_template('index.html',  title_1=title_1, cut_1=cut_1, title_link_1=title_link_1, 
    title_2=title_2, cut_2=cut_2, title_link_2=title_link_2,
    tile_3=title_3, cut_3=cut_3, title_link_3=title_link_3, css=css, date=date)


@app.route('/dev_menu')
@login_required
def home():    
    return render_template("dev_menu.html")

@app.route('/about.html')
def about():  
    date = str(datetime.now(poland))[:-22]   
    my_photo = url_for('static', filename='about_photo.jpg')
    my_photo_back = url_for('static', filename='about_ZM_background.jpg')
    css = url_for('static', filename='button.css')
    return render_template('about.html', my_photo=my_photo, my_photo_back=my_photo_back, css=css, date=date)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

@app.route('/add_post', methods=['GET','POST'])
@login_required
def adding_post():    
    """
       # This function allows to add new posts. Posts that exists in db
       # cant be added for the second time. Everything is secured with a password
    """    
    if request.method == 'GET':
        return render_template('add_post.html')
    if request.method == 'POST':        
        title = request.form['title']
        text= request.form['text']        
        if title == '' or text == '':
            return "You didn't fill all the obligatory fields (title, text)."
        if Post.query.filter_by(title=title).first() is not None:
            return "Post probably is already in the database."
        language = request.form['language']
        par1 = re.compile(r'(p1)(.*)(/p1)')
        par2 = re.compile(r'(p2)(.*)(/p2)')
        par3 = re.compile(r'(p3)(.*)(/p3)')
        par4 = re.compile(r'(p4)(.*)(/p4)')
        par5 = re.compile(r'(p5)(.*)(/p5)')
        par6 = re.compile(r'(p6)(.*)(/p6)')
        l = [par1, par2, par3, par4, par5, par6]
        paragraphs = [None, None, None, None, None, None]
        for i in range(0,6):
            x = l[i].search(text)
            if x is None:
                break
            paragraphs[i] = x.group(2)
            if type(paragraphs[i]) != str:
                break
        lowercase = re.compile(r' ')
        title_link = lowercase.sub('_', title).lower()        
        date = str(datetime.now(poland))[:-13]       
        db.session.add(Post(title, paragraphs[0], paragraphs[1], 
    paragraphs[2], paragraphs[3], paragraphs[4], paragraphs[5], date, language, title_link))
        db.session.commit()
        db.session.close()
        msg = "Added succesfully"                      
        return f"'{title}' post was added... {msg}"
    return "No authorization to perform this action."

@app.route('/add_review', methods=['GET','POST'])
@login_required
def adding_review():    
    """
       # This function allows to add new reviews. Review that exists in db
       # cant be added for the second time. Everything is secured with a password
"""    
    if request.method == 'GET':
        return render_template('add_review.html')
    if request.method == 'POST':        
        artist = request.form['artist']
        album = request.form['album']
        cover = request.form['cover']
        header = request.form['header']
        review_v = request.form['review']
        listen = request.form['listen']
        rate = request.form['rate']
        if artist == '' or album == '' or header == '':
            return "You didn't fill all the obligatory fields (artist, album, header)."
        if Review.query.filter_by(artist=artist).first() is not None and Review.query.filter_by(album=album).first() is not None:
            return "Review probably is already in the database."
        language = request.form['language']
        par1 = re.compile(r'(p1)(.*)(/p1)')
        par2 = re.compile(r'(p2)(.*)(/p2)')
        par3 = re.compile(r'(p3)(.*)(/p3)')
        par4 = re.compile(r'(p4)(.*)(/p4)')
        par5 = re.compile(r'(p5)(.*)(/p5)')
        par6 = re.compile(r'(p6)(.*)(/p6)')
        l = [par1, par2, par3, par4, par5, par6]
        paragraphs = [None, None, None, None, None, None]
        for i in range(0,6):
            x = l[i].search(review_v)
            if x is None:
                break
            paragraphs[i] = x.group(2)
            if type(paragraphs[i]) != str:
                break
        lowercase = re.compile(r' ')
        artist_link = lowercase.sub('_', artist).lower()
        album_link =  lowercase.sub('_', album).lower()
        
        date = str(datetime.now(poland))[:-13]       
        db.session.add(Review(artist, album, cover, header, paragraphs[0], paragraphs[1], 
    paragraphs[2], paragraphs[3], paragraphs[4], paragraphs[5], listen, date, 
    rate, 
    language, 
    artist_link, 
    album_link))
        db.session.commit()
        db.session.close()
        msg = "Added succesfully"                      
        return f"{album} review was added... {msg}"
    return "No authorization to perform this action."

@app.route('/music_menu')
def music_menu():
    
    """
        This function creates a dynamic menu for music reviews.
        at /music?page=1 there are the newest ones (maximum 9 per page).
           1) Firstly the function checkes if requested page isnt too big.
           2) Secondly, it creates a list 'l' of lists of dictionaries returned from 'review_base.json'
           The index 0 of a list is always the review which was added lastly.
           3) Function creates a list 'a' of maximum 9 elements which will be
           presented on a requested page
           4) Important infos like 'artist', 'album' or links to reviews are being stored 
           in dictionaries and the passed to 'music_menu.html' 
    """    
    date = str(datetime.now(poland))[:-22]
    page = int(request.args.get('page', 1))
    reviews = db.session.query(Review).all()[::-1]
    x = int(len(reviews)/9) + 1
    buttons = []
    for i in range(0,x):
        buttons.append(i+1)
    reviews = reviews[(page - 1)*9: 9*page]     
    return render_template('music_menu.html', reviews=reviews, buttons=buttons, date=date)
    

@app.route('/music/')
def music_review():
  
    """
       # Function gets arguments like 'artist', 'review' etc from the music menu
       # and then it passes it to the template 'music_review.html' where the review
       # is shown.
    """
    db.session.close()
    db.session.commit()
    artist = request.args.get('artist',None)
    album = request.args.get('album', None)
    kwargs = {'artist_link': artist, 'album_link': album}
    result = db.session.query(Review).filter_by(**kwargs)
    artist = result[0].artist
    album = result[0].album
    cover = result[0].cover
    header = result[0].header        
    paragraph_1 = result[0].paragraph_1
    paragraph_2 = result[0].paragraph_2
    paragraph_3 = result[0].paragraph_3            
    paragraph_4 = result[0].paragraph_4
    paragraph_5 = result[0].paragraph_5
    paragraph_6 = result[0].paragraph_6
    rate = result[0].rate
    listen = result[0].listen
    date = result[0].date
    db.session.commit()
    db.session.close()
    css = url_for('static', filename='button.css')
    if type(paragraph_1) == str:
        return render_template('music_review.html', artist=artist, album=album,
        paragraph_1=paragraph_1, paragraph_2=paragraph_2, paragraph_3=paragraph_3,
        paragraph_4=paragraph_4, paragraph_5=paragraph_5, paragraph_6=paragraph_6,
        cover=cover, header=header, listen=listen, date=date, rate=rate, css=css)
    else:
        return f"Upsss, something went wrong. Sorry. :("

@app.route('/post/')
def post():
    """
        Function return post. The title is taken from the URL.
        The title and paragraphs are then passed to template.
    """
    css = url_for('static', filename='button.css')
    title_link = request.args.get('title',None)
    kwargs = {'title_link': title_link}
    result = db.session.query(Post).filter_by(**kwargs)
    title = result[0].title
    paragraph_1 = result[0].paragraph_1
    paragraph_2 = result[0].paragraph_2
    paragraph_3 = result[0].paragraph_3            
    paragraph_4 = result[0].paragraph_4
    paragraph_5 = result[0].paragraph_5
    paragraph_6 = result[0].paragraph_6
    date = result[0].date
    db.session.commit()
    db.session.close()
    if type(paragraph_1) == str:
        return render_template('post.html', title=title,
        paragraph_1=paragraph_1, paragraph_2=paragraph_2, paragraph_3=paragraph_3,
        paragraph_4=paragraph_4, paragraph_5=paragraph_5, paragraph_6=paragraph_6,
        date=date, css=css)
    else:
        return "Ups, something went wrong :("

@app.route('/all_posts')
def all_posts():
    date = str(datetime.now(poland))[:-22]
    posts = db.session.query(Post).all()[::-1]
    return render_template('all_posts.html', posts=posts, date=date)

if __name__ == '__main__':
    app.run()