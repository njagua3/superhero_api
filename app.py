from flask import Flask  # Import Flask to create the web application
from flask_migrate import Migrate  # Import Flask-Migrate to handle database migrations
from models import db  # Import the SQLAlchemy database instance
from routes import api  # Import the Blueprint with all the routes
from config import Config  # Import the configuration settings for the app

# Initialize the Flask application
app = Flask(__name__)  # Create a Flask app instance
app.config.from_object(Config)  # Load configuration settings from the Config class

# Initialize the database and set up migrations
db.init_app(app)  # Bind the database (SQLAlchemy) to the Flask app
migrate = Migrate(app, db)  # Set up Flask-Migrate to handle database migrations

# Register the API blueprint to handle all API routes
app.register_blueprint(api, url_prefix='/api')  # Prefix all routes from the 'api' Blueprint with '/api'

# Define a simple home route
@app.route('/')
def index():
    # Return a welcome message for the root URL
    return "This is Nyingi Kevin. Welcome to the Superhero API!"

# Run the application when the script is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)  # Start the app on port 5555 with debug mode enabled
