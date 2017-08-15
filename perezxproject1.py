from flask import Flask, render_template,  request, logging
from data import Product

app = Flask(__name__)

 

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/products')
def products():
    return render_template('products.html', product = Product)

@app.route('/profile')
def Profile():
    return render_template('profile.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
