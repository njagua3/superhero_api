from app import app  # Importing the Flask app instance from the app module
from models import db, Hero, Power, HeroPower  # Importing the database and models

# Seed the database with initial data
with app.app_context():  # Ensures the app context is active to interact with the database
    # Drop and create all tables: This deletes all existing data and recreates the tables from scratch
    db.drop_all()  
    db.create_all()

    # Create a list of hero objects to be added to the database
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
    ]
    
    # Create a list of power objects to be added to the database
    powers = [
        Power(name="Super Strength", description="gives the wielder super-human strengths"),
        Power(name="Flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="Elasticity", description="can stretch the human body to extreme lengths"),
    ]

    # Add the created hero and power objects to the current database session (prepares them for insertion)
    db.session.add_all(heroes)
    db.session.add_all(powers)
    
    # Commit the session to the database, saving the changes (inserts the heroes and powers into the database)
    db.session.commit()

    print("Database seeded!")  # Message to indicate that the seeding process is complete
