from app import db
from models import *

db.create_all()

#db.session.add(BlogPost("Good", "I'm great"))
#db.session.add(BlogPost("Well", "I'm well"))

db.session.commit()