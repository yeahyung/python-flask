from flask import Flask, url_for, request, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print("post")
        #print(request.form['username'])
        print(request.get_data())
    else:
        print(request)
    return "asd"

'''
request body:
{
	"data": {
		"username": "Dean",
		"age": 25
	},
	"valuelist": [{
		"value": 1
	}, {
		"value": 2
	}]
}
'''
@app.route('/test', methods=['POST', 'GET'])
def add():
    data = request.get_json()
    # memberNo header 없으면 그냥 None 으로 출력됨
    if request.headers.get("memberNo") is None:
        print("MemberNo is None")
    else:
        print(request.headers.get("memberNo"))
    print(data['data'])
    print(data['data']['username'])
    print(data["valuelist"])
    print(len(data["valuelist"]))
    for data in data["valuelist"]:
        print(data)
        print(data["value"])
    return "asdf"


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('hello'))


if __name__ == '__main__':
    app.run()
