from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import jsonify, request
from . import web

__author__ = 'Angel'

# 路由 相当于Controller
@web.route('/hello/')
def hello():
    headers = {
        'content-type': 'text/plain', # 设置请求头
        # 'location': 'http://www.baidu.com' # 重定向
    }
    # response = make_response('<html></html>', 404)
    # response.headers = headers
    return '<html></html>', 200, headers


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 isbn
    :param page: 
    :return: 
    """
    q = request.args['q']
    page = request.args['page']

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200 , {'content-type': 'application/json'}

# view_func 视图函数
# 基于类的视图 需要
# app.add_url_rule('/hello/', view_func=hello)