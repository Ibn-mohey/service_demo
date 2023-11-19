from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
class Event(db.Model):
    __tablename__ = "events"
    
    event_id = db.Column( db.Integer,  primary_key=True)
    acud_id = db.Column( db.String(80),  nullable=False)
    category  = db.Column( db.String(80),  nullable=False)
    time = db.Column( db.String(80),  nullable=False)
    venue_id = db.Column( db.String(80),  nullable=False)
    description = db.Column( db.String(150),  nullable=False)
    n_of_attendees  = db.Column( db.Integer,  nullable=False)
    indoor = db.Column( db.Integer,  nullable=False)
    catering_id = db.Column( db.Integer,  nullable=False)
    event_planner_id = db.Column( db.Integer,  nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username