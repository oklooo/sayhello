from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200))
    sender = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)