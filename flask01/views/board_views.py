from flask import Blueprint

# 특정 /url/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로
mbp1 = Blueprint('no1', __name__,url_prefix='/collection/no1')
mbp2 = Blueprint('no2', __name__,url_prefix='/collection/no2')


@mbp1.route('/')
def hello2():
    return f'{__name__} 첫번째째'

@mbp2.route('/')
def hello3():
    return f'{__name__} 두번째째'