from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/users')
def get_users():
    user = { "id": "123", "name": "uros" }
    response = make_response(
        user,
        200,
    )
    response.headers['Content-Type'] = "application/json"
    
    return response