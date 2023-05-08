from app import app
from flask import render_template
from models import Product



@app.route("/")
def home():
    items = Product.query.all()
    return render_template('index.html', items = items)


@app.route("/product/<int:id>/")
def productDetail(id):
    item = Product.query.filter_by(id = id).first()
    return render_template('product.html', item = item)