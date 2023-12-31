from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __str__(self): 
        return f"User {self.id} ({self.email}), age {self.age}, registered on {self.timestamp}"