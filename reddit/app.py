from flask import Flask
from reddit.user import User

app = Flask(__name__)

@app.route('/reddit/')
def api_root():
    return 'Hello World!'

@app.route('/reddit/<username>')
def api_user(username):
    user = User(username)
    return 'Reddit user ' + username + ' was created on: ' + user.getCreationDate()

if __name__ == "__maine__":
    app.run()
