#-*- encoding:UTF-8 -*-

from flask_script import Manager
from c2 import app

manager = Manager(app)

@manager.command
def hello(name):
    print 'hello', name

@manager.option('-n', '--name', dest = 'name', default = 'nowcoder')
def option(name):
    print 'option', name
@manager.command
def initialize_database():
    'initialize_database'
    print 'database ...'
if __name__ == '__main__':
    manager.run()