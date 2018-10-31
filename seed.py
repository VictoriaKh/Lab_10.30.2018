"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import User
# from model import Rating
from model import Movie

from model import connect_to_db, db
from server import app
from datetime import datetime




def load_users():
    """Load users from u.user into database."""

    print("Users")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read u.user file and insert data
    for row in open("seed_data/u.user"):
        row = row.rstrip()
        user_id, age, gender, occupation, zipcode = row.split("|")

        user = User(user_id=user_id,
                    age=age,
                    zipcode=zipcode)

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

    # Once we're done, we should commit our work
    db.session.commit()


def load_movies():
    """Load movies from u.item into database."""

    Movie.query.delete()


    with open ("seed_data/u.item") as items:
        for string in items:
            string = string.rstrip().split("|")
            new_string = string[:5]
            # print(new_string)


            movie_id, title, released_at, something, imdb_url = new_string
            # for movie in title.split():
            #     movie = title[0]
            newTitle = title.split() # ['toy', 'story', '(1995)']
            i = newTitle[:-1] # ['toy', 'story']
            new_word = ' '.join(i) # 'toy story'
            # print(new_word)


            # released_at = 20-Jun-1997
            s = released_at
            d = datetime.strptime(s, '%d-%b-%Y')
            # prettyRelease = d.strftime('%A, %B %d %Y')





            movie = Movie(movie_id=movie_id,
                        title=new_word,
                        released_at=d,
                        imdb_url=imdb_url)

            db.session.add(movie)

    # Once we're done, we should commit our work
    db.session.commit()

                        



def load_ratings():
    """Load ratings from u.data into database."""


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)


    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_movies()
    load_ratings()
    set_val_user_id()
