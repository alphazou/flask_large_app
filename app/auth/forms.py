from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    name_or_email = StringField(label='用户名或邮箱',
                                validators=[DataRequired(message='不能为空'),
                                            Length(1,64)])
    password = PasswordField(label='密码', validators=[DataRequired()])
    remember_me = BooleanField('记住登录')
    submit = SubmitField('登   录')