from app import db
from models import User

# insert data
db.create_all()
db.session.add(User("Zibi242424", "fihejook"))

# commit the changes
db.session.commit()
