from flask import Flask

# 입구 파일을 하나 만들어줌
app = Flask(__name__)

@app.route('/hello2')
def hello2():
    return f'{__name__} hello'

if __name__ == '__main__':
    app.run(debug=True, port=5001)