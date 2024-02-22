from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Users(db.Model, SerializerMixin):
    __tablename__ = 'users'
   

    id = db.Column(db.Integer , primary_key = True)
    firstname = db.Column(db.String )
    secondname = db.Column(db.String )
    email = db.Column(db.String )
    phone_number = db.Column(db.String )
    role = db.Column(db.String )
    password = db.Column(db.String )
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __str__(self):
        return f'{self.firstname} {self.secondname}'


class Properties(db.Model, SerializerMixin):
    __tablename__ = 'properties'
    serialize_rules = ('-property_location.properties')

    id = db.Column(db.Integer , primary_key = True)
    property_name = db.Column(db.String)
    client_name = db.Column(db.String)
    contact_number = db.Column(db.String)
    property_type = db.Column(db.String)
    contact_email = db.Column(db.String)
    precise_location = db.Column(db.String)
    more_description = db.Column(db.String)
    status = db.Column(db.String)
    amount = db.Column(db.Integer)
    max_amount = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    location = db.Column(db.Integer , db.ForeignKey('location.id'))

    def __repr__(self):
        return f'<Properties {self.id} of {self.property_name} >'
    
    def to_dict(self):
        return {
            'id': self.id,
            'property_name': self.property_name,
            'client_name': self.client_name,
            'contact_number': self.contact_number,
            'property_type': self.property_type,
            'contact_email': self.contact_email,
            'precise_location': self.precise_location,
            'more_description': self.more_description,
            'status': self.status,
            'amount': self.amount,
            'max_amount': self.max_amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'location_id': self.location
        }

class Location(db.Model, SerializerMixin ):
    __tablename__ = 'location'
    serialize_rules = ('-properties.property_location')

    id = db.Column(db.Integer, primary_key = True)
    county = db.Column(db.String)
    subcounty = db.Column(db.String)
    street = db.Column(db.String)
    more_description = db.Column(db.String)
    town = db.Column(db.String)
    area = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    properties = db.relationship('Properties' , backref ='property_location')

class Messages(db.Model, SerializerMixin):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    message = db.Column(db.String)
    type = db.Column(db.String)
    status = db.Column(db.String)
    phone_number = db.Column(db.String)

class Careers (db.Model, SerializerMixin):
    __tablename__ = 'careers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    number_required = db.Column(db.String)
    more_description = db.Column(db.String)
    academic_requirement = db.Column(db.String)
    age_requirement = db.Column(db.String)
    highest_education = db.Column(db.String)
    application_deadline = db.Column(db.DateTime)
    salary = db.Column(db.Integer)