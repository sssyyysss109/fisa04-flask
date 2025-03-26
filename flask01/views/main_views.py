from flask import Blueprint

# 특정 /url/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로
mbp = Blueprint('main', __name__,url_prefix='/main')

# localhost:5001/main/
@mbp.route('/')
def hello2():
    return f'{__name__} hello'

#Flask에서 값을 주소줄로 입력받아 사용하는 방법
#<변수명> /변수명
@mbp.route('/<username>')
def print_string(username):
    return f'{__name__} {username} hello'

#Flask에서 값을 주소줄로 입력받아 사용하는 방법
#<자료형:변수명>
@mbp.route('/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath} hello'

#Flask에서 값을 주소줄로 입력받아 사용하는 방법
#<자료형:변수명>
@mbp.route('/상품명/')
@mbp.route('/items/')
@mbp.route('/items/<itemname>')
@mbp.route('/items/<itemname>/<float:quantity>')
def print_itemname(itemname='기본값값',quantity=0):
    return f'{__name__} {itemname, quantity} hello'