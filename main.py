import string
from flask import Flask, render_template, request
from common import *

app = Flask(__name__)

common = Common()

@app.route('/')
def index(name=None):
    context = ''
    res = ''
    return render_template('index.html', context=context, res=res)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        res = []
        context = request.form['context']
        contexts = context.split('\r\n')
        for c in contexts:
            array = c.split('----')
            result = []

            uid = array[0]
            room_id, uname, is_signed = common.GetSigned(array[0])
            result.append(uid)
            result.append(repr(room_id))
            result.append(uname)

            if is_signed == True :
                result.append('已签约')
            else:
                result.append('未签约')

            res.append('----'.join(result))
        str = '\r\n'.join(res)
        return render_template('index.html', context=context, res=str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
