from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import make_response, jsonify

__author__ = 'Angel'

# 蓝图 blueprint

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
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200 , {'content-type': 'application/json'}

# view_func 视图函数
# 基于类的视图 需要
# app.add_url_rule('/hello/', view_func=hello)