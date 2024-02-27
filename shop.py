from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/clothes/')
def clohes():
    context = {'title': 'Каталог одежды'}
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'title': 'Каталог обуви'}
    return render_template('shoes.html', **context)

@app.route('/clothes/jackets/')
def jackets():
    context = {'title': 'Ассортимент курток'}
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run()
