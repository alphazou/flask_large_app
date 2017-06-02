from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from ..models import User


class LoginForm(FlaskForm):
    name_or_email = StringField(label='用户名或邮箱',
                                validators=[DataRequired(message='不能为空'),
                                            Length(1,64)])
    password = PasswordField(label='密码', validators=[DataRequired()])
    remember_me = BooleanField('记住登录')
    submit = SubmitField('登   录')


class RegistrationForm(FlaskForm):

    username = StringField(label='用户名',
                           validators=[
                               DataRequired(),
                               Length(1, 64),
                               Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
                                      '用户名必须为字母、数字和下划线组成')
                           ])
    nickname = StringField(label='昵称',
                           validators=[
                               DataRequired(),
                               Length(1, 64)
                           ])
    email = StringField(label='邮箱',
                        validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(label='密码',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='两次输入密码必须一样')
                             ])
    password2 = PasswordField(label='确认密码',
                              validators=[DataRequired()])
    submit = SubmitField('注    册')

    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('该邮箱已经被注册')

    def validate_username(self, filed):
        if User.query.filter_by(username=filed.data).first():
            raise ValidationError('该用户名已经被注册')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(label='原密码',
                                 validators=[DataRequired()])
    password = PasswordField(label='新密码',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='两次输入密码必须一样')
                             ])
    password2 = PasswordField(label='确认新密码',
                              validators=[DataRequired])
    submit = SubmitField('重设密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField(label='邮箱',
                        validators=[DataRequired(),Length(1,64), Email()])
    submit = StringField('重设密码')


class PasswordResetForm(FlaskForm):
    email = StringField(label='邮箱',
                        validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField(label='新密码',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='两次输入密码必须一样'),
                             ])
    password2 = PasswordField(label='确认新密码', validators=[DataRequired()])
    submit = SubmitField('重设密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱不存在')


class ChangeEmailForm(FlaskForm):
    email = StringField(label='新邮箱',
                        validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(label='密码', validators=[DataRequired()])
    submit = SubmitField('重设邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已注册。')



