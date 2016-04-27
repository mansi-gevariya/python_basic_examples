
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:mansi@localhost:3306/EmpData', echo=True)
Base.metadata.reflect(engine)
app = Flask(__name__)


class User(Base):
    __table__ = Base.metadata.tables['User']


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/Authenticate')
def authenticate():

    from sqlalchemy.orm import scoped_session, sessionmaker
    db_session = scoped_session(sessionmaker(bind=engine))
    if db_session.query(User):
        return "Logged in successfully"
    else:
        return "Username or Password is wrong"

if __name__ == '__main__':
    app.run()

