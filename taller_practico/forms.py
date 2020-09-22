from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError


#crear función para validación custom o personalizada
def queNoSeaHola(form, field):
    if field.data=="hola":
        raise ValidationError('El campo nombre no puede tener el valor hola!!!')



class Persona(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(message="El campo es obligatorio."),
        Length(max=10, min=3, message="El campo debe tener entre 3 y 10 caracteres."),
        queNoSeaHola
    ])
    correo = StringField("E-Mail", validators=[
        DataRequired(),
        Email()
    ])
    telefono = StringField("Teléfono", validators=[
        DataRequired(),
        Length(max=10, min=3)
    ])
    submit = SubmitField('Enviar')