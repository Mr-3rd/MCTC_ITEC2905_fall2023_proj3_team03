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
        db.connect()

        bookmark_recall = Car_Recall(
            year=top_recall_dict['year'],
            make=top_recall_dict['make'],
            model=top_recall_dict['model'],
            photo_title=top_recall_dict['photo_title'],
            photo_link=top_recall_dict['photo_link'],
            photo_error=top_recall_dict['photo_error'], 
            recall_date=top_recall_dict['recall_date'],
            recall_component=top_recall_dict['recall_component'],
            recall_summary=top_recall_dict['recall_summary'],
            recall_error=top_recall_dict['recall_error'],
            video_title=top_recall_dict['video_title'],
            video_embed=top_recall_dict['video_embed'],
            video_error=top_recall_dict['video_error'],
            shop_url=top_recall_dict['shop_url'],
            shop_name=top_recall_dict['shop_name'],
            shop_rating=top_recall_dict['shop_rating'], 
            shop_address=top_recall_dict['shop_address'],
            shop_city=top_recall_dict['shop_city'],
            shop_state=top_recall_dict['shop_state'],
            shop_error=top_recall_dict['shop_error']
        )

        bookmark_recall.save()


    def get_recalls():
        all_bookmarks = []
        bookmarks = Car_Recall.select()
        for bookmark in bookmarks:
            all_bookmarks.append(
                # return car
                {'year': bookmark.year, 'make': bookmark.make,
                'model': bookmark.model,
                # return photo
                'photo_title': bookmark.photo_title,
                'photo_link': bookmark.photo_link,
                'photo_error': bookmark.photo_error,
                # return recall
                'recall_date': bookmark.recall_date,
                'recall_component': bookmark.recall_component,
                'recall_summary': bookmark.recall_summary,
                'recall_error': bookmark.recall_error,
                # return video
                'video_title': bookmark.video_title,
                'video_embed': bookmark.video_embed,
                'video_error': bookmark.video_error,
                # return shop
                'shop_url': bookmark.shop_url,
                'shop_name': bookmark.shop_name,
                'shop_rating': bookmark.shop_rating,
                'shop_address': bookmark.shop_address,
                'shop_city': bookmark.shop_city,
                'shop_state': bookmark.shop_state,
                'shop_error': bookmark.shop_error}
            )

        return all_bookmarks

