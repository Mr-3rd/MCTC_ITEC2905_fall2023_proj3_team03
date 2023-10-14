"""
Main Location to develop code

"""

from flask import Flask, render_template, request  # NOT the same as requests 
from apis import car_recall_api, photo_api, video_api, shops_api

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('car_input.html')


#create the function to respond to requests from the HTML form 
@app.route('/get_car')  #must match the call url exactly
def get_car_recall():

    # Convert into car model
    year = request.args.get('year')
    make = request.args.get('make')
    model = request.args.get('model')
    car = {'year': year, 'make': make, 'model': model }

    car_recalls = 

    return render_template('github.html', user_data=user_data)

    

if __name__ == '__main__':
    app.run()