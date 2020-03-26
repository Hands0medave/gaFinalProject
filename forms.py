from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class InputForm(FlaskForm):
    bill = IntegerField("Enter your bill")
    percentage = IntegerField('What percentage do you want to tip?')
    submit = SubmitField('Submit!')

class DiscountForm(FlaskForm):
    tagPrice =IntegerField('What is the price of the item?')
    discount =IntegerField('What is the percent discount?')
    submit = SubmitField('Submit!')
