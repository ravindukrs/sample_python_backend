from flask import Flask, jsonify, request
from helper_module import get_greeting
import json

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    greeting = get_greeting(name)
    return jsonify({'greeting': greeting})

@app.route('/', methods=['GET'])
def default():
    name = request.args.get('name', 'World')
    greeting = get_greeting(name)
    return jsonify({'greeting': greeting})

@app.route('/healthz')
def healthz():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/health')
def health():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/test1')
def test_1():
    return jsonify({'test': 'test1'})

@app.route('/test2')
def test_2():
    return jsonify({'test': 'test2'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
