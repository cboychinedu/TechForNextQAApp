#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
import json 
import bcrypt
from flask import jsonify, session, redirect, request 
from flask import Blueprint 
from mongo import MongoDB
from flask import session, flash 
from flask import render_template, redirect, url_for 

# Creating the blueprint object 
home = Blueprint('home', __name__, template_folder='templates', static_folder='static'); 

# Creating an instance of the database 
db = MongoDB(); 

# Creating the home page 
@home.route("/", methods=["GET"])
def homePage():
    # Checking if the user is logged in 
    if 'email' in session: 
        # Getting the email 
        email = session['email']

        return redirect('/dashboard')
    
    # Checking if the request was a post request 
    if request.method == 'POST': 
        # Getting the email, and password data from the 
        # request body 
        requestData = request.get_json()
        emailAddress = requestData['email']
        password = requestData['password']
        print(requestData)

        return; 

        # Geteting the user's data by connecting to the Mongodb database 
        db.connect('mongodb://localhost:27017/', 'techForNext')
        databaseData = db.retrieve_data('users', emailAddress)

        # If the database value return a None type, execut the 
        # block of code below 
        if databaseData == None: 
            return { "message": "User not found on the database", "status": "errror"}, 500; 

        # Convertng the json string into a json object using the 
        # json module 
        databaseData = json.loads(databaseData.json);

        # If the user is found on the database with the specified email address, 
        # execute the block of code below 
        if databaseData: 
            # Validate the user's password 
            passwordCondition = bcrypt.checkpw(password.encode('utf-8'), databaseData['password'].encode('utf-8'))

            # Checking if the password condition returned a True, or false value 
            if (passwordCondition == True): 
                # Give the user a session value, and redirect the user's to the 
                # Dashboard page 
                session['email'] = email 

                # Creaging the success message 
                successMessage = {
                    "status": "success", 
                    "message": "User logged in", 
                    "statusCode": 200, 
                }

                # Sending the error message 
                return successMessage; 

            elif (passwordCondition == False): 
                # Creating the error message 
                errorMessage = {
                    "status": "error", 
                    "message": "Invalid username or password", 
                    "statusCode": 500, 
                }

                # Sending back the error message 
                return errorMessage; 
        else: 
            # Creating the error message 
            errorMessage = {
                "status": "error", 
                "message": "User not found on the database", 
                "statusCode": 501, 
            }

            # Returning the database data 
            return errorMessage; 

    else:
        # Rendering the html template file 
        return render_template('home.html'); 


@home.route('/signUp', methods=["POST", "GET"])
def signUp(): 
    # Checking if the user is logged in 
    if 'email' in session: 
        email = session['email']

        # Render the dashboard page 
        return render_template('Dashboard.html')
    
    # Checking if the request made was a post request 
    if request.method == "POST":
        # Getting the firstname, lastname, email, and password data 
        requestData = request.get_json();
        print(requestData)

        fullname = requestData["fullname"]
        emailAddress = requestData['email']; 
        password = requestData["password"] 

        # Connecting to the Mongodb database, and save the users data 
        db.connect('mongodb://localhost:27017/', 'techForNext')


        """
         Here, we need to verify if the user's data are already registered 
         on the mongodb database before saving the new data to the server. 
         And if the user exists, redirect the user to the login page. 
        """
        databaseData = db.retrieve_data('users', emailAddress)

        # Hashing the password 
        hashPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)); 
        hashPassword = hashPassword.decode('utf-8'); 
    
        # Rebuilding the request data 
        requestData = {
            "fullname": fullname, 
            "email": emailAddress, 
            "password": hashPassword
        }

        # Checking if the returned type if None, execute the 
        # block of code below 
        if databaseData == None: 
            # Save the new user on the database 
            result = db.save_data('users', requestData)

            # Checking if the results return a value 
            if (result): 
                return jsonify({
                    "status": "success", 
                    'message': 'User\'s data saved on the database'
                }), 200 
            else: 
                return jsonify({
                    "status": "error", 
                    "message": 'Unable to save the user\'s data on the database'
                }), 500

        else: 
            return jsonify({'status': 'error', 'message': 'The user already exists on the database.'}), 501

    # If the request is GET, execute the block of code below 
    elif request.method == "GET": 
        # Rendering the signUp template file 
        return render_template('signUp.html')
    


# Creating the dashboard route 
@home.route('/dashboard', methods=["POST", "GET"])
def Dashboard(): 
    # 
    pass 


# Creating the sign out route 
@home.route("/logout", methods=["GET"])
def Logout():
    # Removing the email from the session storage 
    session.pop("email", None); 

    # Redirecting the user back to the home page 
    return redirect(url_for("home.HomePage"))