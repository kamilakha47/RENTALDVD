import datetime
from app import db, ma

class City(db.Model):
    __tablename__ = 'city'

    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String())
    country_id = db.Column(db.SmallInteger)
    last_update = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self, city, country_id):
        self.city = city
        self.country_id = country_id

    def __repr__(self):
        return '<city id {}>'.format(self.city_id)

class Country(db.Model):
    __tablename__ = 'country'

    country_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String())
    last_update = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self, country):
        self.country = country

    def __repr__(self):
        return '<country id {}>'.format(self.country_id)

class CitySchema(ma.Schema):
    class Meta:
        fields = ("city_id", "city", "country_id", "last_update")
        model = City

class CountrySchema(ma.Schema):
    class Meta:
        fields = ("country_id", "country", "last_update")
        model = Country