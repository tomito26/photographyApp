from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import User,Role, Comments
from . import main
from flask import render_template
from .forms import CommentForm
from .. import db


# COMMENT METHOD
@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)

@main.route('/new_comment/<int:users_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(users_id):
    users =users.query.filter_by(id = users_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment,user_id=current_user.id, users_id=users_id)
        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New Comment'
    return render_template('new_comment.html',title=title,comment_form = form,users_id=users_id)
