from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    texto = "Hola con las <strong>manos en el código</strong>"
    edad = 18
    return render_template('home.html', texto=texto, edad=edad)


@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


@app.route('/servicios/detalle/<slug>')
def servicios_detalle(slug):
    return f"Detalle del servicio <strong>{slug}</strong>"


@app.route('/servicios/detalle-dos/<int:id1>')
@app.route('/servicios/detalle-dos/<int:id1>/<id2>')
def servicios_detalle_dos(id1, id2=None):
    defecto = ''
    if id2==None:
        defecto=''
    else:
        defecto=id2
    return f"Los valores son <strong>{id1}</strong> | <strong>{defecto}</strong>"


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__=='__main__':
    app.run(debug=True)