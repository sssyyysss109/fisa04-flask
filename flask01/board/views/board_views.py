from flask import Blueprint, render_template
from ..models import Question

# 특정 /url/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로
cbp = Blueprint('collection', __name__,url_prefix='/board')

@cbp.route('/boardlist')
def list():
    return render_template('board_list.html',question)

@cbp.route('/no1')
def hello2():
    return f'{__name__} 첫번째째'

@cbp.route('/no2')
def hello3():
    return f'{__name__} 두번째째'

