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
    # car = {'year': year, 'make': make, 'model': model }

    car_recalls = car_recall_api.get_car_recall(year, make, model)
    if type(car_recalls) != str:
        car_photos = photo_api.get_car_images(year, make, model)
        car_videos = video_api.get_car_videos(year, make, model, car_recalls)
        car_shops = shops_api.get_shops(year, make, model)

    if type(car_recalls) == str or type(car_photos) == str or type(car_videos) == str or type(car_shops) == str:
        return render_template('error.html', error='Generic Error Found')
    else:
        return render_template('car_recalls.html', year=year,make=make,model=model,car_recalls=car_recalls, 
                           car_photos=car_photos, car_videos=car_videos, car_shops=car_shops)
        
    

if __name__ == '__main__':
    app.run()