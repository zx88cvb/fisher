from flask import Blueprint

# 蓝图 blueprint
web = Blueprint('web', __name__)

# 导入需要放下面 否则会报错 cannot import name 'web'
from app.web import book
from app.web import user