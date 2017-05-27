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


class RegisterForm(FlaskForm):
    user_name = StringField(u'用户名',
                        validators=[DataRequired(
                            message=u'账号不能为空'),
                            Length(1,24)])
    nick_name = StringField(u'昵称',
                            validators=[DataRequired(
                                message=u'昵称不能为空')])
    email = StringField(u'邮箱',
                        validators=[DataRequired(
                            message=u'邮箱不能为空'),
                            Length(1,64),
                            Email(message='邮箱格式不正确')])
    password = PasswordField (u'密码',
                           validators=[DataRequired(
                               message=u'密码不能为空'),
                               Length(1, 24)])
    confirm_password = PasswordField(u'确认密码',
                               validators=[DataRequired(
                               message=u'不能为空'),
                               Length(1, 24)])
    submit = SubmitField('注  册')



