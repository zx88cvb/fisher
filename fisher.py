from flask import Flask, make_response

from helper import is_isbn_or_key

__author__ = 'Angel'

app = Flask(__name__)

# 载入配置
app.config.from_object('config')

# 路由 相当于Controller
@app.route('/hello/')
def hello():
    headers = {
        'content-type': 'text/plain', # 设置请求头
        # 'location': 'http://www.baidu.com' # 重定向
    }
    # response = make_response('<html></html>', 404)
    # response.headers = headers
    return '<html></html>', 200, headers


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 isbn
    :param page: 
    :return: 
    """

    isbn_or_key = is_isbn_or_key(q)
    pass

# view_func 视图函数
# 基于类的视图 需要
# app.add_url_rule('/hello/', view_func=hello)


# 入口文件才能调用
if __name__ == '__main__':
    # 生产环境 nigix+uwsgi

    # host 让局域网和外网访问
    app.run(host='0.0.0.0', port=8082, debug=app.config['DEBUG'])