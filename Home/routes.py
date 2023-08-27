#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from quart import request 
from quart import Blueprint 
from quart import session, flash 
from quart import render_template, redirect, url_for 

# Creating the blueprint object 
home = Blueprint('home', __name__, template_folder='templates', static_folder='static'); 

# Creating the home page 
@home.route("/", methods=["GET"])
async def HomePage():
    # Rendering the html template file 
    return await render_template('home.html'); 