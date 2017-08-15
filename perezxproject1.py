from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def Login():
    return render_template('Login.html')

@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/products')
def Products():
    return render_template('products.html')

@app.route('/profile')
def Profile():
    return render_template('profile.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def Contact():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
