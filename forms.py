from wtforms import Form, SelectField, RadioField
from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField,RadioField, IntegerField
from wtforms import EmailField
from wtforms import validators

class DictionaryForm(Form):
    word_english = StringField('Ingles:', validators=[validators.InputRequired()])
    word_spanish = StringField('Español:', validators=[validators.InputRequired()])

class ResistanceForm(Form):
    colores = [
        (0, 'Negro'),
        (1, 'Cafe'),
        (2, 'Rojo'),
        (3, 'Naranja'),
        (4, 'Amarillo'),
        (5, 'Verde'), 
        (6, 'Azul'),
        (7, 'Violeta'),
        (8, 'Gris'),
        (9, 'Blanco'),
    ]
    tolerancias = [
        (5, 'Oro'), 
        (10, 'Plata')
    ]

    color1 = SelectField('Color 1', choices=colores)
    color2 = SelectField('Color 2', choices=colores)
    color3 = SelectField('Color 3', choices=colores)
    tolerancia = RadioField('Tolerancia', choices=tolerancias)
    
class DictionaryForm(Form):
    word_english = StringField('Ingles:', validators=[validators.InputRequired()])
    word_spanish = StringField('Español:', validators=[validators.InputRequired()])

