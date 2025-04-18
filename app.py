from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
session(app)

# Home route


@app.route("/")
def index():
    return render_template('index.html')


# Clear session route
@app.route('/clear_session', methods=['GET'])
def clear_session():
    # Clear the session
    session.clear()
    return jsonify({'status': 'session cleared'})

if __name__ == 'main':
     app.run(host='192.168.1.160', port=8080, debug=True)