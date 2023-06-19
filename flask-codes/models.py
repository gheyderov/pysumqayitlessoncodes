from extensions import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(55), nullable = False)
    email = db.Column(db.String(200), nullable = True)
    password = db.Column(db.String(255), nullable = True)
    blogs = db.relationship('Blog', backref = 'user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()      


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255), nullable = True)
    image = db.Column(db.String(255))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    reviews = db.relationship('ProductReview', backref = 'product')

    def __init__(self, title, description, image, price, quantity, category_id):
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        self.quantity = quantity
        self.category_id = category_id

    def save(self):
        db.session.add(self)
        db.session.commit()     


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    products = db.relationship('Product', backref = 'category')

    def __init__(self, title):
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()     


class ProductReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String(255))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, message, name, email, product_id):
        self.message = message
        self.name = name
        self.email = email
        self.product_id = product_id

    def save(self):
        db.session.add(self)
        db.session.commit()    


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    company = db.Column(db.String(100))
    message = db.Column(db.String(255))
    is_subscribe = db.Column(db.Boolean)

    def __init__(self, name, email, company, message, is_subscribe):
        self.name = name
        self.email = email
        self.company = company
        self.message = message
        self.is_subscribe = is_subscribe

    def save(self):
        db.session.add(self)
        db.session.commit() 