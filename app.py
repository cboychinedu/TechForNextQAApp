#!/usr/bin/env python3

# Importing the necessary modules
import os
import logging
from flask import Flask, url_for, session
from flask_cors import CORS
from datetime import timedelta

# Importing the views
from Home.routes import home

# Creating the flask application
app = Flask(__name__, static_folder=None, template_folder=None)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "kdsd8*DEKFE!@$#$$REDKDNI*(KEHE&E&^"
app.permanent_session_lifetime = timedelta(days=24)


# # Logging the configurations to a file on disk
logging.basicConfig(filename="Logs/requests.log", level=logging.DEBUG,
                    format="%(asctime)s %(message)s %(filename)s %(module)s %(pathname)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p")

# Register the views using the "app.register" function
app.register_blueprint(home, url_prefix="/")

# Running the flask application
if __name__ == "__main__":
    app.run(port=5001,
            host="localhost",
            debug=True
            )
    # Running the application
    app.run()
