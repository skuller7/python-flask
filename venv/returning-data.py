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

@app.route('/article1')
def article1():
    return render_template(
        'article.html',
        title='My First Article',
        content="Thank you for reading! this is my first article"
    )

@app.route('/article2')
def article2():
    return render_template(
        'article.html',
        title='My Second Article',
        content="Thank you for reading! this is my second article"
    )

@app.route('/article3')
def article3():
    return render_template(
        'article.html',
        title='My Third Article',
        content="Thank you for reading! this is my third article"
    )
