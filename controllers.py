from app import app
from flask import render_template, request
from models import Product, Contact, ProductReview
from forms import ContactForm, ReviewForm



@app.route("/")
def home():
    items = Product.query.all()
    return render_template('index.html', items = items)


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