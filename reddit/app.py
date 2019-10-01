from flask import Flask

app = Flask(__name__)

@app.route('/reddit/')
def api_root():
    return 'Hello World!'

@app.route('/reddit/<username>')
def api_user(username):
    pass

if __name__ == "__maine__":
    app.run()
