from flask import Flask, make_response, jsonify

from app import create_app

__author__ = 'Angel'

app = create_app()

# 入口文件才能调用
if __name__ == '__main__':
    # 生产环境 nigix+uwsgi

    # host 让局域网和外网访问
    app.run(host='0.0.0.0', port=8082, debug=app.config['DEBUG'])