from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField

class InputForm(FlaskForm):
	bill = IntegerField("Bill")
	percentage = IntegerField('Percent')

class DiscountForm(FlaskForm)
	tagPrice =FloatField('Tagged Price')
	discount =FloatField('% Discount')
