from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, data_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '532fc25723ac39cdf095fc0468d6dd16'

class SimpleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Send')

@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        name = form.name.data
        return f'Hello, {name} Your form was send!'
    return render_template('form.html', form=form)

if __name__ =='__main__':
    app.run(debug=True)
