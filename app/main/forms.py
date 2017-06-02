from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email



class LoginForm(FlaskForm):

    name_or_email = StringField(u'用户名或邮箱',
                        validators=[DataRequired(
                            message=u'请输入用户名或邮箱'),
                            Length(1, 64)])
    password = PasswordField(u'密码',
                             validators=[DataRequired(
                                 message=u'密码不能为空'),])
    remember_me = BooleanField('记住', default=False)
    submit = SubmitField(u'登录')






