import string
from flask import Flask, render_template, request
from common import *

app = Flask(__name__)

common = Common()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

@app.route('/')
def index(name=None):
    context = ''
    res = ''
    return render_template('index.html', context=context, res=res)

@app.route('/config', methods=['POST', 'GET'])
def config():
    context = common.cookie_string
    return render_template('config.html', context=context)

@app.route('/save', methods=['POST', 'GET'])
def save():
    context = request.form['context']
    print('config=' + context)
    common.save_config(context)
    return render_template('config.html', context=context)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # if request.method == 'POST':
    res = []
    context = request.form['context']
    context = context.replace(" ", "")
    if context == "":
        str = ''
        return render_template('index.html', context=context, res=str)

    contexts = context.split('\r\n')
    if len(contexts) == 0:
        str = ''
        return render_template('index.html', context=context, res=str)

    for c in contexts:
        if c == None or c == '':
            continue

        array = c.split('----')
        if len(array) == 0:
            continue

        result = []

        uid = array[0]
        if is_number(uid) == False:
            continue

        room_id, uname, is_signed = common.GetSigned(array[0])
        if room_id != "" and uname != "":
            result.append(uid)
            result.append(repr(room_id))
            result.append(uname)
            if is_signed == True :
                result.append('已签约')
            else:
                result.append('未签约')
            res.append('----'.join(result))
        else:
            print('返回数据错误')
    str = '\r\n'.join(res)
    return render_template('index.html', context=context, res=str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
