"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy#import SQl SQLAlchemy
# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()#initiate SQLAlchemy object as db


##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)#if the string is optional
    password = db.Column(db.String(64), nullable=True)#can return a colums value as NULL
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):

        return "<User user_id = {} email = {}>".format(self.user_id, self.email)

# Put your Movie and Rating model classes here.

class Movie(db.Model):#Build in
    """ Rated movies. """

    __tablename__ = "movies"#creating a table, __tablename__ is a class attribute

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)#is required to create a primary key
    title = db.Column(db.String(100))
    released_at = db.Column(db.DateTime())#when the movie was released
    imdb_url = db.Column(db.String(300))

class Rating(db.Model):
    """ Movie Ratings. """

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'#ratings-we created a db with thins name
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#true will print everything in the console
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
