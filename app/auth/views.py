from flask import render_template, redirect, request, url_for, flash
from flask_login import  login_user, logout_user, login_required

from . import auth
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_or_email = form.name_or_email.data
        user = None
        if '@' in user_or_email:
            user = User.query.filter(User.email==user_or_email).first()
        else:
            user = User.query.filter(User.username==user_or_email).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名、邮箱或密码不正确')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已登出')
    return  redirect(url_for('main.index'))