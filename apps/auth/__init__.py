#apps/auth/__init__.py
from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates')
#main = Blueprint('main', __name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

from . import views  # views.py import해서 라우팅 등록
from . import forms  # forms.py import해서 폼 클래스 등록
