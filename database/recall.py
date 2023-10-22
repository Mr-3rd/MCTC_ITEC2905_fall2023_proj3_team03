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

