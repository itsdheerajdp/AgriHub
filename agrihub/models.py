from datetime import datetime
from agrihub import db,login_manager
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    return Farmer.query.get(int(user_id))

@login_manager.user_loader
def load_user(user_id):
    return Buyer.query.get(int(user_id))

class Farmer(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    crops = db.Column(db.String(50),nullable=False,default='')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Buyer(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    

class Crop(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    price=db.Column(db.Integer,nullable=False)
    farmer_address=db.Column(db.String(100),nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)

     

    def __repr__(self):
        return f"Post('{self.crop_name}', '{self.date_posted}')"