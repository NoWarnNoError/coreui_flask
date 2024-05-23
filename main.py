from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/uploadFile1', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.name)
        print("file", f)

    return "<p>uploadFile1</p>"


@app.route('/uploadParam1', methods=['GET', 'POST'])
def upload_param1():
    if request.method == 'POST':
        sensitive_data = request.form.get('sensitive_data')
        t = request.form.get('t')
        algorithm = request.form.get('algorithm')
        c1 = request.form.get('c1')
        c2 = request.form.get('c2')
        w = request.form.get('w')
        pm = request.form.get('pm')
        pc = request.form.get('pc')
        F = request.form.get('F')
        CR = request.form.get('CR')

        print(sensitive_data)
        print(algorithm)

    return "<p>uploadParam1</p>"


@app.route('/uploadFile2', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f1 = request.files['file1']
        f1.save(f1.name)

        f2 = request.files['file2']
        f2.save(f2.name)

    return "<p>uploadFile2</p>"


@app.route('/uploadParam2', methods=['GET', 'POST'])
def upload_param2():
    if request.method == 'POST':
        k = request.form.get('k')

        print(k)

    return "<p>uploadParam2</p>"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3001)
