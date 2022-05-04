from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# execute the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "FavPlaces" table
class FavPlaces(base):
    __tablename__ = "Favourite places"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)
    visited = Column(String)
    year_first_visited = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our FavPlaces table
malmo = FavPlaces(
    name="Malmö",
    country_name="Sweden",
    capital_city="Stockholm",
    population=300000,
    visited="Yes",
    year_first_visited=1992
)

staffanstorp = FavPlaces(
    name="Staffanstorp",
    country_name="Sweden",
    capital_city="Stockholm",
    population=20000,
    visited="Yes",
    year_first_visited=2012
)


# add each instance of our places to our session
# session.add(malmo)
# session.add(staffanstorp)


# commit our session to the database
session.commit()


# query the database to find all places
places = session.query(FavPlaces)
for place in places:
    print(
        place.id,
        place.name,
        place.country_name,
        place.capital_city,
        place.population,
        place.visited,
        place.year_first_visited,
        sep=" | "
    )
