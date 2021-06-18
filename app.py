from flask import Flask,redirect,url_for,render_template,request
from test import cat_generator


app=Flask(__name__)

@app.route('/index')
def index(name='Index'):
    return render_template('index.html', name=name, cat_generator=cat_generator())

if __name__ == '__main__':
    app.run(port=5000,debug=True)