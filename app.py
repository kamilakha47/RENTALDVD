from flask import Flask, jsonify, json, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy()

POSTGRES = {
    'user': 'postgres',
    'pw' : '24434',
    'db' : 'dvdrental',
    'host' : 'localhost',
    'port' : '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
ma = Marshmallow(app)
from models import City, CitySchema, Country, CountrySchema

cities_schema = CitySchema(many=True)
city_schema = CitySchema()
country_schema = CountrySchema()

#CITY

@app.route('/city', methods=['GET'])
def get_cities():
    try:
        cities = City.query.all()
        return jsonify(data = cities_schema.dump(cities))
    except Exception as e:
        return jsonify(error = str(e))

@app.route('/city/<_id>', methods=['GET'])
def get_city_by_id(_id):
    try:
        city = City.query.filter_by(city_id=_id).first()
        return jsonify(city_schema.dump(city))
    except Exception as e:
        return jsonify(error = str(e))

@app.route('/city/add', methods=['POST'])
def add_city():
    body = request.json
    city = body.get("city")
    country_id = body.get("country_id")
    try:
        city = City(city,country_id)
        db.session.add(city)
        db.session.commit()
        return jsonify(city_schema.dump(city))
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/city/<_id>', methods=['PUT'])
def update_city(_id):
    body = request.json
    city_name = body.get("city")
    country_id = body.get("country_id")
    try:
        city = City.query.filter_by(city_id=_id).first()
        city.city = city_name
        city.country_id = country_id
        db.session.commit()
        return jsonify(city_schema.dump(city))
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/city/<_id>', methods=['DELETE'])
def remove_city(_id):
    try:
        city = City.query.filter_by(city_id=_id).first()
        db.session.delete(city)
        return jsonify(city_id=_id)
    except Exception as e:
        return jsonify(error=str(e)) 


#COUNTRY

@app.route('/country/<_id>', methods=['GET'])
def get_country_by_id(_id):
    try:
        country = Country.query.filter_by(country_id=_id).first()
        return jsonify(country_schema.dump(country))
    except Exception as e:
        return jsonify(error = str(e))


@app.route('/country/add', methods=['POST'])
def add_country():
    body = request.json
    country = body.get("country")
    try:
        country = Country(country)
        db.session.add(country)
        db.session.commit()
        return jsonify(country_schema.dump(country))
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/country/<_id>', methods=['PUT'])
def update_country(_id):
    body = request.json
    country_name = body.get("country")
    try:
        country = Country.query.filter_by(country_id=_id).first()
        country.country = country_name
        db.session.commit()
        return jsonify(country_schema.dump(country))
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/country/<_id>', methods=['DELETE'])
def remove_country(_id):
    try:
        country = Country.query.filter_by(country_id=_id).first()
        db.session.delete(country)
        return jsonify(country_id=_id)
    except Exception as e:
        return jsonify(error=str(e)) 