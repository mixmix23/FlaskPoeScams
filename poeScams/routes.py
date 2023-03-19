from poeScams import app
from flask import render_template
from poeScams.models import Item
from poeScams.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/gem-deals')
def gem_deals():
    items = Item.query.all()
    return render_template('gem-deals.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)