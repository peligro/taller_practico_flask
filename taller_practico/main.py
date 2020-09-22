from flask import Flask, redirect, url_for, render_template, request
from forms import Persona
from flask_mysqldb import MySQL


app = Flask(__name__)


app.secret_key = "123456"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'peligro'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'pruebas_python'

mysql = MySQL(app)

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
    cursor = mysql.connection.cursor()
    cursor.execute("select * from servicios;")
    datos  = cursor.fetchall()
    return render_template('servicios.html', datos=datos)


@app.route('/servicios/detalle/<slug>')
def servicios_detalle(slug):
    cursor = mysql.connection.cursor()
    cursor.execute(f"select * from servicios where slug='{slug}';")
    datos = cursor.fetchone()
    if datos==None:#si la consulta a la BD llega vacía
        return render_template('404.html')
    return render_template('detalle.html', datos=datos)


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

@app.route('/formulario-simple', methods=["GET", "POST"])
def formulario_simple():
    if request.method =='POST':
        return f"nombre={ request.form['nombre'] } | E-Mail={ request.form['correo'] } | teléfono={ request.form['telefono'] }"
    return render_template("formulario-simple.html")


@app.route('/formulario-simple-objeto', methods=["GET", "POST"])
def formulario_simple_objeto():
    form = Persona()
    if form.validate_on_submit():
        return f"nombre={ request.form['nombre'] } | E-Mail={ request.form['correo'] } | teléfono={ request.form['telefono'] }"
    return render_template("formulario-simple-objeto.html", form=form)


if __name__=='__main__':
    app.run(debug=True)