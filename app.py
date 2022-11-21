from flask import Flask
from flask import render_template, request, redirect

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

@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/regionales')
def admin_regionales():
    return render_template("admin/regionales.html")

@app.route('/admin/regionales/guardar', methods=['POST'])
def admin_regionales_guardar():
    print(request.form['txtNombre'])
    return redirect("/admin/regionales")

if __name__ == '__main__':
    app.run(debug=True)

    