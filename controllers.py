from app import app
from flask import render_template, request
from models import Product, Contact, ProductReview, User, Category
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from forms import (
    ContactForm, 
    ReviewForm, 
    RegisterForm,
    LoginForm
    )



@app.route("/")
def home():
    categories = Category.query.all()
    items = Product.query.all()
    return render_template('index.html', items = items, categories = categories)


@app.route("/category/<string:title>/")
def cat(title):
    categories = Category.query.all()
    items = Category.query.filter_by(title = title).first().products
    return render_template('index.html', items = items, categories = categories)


@app.route("/login/", methods = ['GET', 'POST'])
def log():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            print('login')
            return render_template('index.html')
    return render_template('login.html', form = form)


@app.route("/register/", methods = ['GET', 'POST'])
def reg():
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate_on_submit():
            user = User(
                username = form.username.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data)
            )
            user.save()
    return render_template('register.html', form = form)


@app.route("/product/<int:id>/", methods = ['GET', 'POST'])
def productDetail(id):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.form)
        print(request.form)
        if form.validate_on_submit():
            review = ProductReview(
                message = form.message.data,
                name = form.name.data,
                email = form.email.data,
                product_id = id
            )
            review.save()
    item = Product.query.filter_by(id = id).first()
    return render_template('product.html', item = item, form = form)


@app.route("/contact/", methods = ['GET', 'POST'])
def contact_us():
    form = ContactForm()
    print(request.form)
    if request.method == 'POST':
        print('post')
        form = ContactForm(request.form)
        if form.validate_on_submit():
            print('valid')
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                company = form.company.data,
                message = form.message.data,
                is_subscribe = form.is_subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)