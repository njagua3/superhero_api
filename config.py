import os  # Import the os module to access environment variables (if needed)

# Create a Config class to store configuration settings for the Flask app
class Config:
    # Define the database URI, specifying that the app will use an SQLite database called 'app.db'
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    
    # Disable SQLAlchemy's modification tracking system to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
