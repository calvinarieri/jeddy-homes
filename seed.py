from models import Properties, Location, db
from app import app

with app.app_context():
    # Create sample location data
    # location1 = Location(id=1, county='Nairobi')
    # location2 = Location(id=2, county='Nairobi')

    # db.session.add_all([location1, location2])
    # db.session.commit()

    # Create sample property data
    locations = [
        Location(county='County A', subcounty='Subcounty A', street='Street A', more_description='Description A', town='Town A', area='Area A'),
        Location(county='County B', subcounty='Subcounty B', street='Street B', more_description='Description B', town='Town B', area='Area B'),
        # Add more locations as needed
    ]

    db.session.add_all(locations)
    db.session.commit()
    property1 = Properties(
        property_name='Sample Property 1',
        client_name='Client A',
        contact_number='123-456-7890',
        property_type='Residential',
        contact_email='clienta@example.com',
        precise_location='123 Main St, City, Country',
        more_description='A cozy home',
        status='Available',
        amount=200000,
        max_amount=250000,
        location=3,  # Assuming you want to associate it with location1
        created_at= None,
        updated_at= None
    )

    property2 = Properties(
        property_name='Sample Property 2',
        client_name='Client B',
        contact_number='987-654-3210',
        property_type='Commercial',
        contact_email='clientb@example.com',
        precise_location='456 Oak St, City, Country',
        more_description='Spacious office space',
        status='Occupied',
        amount=500000,
        max_amount=600000,
        location=3,  # Assuming you want to associate it with location2
        created_at= None,
        updated_at= None
    )

    db.session.add_all([property1, property2])
    db.session.commit()

    print("Seed data has been added to the database.")
