from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(55), nullable = False)
    email = db.Column(db.String(200), nullable = True)
    blogs = db.relationship('Blog', backref = 'user')

    def __init__(self, username, email):
        self.username = username
        self.email = email

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

    def __init__(self, title, description, image, price, quantity):
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        self.quantity = quantity

    def save(self):
        db.session.add(self)
        db.session.commit()     