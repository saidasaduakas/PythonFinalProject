from re import U
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'



convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)


       
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, id, login, password, token):
        self.id=id
        self.login =login
        self.password=password
        self.token = token
        
        data = User(1,'Saida','saida',True)
        dat =User(2, 'Adi','adi',True)
        dataa=User(3,'Ali','ali',True)
        db.session.add(data)
        db.session.add(dat)
        db.session.add(dataa)

db.session.commit()
