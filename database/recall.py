from peewee import *

db = SqliteDatabase('top_recall_bookmarks.sqlite')

class Car_Recall(Model):
    # save car
    year =CharField()
    make = CharField()
    model = CharField()
# save photo 
    photo_title = CharField()
    photo_link = CharField()
    photo_error = CharField()
#  Save Recall
    recall_date = CharField()
    recall_component = CharField()
    recall_summary = CharField()
    recall_error = CharField()
# <!-- Save the video -->
    video_title = CharField()
    video_embed = CharField()
    video_error = CharField()
# <!-- Save the shop -->
    shop_url = CharField()
    shop_name = CharField()
    shop_rating = CharField()
    shop_address = CharField()
    shop_city = CharField()
    shop_state = CharField() 
    shop_error = CharField()

    class Meta:
        database = db

    def create_db():
        db.connect()
        db.create_tables([Car_Recall])

    def save_recall(top_recall_dict):

        data = {'year': '2012', 'make': 'Fiat', 'model': '500', 'photo_title': '2012 Fiat 500 Abarth', 
                'photo_link': 'https://live.staticflickr.com/7207/6838497826_533da1c937_w.jpg', 'photo_error': 'None', 
                'recall_date': '15/11/2019', 'recall_component': 'Power Train:Automatic Transmission:Lever And Linkage:Floor Shift', 
                'recall_summary': 'Chrysler (fca us llc) is recalling certain 2012-2013 fiat 500 vehicles equipped with 6-speed automatic transmissions.  the shifter cable bushing may fail allowing the cable to detach from the transmission.', 
                'recall_error': 'None', 'video_title': 'Easy Transmission Shift Cable Bushing Replacement: HOW TO ESCAPE', 
                'video_embed': 'https://www.youtube.com/embed/G4V32X0XSxU', 'video_error': 'None', 
                'shop_url': 'https://www.yelp.com/biz/fiat-of-minneapolis-minneapolis-4?adjust_creative=VFkkfbqQacs_VkhToIhzCw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=VFkkfbqQacs_VkhToIhzCw', 
                'shop_name': 'FIAT of Minneapolis', 
                'shop_rating': "({'name': 'FIAT of Minneapolis', 'url': 'https://www.yelp.com/biz/fiat-of-minneapolis-minneapolis-4?adjust_creative=VFkkfbqQacs_VkhToIhzCw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=VFkkfbqQacs_VkhToIhzCw', 'rating': 4.0, 'street_address': '1820 Quentin Ave', 'city': 'Minneapolis', 'state': 'MN'}, Undefined)", 'shop_address': '1820 Quentin Ave', 'shop_city': 'Minneapolis', 'shop_state': 'MN', 'shop_error': 'None'}


        #create db insert
        return 'Data Stored'


    def get_recalls():
        all_bookmarks = []
        bookmarks = Car_Recall.select()
        for bookmark in bookmarks:
            all_bookmarks.append({
                # return car
                {'year': bookmark.year},
                {'make': bookmark.make},
                {'model': bookmark.model},
                # return photo
                {'photo_title': bookmark.photo_title},
                {'link': bookmark.photo_link},
                {'photo_error': bookmark.photo_error},
                # return recall
                {'date': bookmark.recall_date},
                {'component': bookmark.recall_component},
                {'summary': bookmark.recall_summary},
                {'photo_error': bookmark.photo_error},
                # return video
                {'video_title': bookmark.video_title},
                {'embed': bookmark.embed},
                {'video_error': bookmark.video_error},
                # return shop
                {'url': bookmark.shop_url},
                {'name': bookmark.shop_rating},
                {'rating': bookmark.shop_rating},
                {'address': bookmark.shop_street},
                {'city': bookmark.shop_city},
                {'state': bookmark.shop_state},
                {'shops_error': bookmark.shop_error}
            })

        return all_bookmarks

