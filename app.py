from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/regionales')
def regionales():
    return render_template('sitio/regionales.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

if __name__ == '__main__':
    app.run(debug=True)

    