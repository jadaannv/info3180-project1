from . import db 

class PropertyDisplay(db.Model):
    __tablename__ = 'property_list'

    #column names 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(300))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.String(50))
    propertytype = db.Column(db.String(20))
    image = db.Column(db.String(255))
    
    def __init__(self, title, bedrooms, bathrooms, location, price, propertytype, description, image):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.propertytype = propertytype
        self.image = image 
