from peewee import *

db = SqliteDatabase('car_recall_bookmarks.sqlite')

class Car_Recall(Model):
    year = IntegerField()
    make = CharField()
    model = CharField()

    photo_title = CharField()
    photo_link = CharField()
    photo_error = CharField()

    



    class Meta:
        database = db

    def get_recall(self):
        return f'{self.id}, {self.name}, {self.color}, {self.age}'