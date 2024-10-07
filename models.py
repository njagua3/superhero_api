# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String, nullable=False)  # Hero's name
    super_name = db.Column(db.String, nullable=False)  # Hero's superhero name

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String, nullable=False)  # Name of the power
    description = db.Column(db.String, nullable=False)  # Description of the power

    # Validation: Ensure description is at least 20 characters long
    __table_args__ = (
        CheckConstraint('length(description) >= 20', name='check_description_length'),
    )

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    strength = db.Column(db.String, nullable=False)  # Strength of the power

    # Validation: Ensure strength is one of the predefined values
    __table_args__ = (
        CheckConstraint(strength.in_(['Strong', 'Weak', 'Average']), name='check_strength_value'),
    )

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)  # Foreign key to Hero
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)  # Foreign key to Power

    hero = db.relationship('Hero', back_populates='hero_powers')  # Relationship to Hero
    power = db.relationship('Power', back_populates='hero_powers')  # Relationship to Power

    def to_dict(self):
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "strength": self.strength,
            "hero": self.hero.to_dict(),
            "power": self.power.to_dict()
        }
