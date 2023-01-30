"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/calculateBMI/<float:weight>/<float:height>')
def calculateBMI(height, weight):
    bmi = round(weight/(height*height), 3)

    if bmi>31:
        descr = 'Your bmi is', bmi,'Silly and fat!!!'

    elif bmi>19:
        descr = 'Your Body Mass Index is', bmi, 'You have a healthy weight for your height'

    elif bmi<=19:
        descr = 'Your Body Mass Index is', bmi ,'Underweight! skinny fr!!'

    return jsonify({"BMI":bmi, 
            "Description":descr})


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
