from flask import Flask

__author__ = 'Angel'

def create_app():
    app = Flask(__name__)
    # 载入配置
    app.config.from_object('config')
    # 注册蓝图
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)