from flask_restful import Resource
from flask import make_response, jsonify, request
from models import db , Properties as P

class Property(Resource):
    def get(self):
        try:
            properties = [property.to_dict() for property in P.query.all()]
            if len(properties) > 2:
                return make_response(
                    jsonify(properties), 200
                )
            return make_response(
                'propeties not found' , 404
            )
        except Exception:
            return 'Server error!', 500
    def post(self):
            data = request.get_json()
        
            try:
                property = P(
                    property_name=data.get('property_name'),
                    client_name=data.get('client_name'),
                    contact_number= data.get('contact_number'),
                    property_type=data.get('property_type'),
                    contact_email=data.get('contact_email'),
                    precise_location=data.get('precise_location'),
                    more_description=data.get('more_description'),
                    status=data.get('status'),
                    amount=data.get('amount'),
                    max_amount=data.get('max_amount'),
                    location=5,  # Assuming you want to associate it with location2
                    created_at= None,
                    updated_at= None
                )
                db.session.add(property)
                db.session.commit()
                return make_response(
                     jsonify(property.to_dict())
                )
            except NotImplementedError:
                 return 'server error', 500

class SpecificProperty(Resource):
     def get(self, id):
          property = P.query.filter_by(id=id).first()
          if property:
               return make_response(
                    jsonify(property.to_dict()), 200
               )
          return 'Property Not found', 404
     
     def patch(self, id):
        property = P.query.filter_by(id=id).first()
        if property:
            data = request.get_json()

            for attr in data:
                 setattr(property, attr, request.get_json().get(attr))
            try:
                db.session.add(property)
                db.session.commit()
                return make_response(
                     jsonify(property.to_dict())
                )
            except Exception:
                 return 'server error', 100
            
     def delete(self, id):
        property = P.query.filter_by(id=id).first()
        if property:
            try:
                db.session.delete(property)
                db.session.commit()
                return 'deleted successfully!' , 200
            except Exception:
                return 'Not deleted', 500
        return 'Property does not exist', 404
                 


