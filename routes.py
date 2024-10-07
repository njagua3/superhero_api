from flask import Blueprint, jsonify, request  # Import Flask components for routing and JSON handling
from models import db, Hero, Power, HeroPower  # Import the database and models

# Create a Blueprint for organizing routes. A Blueprint allows grouping of routes for better modularity.
api = Blueprint('api', __name__)

# Route to fetch all heroes
@api.route('/heroes', methods=['GET'])
def get_heroes():
    # Retrieve all heroes from the database and return them as a list of dictionaries in JSON format
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200  # Return JSON response with status code 200 (OK)

# Route to fetch a single hero by ID
@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    # Retrieve a hero based on the ID provided in the URL
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict()), 200  # Return the hero data if found
    return jsonify({"error": "Hero not found"}), 404  # Return error message if hero is not found

# Route to fetch all powers
@api.route('/powers', methods=['GET'])
def get_powers():
    # Retrieve all powers from the database and return them as a list of dictionaries in JSON format
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200  # Return JSON response with status code 200 (OK)

# Route to fetch a single power by ID
@api.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    # Retrieve a power based on the ID provided in the URL
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200  # Return the power data if found
    return jsonify({"error": "Power not found"}), 404  # Return error message if power is not found

# Route to update a power's description based on its ID
@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    # Retrieve the power based on the provided ID
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404  # Return error if power does not exist
    
    data = request.get_json()  # Extract JSON data from the request
    if 'description' in data:
        power.description = data['description']  # Update the description if provided
    
    try:
        db.session.commit()  # Commit the changes to the database
        return jsonify(power.to_dict()), 200  # Return the updated power data
    except Exception as e:
        db.session.rollback()  # Rollback changes if there is an error
        return jsonify({"errors": ["validation errors"]}), 400  # Return error if validation fails

# Route to create a new HeroPower relationship
@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    # Extract data from the JSON request to create a new HeroPower
    data = request.get_json()
    hero_power = HeroPower(
        strength=data['strength'],  # Set the strength attribute
        hero_id=data['hero_id'],  # Set the hero ID for the relationship
        power_id=data['power_id']  # Set the power ID for the relationship
    )
    
    try:
        db.session.add(hero_power)  # Add the new HeroPower object to the database session
        db.session.commit()  # Commit the changes to the database
        return jsonify(hero_power.to_dict()), 201  # Return the created HeroPower data with status code 201 (Created)
    except Exception as e:
        db.session.rollback()  # Rollback changes if there is an error
        return jsonify({"errors": ["validation errors"]}), 400  # Return validation error if any
