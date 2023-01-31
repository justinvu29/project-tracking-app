from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = db.column(db.Intger, primary_key = True, autoincrement = True)
    username = db.Column(db.string(255), unique = True, nullable = False)
    password = db.Column(db.string(255), nullable = False) 