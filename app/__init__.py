from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
# session_protection属性可以设置None, basic, strong,
# 设置为strong的时候Flask-Login 会监控用户的IP地址变动并提示用户重新登陆。
login_manager.session_protection = 'strong'
# login_view属性设置了login页面的断点
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    # 导入蓝图并注册
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # url_prefix参数是可选的，当设置了url_prefix以后，
    # 所有auth blueprint的路由都会默认加上前缀
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app