from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # name = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)
    first_name = db.Column( db.String(80),  nullable=True)
    last_name = db.Column( db.String(80),  nullable=True)
    national_id = db.Column( db.Integer,  nullable=True)
    nationality  = db.Column( db.String(80),  nullable=True)
    gender = db.Column( db.String(80),  nullable=True)
    date_of_birth = db.Column( db.String(80),  nullable=True)
    mobile_number = db.Column( db.Integer,  nullable=True)
    user_type = db.Column( db.String(80),  nullable=True)
    profile_pic = db.Column( db.String(80),  nullable=True)



    def __repr__(self):
        return '<User %r>' % self.username
    
class Event(db.Model):
    __tablename__ = "events"
    
    event_id = db.Column( db.Integer,  primary_key=True)
    acud_id = db.Column( db.String(80),  nullable=False)
    category  = db.Column( db.String(80),  nullable=False)
    time = db.Column( db.String(80),  nullable=False)
    venue_id = db.Column( db.String(80),  nullable=False)
    description = db.Column( db.String(150),  nullable=True)
    n_of_attendees  = db.Column( db.Integer,  nullable=False)
    indoor = db.Column( db.Integer,  nullable=False)
    catering_id = db.Column( db.Integer,  nullable=False)
    event_planner_id = db.Column( db.Integer,  nullable=False)
    # @classmethod
    
    
    def hall_name(self):
        halls = {
            "h1": ['static/assets/media/new/H.png','قاعة اللوتس']
        }
        
        return halls[self.venue_id]
    def hall_pic(self):
        return "new/H.png"
    def planner_data(self):
        planners = {'org1pack1': ['monasba ', 'package 1 ', 2000, 'org1.png'],
 'org1pack2': ['monasba ', 'package 2 ', 3000, 'org1.png'],
 'org2pack1': ['candor', 'package 1 ', 1500, 'org2.png'],
 'org2pack2': ['candor', 'package 2 ', 2200, 'org2.png'],
 'org3pack1': ['planiro', 'package 1 ', 1700, 'org3.png'],
 'org3pack2': ['planiro', 'package 2 ', 2700, 'org3.png']}
    
        return planners[self.event_planner_id]
    def catering_data(self):
        catering = {'f1p1': ['200 جاتوه\n1 كعك ', 2000, 'image1.png', 'la poire'],
 'f1p2': ['\n100 جاتوه\n1 كعك ', 1200, 'image1.png', 'la poire'],
 'f2p1': ['\n100 جاتوه\n1 كعك ', 720, 'image2.png', 'monginis'],
 'f2p2': ['\n3 جاتوه\n3 كعك ', 720, 'image2.png', 'monginis'],
 'f3p2': ['\n3 جاتوه\n3 كعك ', 720, 'image2.png', 'monginis']}

        return catering[self.catering_id]

