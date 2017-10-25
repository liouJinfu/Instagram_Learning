#-*- encoding:UTF-8 -*-
from flask import Flask, render_template, request, make_response, redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.jinja_env.line_comment_prefix = "#"
app.secret_key = 'nowcoder'


@app.route("/")
def index():
    res = ''
    for msg, categorys in get_flashed_messages( with_categories=True):
        res += msg + categorys + '<br>'
    res += 'hello'
    return  res

@app.route('/profile/<int:uid>/', methods= ['POST','GET','OPTIONS'])
def profile(uid):
    colors = ('red', 'blue', 'green', 'black')
    dict = {'newcoder':'abc', 'goole':'def'}
    return render_template('profile.html', uid = uid, colors = colors, dict = dict)

@app.route('/request/')
def request_demo():
    key = request.args.get('key', 'defaultkey') + '<br>'
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url + '+' + request.path + '<br>'
    for property in dir(request):
        res = res + str(property) + "|==|\n"+ str(eval('request.'+property)) +  '<br>'
    response = make_response(res)
    response.set_cookie("newcoderreso", key)
    response.status = '404'
    response.headers['name'] = 'hello~~~~'
    return response

@app.route("/newpath/")
def newpath():
    return "'newpath"

@app.route("/redirect/<int:code>")
def redirect_demo(code):
    return redirect('/newpath', code = code)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error404.html", error = error)

# @app.errorhandler(400)
# def exception_page(error):
#     return 'exception'

@app.route("/admin")
def loging_page():
    key  = request.args.get("key")
    if key == 'admin':
        return "hello admin"
    else:
        return render_template("error404.html", error = 400)

@app.route('/login')
def login():
    app.logger.info('log success!')
    flash("登录成功", 'INFO')
    return redirect("/")

@app.route("/log/<level>/<msg>/")
def log(level, msg):
    dict = {'warn': logging.WARNING, 'error':logging.ERROR, 'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)
    return 'logged:' + msg

# @app.logger.log()
def set_logger():
    info_file_handler = RotatingFileHandler('D:\\Instagram_Learning\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('D:\\Instagram_Learning\\warning.txt')
    warn_file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(warn_file_handler)

    error_file_hander = RotatingFileHandler('D:\\Instagram_Learning\\error.txt')
    error_file_hander.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_hander)
if __name__ == '__main__':
    set_logger()
    app.run(debug= 'True')