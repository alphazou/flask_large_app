#!/home/xiaozi/anaconda3/bin/python

import os
from app import create_app, db, mail
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, mail=mail, User=User, Role=Role)

manager.add_command('shell', Shell(make_context=make_shell_context))

# 命令行输入: ./manage.py db init 创建迁移资源库
# ./manage.py db migrate -m "注释内容"创建自动迁移脚本
# ./manage.py db upgrade 更新数据库
manager.add_command('db', MigrateCommand)

# 被装饰的函数名可以被当做命令名使用
# 在命令行输入：python manage.py test 可启动单元测试
@manager.command
def test():

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()


'''
flask-script 命令行的常用用法：
1、启动服务: ./manage.py runserver [option]
2、进入调试模式： ./manage.py shell
3、调试模式下命令：
    db.create_all()  创建数据库表
    db.drop_all()    清空数据库表
    
    # 添加字段
    admin_role = Role(name='admin')
    user_role = Role(name='user')
    db.session.add_all([admin_role, user_role])

    user_xiaozi = User(username='xiaozi', nickname='娜西小子', email='nx_xiaozi@163.com',password='b091880', role=admin_role)
    db.session.add(user_xiaozi)

    for i in range(1,10):
        db.session.add(User(username='user{}'.format(i), role=user_role))

    db.session.commit()

    #查询
    user8 = User.query.filter_by(username='user8').first()
    role_user = Role.query.filter_by(name='user').first()
    print(role_user.users.order_by(User.username).all())
    print(user8.role)
    print(role_user.users.count())


    #删除
    user8 = User.query.filter_by(username='user8').first()
    db.session.delete(user9)
    db.session.commit()


'''
