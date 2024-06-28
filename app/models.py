from app import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    evaluation_reason = db.Column(db.String(200), nullable=True)
    evaluator = db.Column(db.String(100), nullable=True)
