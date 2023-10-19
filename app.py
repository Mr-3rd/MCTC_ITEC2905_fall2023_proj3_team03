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
    errors = []

    # Convert into car model
    year = request.args.get('year')
    make = request.args.get('make')
    model = request.args.get('model')

    recall_error, car_recalls = car_recall_api.get_car_recall(year, make, model)
    photo_error, car_photos = photo_api.get_car_images(year, make, model)
    if car_recalls != None:
        video_error, car_videos = video_api.get_car_videos(year, make, model, car_recalls)
    else:
        video_error = "No Recalls are present"
        car_videos = None 
    shops_error, car_shops = shops_api.get_shops(year, make, model)
    return render_template('car_recalls.html', year=year,make=make,model=model, recall_error=recall_error, 
                           photo_error=photo_error, car_recalls=car_recalls, car_photos=car_photos, car_videos=car_videos, 
                           car_shops=car_shops, video_error=video_error , shops_error=shops_error )
    

if __name__ == '__main__':
    app.run()