from flask import Flask

def create_app():

    # 입구 파일을 하나 만들어줌
    app = Flask(__name__)

    from views import main_views
    app.register_blueprint(main_views.mbp)
    
    from views import board_views
    app.register_blueprint(board_views.mbp1)
    app.register_blueprint(board_views.mbp2)

    @app.route('/collection')
    def hello2():
        return f'두번째째'

    @app.route('/collection/test')
    def hello3():
        return f'두번째째'
    
    return app

# flask run --debug --port 5001