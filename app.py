from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/test2')
def hello2():
    return "2222222222222"

# 파이썬 코드가 직접 실행인지 아니면 다른 모듈에 의해서
# 임포트 되었는지를 판단하는데 사용
if __name__ == '__main__': # 직접 실행 조건
    app.run(debug=True)