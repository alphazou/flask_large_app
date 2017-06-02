from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from . import login_manager
# from manage import app
from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    nickname = db.Column(db.String(48))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),default=2)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('密码不是可读的属性')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    confirmed = db.Column(db.Boolean, default=False)

    def generate_confirmation_token(self, expiration=3600):
        # expiration=3600表示默认失效时间3600秒
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return  s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))








# # 删除和创建表
# db.drop_all()
# db.create_all()
#
# # 添加字段
# admin_role = Role(name='admin')
# user_role = Role(name='user')
# db.session.add_all([admin_role, user_role])
#
# user_xiaozi = User(username='xiaozi', nickname='娜西小子', email='nx_xiaozi@163.com',password='b091880', role=admin_role)
# db.session.add(user_xiaozi)
#
# for i in range(1,10):
#     db.session.add(User(username='user{}'.format(i), role=user_role))
#
# db.session.commit()

#查询
# user8 = User.query.filter_by(username='user8').first()
# role_user = Role.query.filter_by(name='user').first()
# print(role_user.users.order_by(User.username).all())
# print(user8.role)
# print(role_user.users.count())


#删除
# user8 = User.query.filter_by(username='user8').first()
# db.session.delete(user9)
# db.session.commit()