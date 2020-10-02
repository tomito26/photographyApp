from .. import db,photos
from flask import render_template,redirect,flash,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User
from ..email import mail_message
from ..models import User
from .forms import UpdateProfile
from ..requests import get_images,search_image
import cloudinary
import cloudinary.uploader
import cloudinary.api

@main.route('/')
def index():
    '''
    Function that returns index page and its contents
    '''
    people = get_images('people')
    nature = get_images('nature')
    urban = get_images('computers')
    title = 'Home - Welcome to PhotoWeb  where you can get all images under one platform '
    
    search_image = request.args.get('image_query')
    
    if search_image:
        return redirect(url_for('main.search',image_name=search_image))
    else:    
        return render_template('index.html', people=people,title=title,nature=nature,urban=urban)   
@main.route('/nature')
def nature():
    nature = get_images('nature')
    return render_template('nature.html',nature=nature)
@main.route('/search/<search_term>')
def search(search_term):
    '''
     view function to display the search results   
    '''
    
    search_term_list = search_term.split(" ")
    search_term_format = "+".join(search_term_list)
    searched_images = search_image(search_term_format)
    
    title = f'search reuslts for {{search_term}}'
    
    return render_template('search.html',images = searched_images)
    
    
    
@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        upload = cloudinary.uploader.upload(filename)
        path = upload.get('url')
        user.profile_pic_path = path
        db.session.commit()
        
    return redirect(url_for('main.profile', uname=uname))


@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)
