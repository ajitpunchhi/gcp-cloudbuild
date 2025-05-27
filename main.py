from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from App Engine! This is a Version 2 of the app.'

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)