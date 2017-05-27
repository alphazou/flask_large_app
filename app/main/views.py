from datetime import datetime
from flask import render_template, session, redirect,url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required

from . import main
from .forms import LoginForm, RegisterForm
from ..models import User
from app import db


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():

    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           user=session.get('user'),)

