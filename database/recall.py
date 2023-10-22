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

    def get_recalls():
        bookmarks = Car_Recall.select()
        for bookmark in bookmarks:
            return {
                # return car
                {'year': bookmark['year']},
                {},
                {},
                # return photo
                {},
                {},
                {},
                # return recall
                {},
                {},
                {},
                # return video
                {},
                {},
                {},
                # return shop
                {},
                {},
                {},
            }

db.connect()
db.create_tables([Car_Recall])