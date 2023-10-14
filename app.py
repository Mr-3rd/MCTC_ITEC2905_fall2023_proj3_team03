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

    car_recalls = car_recall_api(car)
    car_photos = photo_api(car)
    car_videos = video_api(car)
    car_shops = shops_api(car)

    return render_template('car_recalls.html', car_recalls=car_recalls, 
                           car_photos=car_photos, car_videos=car_videos, car_shops=car_shops)
    

if __name__ == '__main__':
    app.run()