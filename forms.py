from flask_wtf import FlaskForm
from wtforms import StringField

class InputForm(FlaskForm):
	bill = StringField("Bill")
	percentage = StringField('Percent')

class DiscountForm(FlaskForm)
	tagPrice =StringField('Tagged Price')
	discount =StringField('% Discount')
