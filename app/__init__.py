from flask import Flask

__author__ = 'Angel'

def create_app():
    app = Flask(__name__)
    # 载入配置
    app.config.from_object('config')
    return app