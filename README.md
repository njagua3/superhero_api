# Superhero API

## Overview

This project is a simple API (Application Programming Interface) for tracking superheroes and their powers. Think of it like a mini-database where you can store information about heroes, their superpowers, and how strong they are with each power.

This API lets you do four main things:
1. See a list of all heroes.
2. See a list of all superpowers.
3. See which hero has which powers and how strong they are.
4. Add new heroes, powers, and combinations of heroes and their powers.

## What This Project Does

Imagine you are building a system to keep track of heroes like Spider-Man and their superpowers (like "web-swinging" or "super strength"). The API allows you to:

- Add new heroes.
- Add superpowers.
- Show which heroes have which powers.
- Track how strong each hero is with a particular power (e.g., Spider-Man is "strong" at web-swinging, but maybe just "average" at using super strength).

### Project Structure

- **Heroes**: These are the people with superpowers (e.g., Spider-Man, Superman).
- **Powers**: These are the abilities the heroes have (e.g., flying, super strength).
- **HeroPower**: This is where we keep track of which hero has which powers, and how strong they are with each power.

## How It Works (Step by Step)

### 1. Setting Up the Project

To use this API on your local machine, follow these steps:

1. **Clone the project** 
   
   git clone <repo url>
   cd superhero_api

2. Set up a virtual environment (this is like creating a separate area on your computer to install software for this project):

python3 -m venv venv
source venv/bin/activate  # Activate the virtual environment

3. Install required software: The project needs some extra software to work. These are listed in a file called requirements.txt. Install them by running this command:

pip install -r requirements.txt

4. Set up the database: We need to create a database (this is where all the hero and power information is stored). Run the following commands to set it up:
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

5. Add some starting data: The project comes with a script to add some heroes and powers to the database so you can test the API right away:
python seed.py

6. Run the application: You can now run the application and start using the API by executing:

python app.py


The application will be available at http://127.0.0.1:5555/


Using the API
Once the project is running, you can interact with it using an API tool like Postman or directly from your web browser.

Available Actions (Endpoints)
1. Get a List of All Heroes

URL: /api/heroes
Method: GET
Response: A list of all heroes with their names and superhero identities.

## Postman Collection

To help you test the API endpoints, a Postman collection has been provided.

### How to Import Postman Collection:

1. **Download the Postman Collection:**
   - You can find the collection in this repository: `challenge-2-superheroes.postman_collection.json`.

2. **Open Postman:**
   - If you don't have Postman installed, you can download it from [Postman Download](https://www.postman.com/downloads/).

3. **Import the Collection:**
   - In Postman, click on the **Import** button (usually at the top left).
   - Select the **Upload Files** option.
   - Navigate to the folder where this repo is located and select the file: `challenge-2-superheroes.postman_collection.json`.
   - Once imported, you will see the collection in the sidebar under **Collections**.

4. **Test the API:**
   - Expand the collection to see all available endpoints.
   - Make sure your API is running, and then you can start testing the endpoints by selecting one and clicking **Send**.


