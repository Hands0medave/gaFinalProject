##My Website will feature a home page, about me, and 3 web applications

import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from forms import InputForm, DiscountForm

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SECRET_KEY'] = 'spinal tap'

# The default URL ends in / ("my-website.com/").
@app.route('/')

# Function that returns the home page
def home():
    return render_template('home.html')

@app.route('/about')
#Function that returns the about me page
def about():
    return render_template('about.html')


#helper functions
def calculateTip (bill, percent):
	totalBill = bill*(1+percent)
	return(totalBill)

#function that ruturns the tip calculator app
@app.route('/tip_calculator', methods=["GET", "POST"])	
def tipCalculator():
    
    form = InputForm()
    pagedata = {}
    if request.method == "POST":
        """Get user input from form """
        userBill = int(request.form["bill"])
        userPercentage = int(request.form["percentage"])
        
        """ Calculate total bill """
        tipPercentage = userPercentage / 100
        totalBill = calculateTip(userBill, tipPercentage)
        
        pagedata = {
            "totalBill": totalBill
        }
    
    return render_template('tipCalculator.html',form=form, pagedata=pagedata)
    
#function that returns the guess the number game
@app.route('/discount_calculator', methods=["GET", "POST"])
def discountCalculator():
    
    form = DiscountForm()
    pagedata = {}
    
    if request.method == "POST":
        itemPrice = int(request.form["tagPrice"])
        percentDiscount = int(request.form["discount"])
    
        """ Calculate discounted price """
        reducedPrice = itemPrice - (itemPrice * percentDiscount / 100)
        
        pagedata = {
            "reducedPrice": reducedPrice
        }
        
    return render_template('discountCalculator.html', form=form, pagedata=pagedata)
    
    
#weather app
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/weatherApp', methods=['GET', 'POST'])
def weatherApp():
    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            new_city_obj = City(name=new_city)
            
            db.session.add(new_city_obj)
            db.session.commit()
            
    cities = City.query.all()
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    
    weather_data = []
    
    for city in cities:
        
        r = requests.get(url.format(city.name)).json()
        
        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)


# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)