from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = StringField('Капитан команды', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = StringField('Время работы', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    start_date = DateField('Начало работы', validators=[DataRequired()])
    end_date = DateField('Конец работы')
    is_finished = BooleanField('Закончена ли работа?')
    submit = SubmitField('Применить')