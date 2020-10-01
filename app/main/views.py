from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_image

@main.route('/')
def index():

    title = 'PHOTO APP'

    images = get_image("photo")



    return render_template("index.html",title = title,images = images)
