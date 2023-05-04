from flask import Flask, render_template

app = Flask(__name__,)

items = {
    1: {
        'id' : 1,
        'title': 'Product #1',
        'description': 'Some Description #1',
        'image': 'shoes1.jpeg',
        'price': 100,
        'quantity': 10,
        'colors' : ['red', 'blue'],
        'sizes' : ['S', 'M']
    },
    2: {
        'id' : 2,
        'title': 'Product #2',
        'description': 'Some Description #2',
        'image': 'shoes2.jpeg',
        'price': 200,
        'quantity': 20,
        'colors' : ['yellow', 'blue'],
        'sizes' : ['XS', 'M']
    },
    3: {
        'id' : 3,
        'title': 'Product #3',
        'description': 'Some Description #3',
        'image': 'shoes3.jpeg',
        'price': 300,
        'quantity': 30,
        'colors' : ['green', 'blue'],
        'sizes' : ['XL', 'M']
    }
}


@app.route("/")
def home():
    return render_template('index.html', items = items)


@app.route("/product/<int:id>/")
def productDetail(id):
    return render_template('product.html', item = items[id])